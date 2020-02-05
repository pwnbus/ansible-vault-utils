import shutil
import logging

from os import path, walk
from subprocess import Popen, PIPE, STDOUT

# Handle python2
try:
    input = raw_input
except NameError:
    pass

logger = logging.getLogger()
logger.level = logging.INFO
custom_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(custom_formatter)
logger.addHandler(stream_handler)


def get_input(msg):
    return input(msg).rstrip()


def run_command(cmd_str, working_dir=None):
    process = Popen(cmd_str.split(' '), cwd=working_dir, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = process.communicate()
    return stdout


def remove_repo_data(repos_path):
    if path.isdir(repos_path):
        logger.debug('Removing tmp repo data at ' + repos_path)
        shutil.rmtree(repos_path)


def clone_repo(main_repo_name, remote_branch, destination):
    remote_params = remote_branch.split(':')
    account_name = remote_params[0]
    branch_name = remote_params[1]
    full_url = 'git@github.com:' + account_name + '/' + main_repo_name
    logger.debug("Cloning {0} {1} branch into {2}".format(full_url, branch_name, destination))
    run_command('git clone --depth=1 --branch={0} {1} {2}'.format(branch_name, full_url, destination))


def decrypt_file(repo_path, file_name):
    full_file_name = path.join(repo_path, file_name)
    logger.debug('Decrypting ' + full_file_name)
    run_command('ansible-vault decrypt {0}'.format(full_file_name), repo_path)


def diff_file(source_file, destination_file):
    diff_output = run_command('git diff --no-index -- {0} {1}'.format(destination_file, source_file))
    return diff_output


def setup_repo(repo_location):
    # If we need to create a ansible.cfg file, let's do it
    if not path.isfile(path.join(repo_location, 'ansible.cfg')) and path.isfile(path.join(repo_location, 'ansible.cfg.inc')):
        run_command('cp {0}/ansible.cfg.inc {0}/ansible.cfg'.format(repo_location))

def diff_repo(source_repo_path, destination_repo_path):
    results = {}
    setup_repo(source_repo_path)
    setup_repo(destination_repo_path)
    for subdir, dirs, files in walk(source_repo_path):
        for file in files:
            source_filepath = path.join(subdir, file)
            # Skip .git files
            if '.git/' in source_filepath:
                continue
            local_repo_file = source_filepath.replace(source_repo_path + '/', '')
            destination_filepath = path.join(destination_repo_path, local_repo_file)
            if path.isfile(destination_filepath):
                with open(source_filepath, 'rb') as handler:
                    source_contents = handler.read()
                with open(destination_filepath, 'rb') as handler:
                    destination_contents = handler.read()
                if source_contents != destination_contents:
                    # If the files are encrypted...
                    if '$ANSIBLE_VAULT' in str(source_contents):
                        decrypt_file(source_repo_path, local_repo_file)
                        decrypt_file(destination_repo_path, local_repo_file)
                        diff_results = diff_file(source_filepath, destination_filepath)
                        if type(diff_results) is bytes:
                            diff_results = diff_results.decode()
                        results[local_repo_file] = diff_results
    return results


def find_str(search_string, repo_path):
    results = {}
    setup_repo(repo_path)
    for subdir, dirs, files in walk(repo_path):
        for file in files:
            source_filepath = path.join(subdir, file)
            # Skip .git files
            if '.git/' in source_filepath:
                continue
            local_repo_file = source_filepath.replace(repo_path + '/', '')
            if path.isfile(source_filepath):
                with open(source_filepath, 'rb') as handler:
                    source_contents = handler.read()
                # If the files are encrypted...
                if '$ANSIBLE_VAULT' in str(source_contents):
                    decrypt_file(repo_path, local_repo_file)
                    with open(source_filepath, 'rb') as handler:
                        source_contents = handler.read()
                try:
                    source_contents = source_contents.decode('ascii')
                except UnicodeDecodeError:
                    continue
                for line in source_contents.splitlines():
                    if search_string in line:
                        if local_repo_file not in results:
                            results[local_repo_file] = []
                        results[local_repo_file].append(line)
    return results
