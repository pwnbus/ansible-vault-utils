# ansible-vault-utils
A suite of tools used to interact with ansible-vault encrypted repositories

## Installation Instructions
Requires git and ansible-vault commands  
```bash
git clone https://github.com/pwnbus/ansible-vault-utils
cd ansible-vault-utils
pip install -e .
```

## Usage

### vault_diff
A tool used to display a 'diff' between two ansible-vault repos

#### Supported Environment Variables
You can use environment variables which will tell the script to not prompt you for certain values
- AVD_REPO_NAME
- AVD_SOURCE_REMOTE_BRANCH
- AVD_DESTINATION_REMOTE_BRANCH

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

### vault_find
A tool used to find strings in files (including ansible-vault encrypted files)

#### Supported Environment Variables
You can use environment variables which will tell the script to not prompt you for certain values
- AVD_REPO_NAME
- AVD_REMOTE_BRANCH
- AVD_SEARCH_STRING

```bash
$ ./bin/vault_find
Enter repo name: somerandomrepo
Enter repository remote:branch: pwnbus:testing_diff_branch
Enter string to search for: somevar

== Results ==

=== files/example.txt ===
somevar = super secret credential

=== files/otherfile.conf ===
someothervar =  {{ somevar }}
```
