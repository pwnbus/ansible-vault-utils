# ansible-vault-diff
A tool used to display a 'diff' between two ansible-vault repos

## Installation Instructions
Requires git, ansible-vault, diff commands  
`pip install -e .`

## Usage
```bash
$ ./bin/vault_diff
Enter repo name: somerandomrepo
Enter source remote:branch: pwnbus:testing_diff_branch
Enter destination remote:branch: originalrepo:master

== Results ==

=== files/configuration.txt ===
40c40
<     'db.password': 'samplepassword1',
---
>     'db.password': 'modifiedpassword1',
45c45
<     #'debug': True,
---
>     'debug': True,


=== files/otherfile.conf ===
3d2
< rand_key=1213124124
```
