try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


from ansible_vault_utils import __version__ as version


config = {
    'description': 'A suite of tools used to interact with ansible-vault encrypted repositories',
    'author': 'Brandon Myers',
    'url': 'https://github.com/pwnbus/ansible-vault-utils',
    'download_url': 'https://github.com/pwnbus/ansible-vault-utils/archive/master.zip',
    'author_email': 'pwnbus@mozilla.com',
    'version': version,
    'install_requires': [
        'six',
        'ansible'
    ],
    'packages': ['ansible_vault_utils', 'bin'],
    'scripts': [],
    'name': 'ansible_vault_utils'
}

setup(**config)
