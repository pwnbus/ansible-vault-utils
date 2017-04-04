try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


from ansible_vault_diff import __version__ as version


config = {
    'description': 'Tool used to display a diff of two ansible-vault encrypted repos',
    'author': 'Brandon Myers',
    'url': 'https://github.com/pwnbus/ansible-vault-diff',
    'download_url': 'https://github.com/pwnbus/ansible-vault-diff/archive/master.zip',
    'author_email': 'pwnbus@mozilla.com',
    'version': version,
    'install_requires': [
        # None yet :)
    ],
    'packages': ['ansible_vault_diff', 'bin'],
    'scripts': [],
    'name': 'ansible_vault_diff'
}

setup(**config)
