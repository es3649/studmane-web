# Intro to `bash`

## Contents


# Moving around

**Note:** At any time when typing a directory or filename, use the [tab] key to autocomplete.

***
## `ls`

`ls` **l**i**s**ts the files in the current directory.

**Flags:**

`-l` lists files with metadata. It shows file size, permissions and ownership.<br>
`-A` lists hidden files as well. Files starting with the `.` (period) are hidden, and don't appear with `ls` by default.

**Arguments:**

Arguments are not required, but if provided `ls` lists the files matching the argument. 
Passing a directory path lists the contents of that directory.
Passing a filename just prints the filename, so without `-l`, it's not terribly useful.

***
## `cd`

`cd` **c**hange **d**irectory.

**Arguments:**

An argument is not provided, then by default, it changes to the home directory: `'~'`.
If an argument is provided, then it changes to that directory.
Every folder (besides the root directory, `'/'`) contains a symbolic link called `'..'`, which points to the enclosing folder.
To move up the directory tree (out of folders), use `cd ..`

***
## `mkdir`

`mkdir` creates a new directory (**m**a**k**e **dir**ectory)

**Flags:**

`-p` created all intermediate directories if they don't exist (i.e. creates multiple nested directories)

**Arguments:**

The names of the directories to create

# Files

## `touch`

`touch` creates a completely empty file (if the file does not already exist). If the file already exists, then the access information is updated ('last opened' is set to now)

**Arguments:**

The names of the files to create/update

***
## `rm`

`rm` **r**e**m**oves a file. This action cannot be undone. If `git` is in use, then it may be recoverable using `git`.

**Flags:**

`-r` delete recursively, this flag is required when deleting directories
<br>`-f` force delete. Some files will ask for confirmation to delete, this flag ignores those confirmations and deletes the files anyway.

***
## `mv`

`mv` **m**o**v**es a file or directory

It is also used to rename a file. Give the name of the file to rename as the first argument, and the desired new name as the second.

**Arguments:**

The first argiuments a re the files to move

The last argument is the destinaton for the files to be moved.

***
## `cp`

`cp` **c**o**p**ies a file or directory.

**Flags:**

`-r` recursive. This flag is required to copy directories

**Arguments:**

The first arguments are the names of the files to copy.

The final argument is the destination for the files to copy.

***
## `vim`

`vim` is actually a text editor.

**Arguments:**

The name of the file to open. If the filedoesn't exist, then it is created.

**Usage**

`vim` has the steepest learning curve of any editor because it is so powerful. Here are some basic commands:

* `i` enters editing mode. once in editing mode, everything works as you might assume it should.
* `[esc]` exits the current mode.
* `:q` closes the file. It fails if there are unsaved changes
* `:q!` force closes the file
* `:w` saves
* `:x` saves and exits. It is equivalent to `:wq`
* `:e` loads changes from the disk (if the file has been changed by another user/program)

***
## `nano`

`nano` is another text editor, easier to use than vim.

It's pretty straightforward to use. In some versions, crtl+s can be used to save, and in all versions, ctrl+x will exit (with the option to save ic ctrl-x isn't doing it).

**Arguments:**

the name of the files to open. It will be created if it doesn't exist

***
## `chmod`

`chmod` **ch**ange **mod**e changed the permission mode on a file. Permissions on a file are visible using `ls -l` (or just `ll`), and appear like this

```
-rwxr-xr-x
```

The first character appears as a `'d'` if the file is a **d**irectory
It then contains three sets of three values.

Within each group, the first value appears as an `'r'` if the file has permission to be **r**ead. The second appears as a `'w'` if the file is **w**ritable, and the third appears as an `'x'` if the file has permissions to be e**x**ecuted.

Each group refers to a different collection of users. The first group refers to the permissions granted to the owner, the second set refers to permissions granted to members of the same group, and the third represents permissions granted globally.

**Arguments:**

The first argument is a file mode or modifier. The modifiers are given in the table below. Thes modifiers grant/revoke permissions for all users

||Adds|Removes|
|---|---|---|
|Read|+r|-r|
|Write|+w|-w|
|Execute|+x|-x|

The mode is a combination of three valued as described above: owner, group, and global permissions. Each is a 3 bit integer. Add 4 to make it readable, add 2 to make it writeable, add 1 to make it executable.

Examples:
```
   ls -l    mode
-rw-r--r--  644
-rwxr-xr-x  755
drwxrwxrwx  777
-rwxrw-r--  764
-r--------  400
```

The second (third, fourth, etc) argument(s) name the files whose permissions you want to change.

***
# Tools

## `screen`

`screen` is a terminal multiplexer. It allows you to create terminal sessions, then detach them from the display and continue running in the background. It is expecially useful for remote work that is expected to take a long time, expecially if you will need to log out in the middle of the session.

**Flags:**

`r` reattaches to a previous session. If there is more than one session to attach to, it will fail and print a list of possible session IDs. In this case, you must pass the listed ID of the session to attach to as an argument to `-r`

**Arguments:**

**Usage:**

## `grep`

`grep` is a regular expression search tool

**Flags:**

`-E` use extended regular expression syntax
<br>`-o` print only the matching parts of the line, not the whole line
<br>`-c` show number of lines matches, instead of the lines themselves
<br>`-C <num>` print `<num>` lines of context before and after the match
<br>`-v` show non-matches, instead of matches
<br>`-i` ignore case

**Arguments:**

The first argument is the string or regular expression to match.
The rest are the file or files to search.

**Note:** Regular expression syntax is extensive and described [here](https://docs.python.org/2.4/lib/re-syntax.html)

***
## `man`

`man` prints the **man**ual pages for a command

**Arguments:**

The name of a command or tool. It prints detailed usage information for that command if such information is available.

***
# Environment

***
# Variables

Variables can be set in the environment, and accessed later. To set a variable, sue the equals sign with NO spaces. The style is that environment variables are capitalized.

```
MY_VARIABLE="some value"

MY_OTHER_VAR=$(ls)
```

The first, stores the string `some value` in the variable. The second stores the output of the command `ls` in the variable.

To access a variable, use `'$'`. Varibles are concatenated by default.

***
# Loops


## TODO
* wildcards
* $PATH
* {}
* '>' and '>>'
* '|'
