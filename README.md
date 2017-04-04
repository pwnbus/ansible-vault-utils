# ansible-vault-diff
A tool used to display a 'diff' between two ansible-vault repos

## Installation Instructions
Requires git and ansible-vault commands  
`git clone https://github.com/pwnbus/ansible-vault-diff`  
`cd ansible-vault-diff`  
`pip install -e .`

## Usage
```bash
$ ./bin/vault_diff
Enter repo name: somerandomrepo
Enter source remote:branch: pwnbus:testing_diff_branch
Enter destination remote:branch: originalrepo:master

== Results ==

=== files/configuration.txt ===
diff --git a/files/configuration.txt b/files/configuration.txt
index 6621dfd..ac7d3d3 100644
--- a/files/configuration.txt
+++ b/files/configuration.txt
@@ -1,5 +1,6 @@
 {
   'db_host': 'localhost',
   'db_user': 'secretusername',
-  'db_password': 'secretpassword',
+  'db_password': 'changemypassword',
+  'db_name': 'somedb',
 }


=== files/otherfile.conf ===
diff --git a/files/otherfile.conf b/files/otherfile.conf
index e785b8e..43dbf7b 100644
--- a/files/otherfile.conf
+++ b/files/otherfile.conf
@@ -1,3 +1,4 @@
 {
   'debug': True,
+  'additonalkey': '1234',
 }
```
