# `git` Workflow - a Basic Toolkit

## Contents
Highlights are bolded
* [Cloning a repository](#cloning)
* **[Commit](#commit)**
  * **[Status](#status)**
  * [Stash](#stash)
  * [Log](#log)
  * **[Tracking (add, remove)](#tracking)**
* [Accesing Remote](#accessing-remote)
  * **[Push](#push)**
  * **[Pull](#pull)**
  * [Remote](#remote)
* [Branches](#branches)
  * [Creating branches](#creating-branches)
  * [Moving between branches](#moving-between-branches)
  * [Merging branches](#merging-branches)
  * [Rebase](#rebasing)
  * [Deleting branches](#deleting-branches)
* [Reverting](#reverting)

# Cloning

To "clone" a repository is to copy all the files to your local workspace.
It also copies the associated `git` workspace.

To clone a repository, run `git clone [repo-url]`

The `repo-url` can be found at the repository's home page.
Click the green button in the upper right of the home page which says "Clone or Download."
It will generate a little pop-up box with the `repo-url`

When you clone a repository via command line, it will create a new folder with the files and the git workspace inside.

# Commit

Committing is pretty simple, it 'saves' your changes. Just run: `git commit -am [COMMIT_MESSAGE]`

The `[COMMIT MESSAGE]` should include a short but specific summary of the changes which are being saved.

If needed, you can run `git commit --amend -am [COMMIT_MESSAGE]` to change or update the commit message of the last commit. Also, omitting the `m` in `-am` will cause git to open an editor in which you can give a longer explanation of the changes. 

## Status

Displays what files have been changed since the last commit.

It also shows a list of untracked files. These files will NOT be saved in the commit, and will not be modified or even monitored by `git`.

Manage these with the commands in the [Tracking](#tracking) section.

## Stash

Occasionally you may try to perform an operation but you will be unable to, or you might risk losing changes. You could commit those changes, or you could stash them with `git stash`. The changes will be stashed away in a secret place, and the branch will revert to the previous commit.

Those stashed changes can be reapplied using `git stash apply` once you are ready to put them back, and they can even be applied to other branches, though with risk of conflict.

## Log

Opens a commit history similar to the following:

```
01 commit 9e34fe47b705b1ae10f372343aba0dd70005730b (HEAD -> es3649/NHC)
02 Author: es3649 <es3649@gmail.com>
03 Date:   Fri Feb 8 14:21:11 2019 -0700
04 
05     added documentation for train_test_split.py
06 
07 commit 334acbd0ed88de8eaf8faf067e8a4297425d603e (origin/es3649/NHC)
08 Merge: 6b80fbd f0ea129
09 Author: es3649 <es3649@gmail.com>
10 Date:   Thu Jan 31 09:59:29 2019 -0700
11 
12     Merge branch 'master' of https://github.com/es3649/NHC into es3649/NHC
13
14 commit 6b80fbd3df05646796448777004c615df99b57f9
15 Author: es3649 <es3649@gmail.com>
16 Date:   Tue Jan 29 18:07:16 2019 -0700
17 
18     added the time separated data
19 
20 commit f0ea129ee8fd3db7d251c3543211a8b7ff6d562e (origin/master, origin/HEAD, master)
21 Merge: 4e6d7f5 524efbe
22 Author: es3649 <es3649@gmail.com>
23 Date:   Mon Jan 28 14:35:22 2019 -0700
24
25     Merge branch 'es3649/fix-the-tree-logs'
```

So, these line numbers don't actually appear, I just put theme there for easier reference. This log you see may be longer or shorter. This one shows the last 4 commits.

On lines 1, 7, 14, 20 we have commit hashes. These big long strings are unique identifiers for commits.

On 1, 7, 20 at the end of the line (in parentheses) we have branch names. `origin/master` is currently behind the by current branch `es3649/NHC`. But the remote version of my `NHC` branch is behind the remote version, `origin/es3649/NHC`.

On lines 5, 12, 18, 25 I have commit messages for the commits which have been made.


## Tracking

`git` tracks changes in files for you, but it doesn't follow everything by default. You have to tell it what it should/can pay attention to. This is done with the [`add`](#add) and [`rm`](#remove) commands. 

`git add [FILENAME]` tells git to begin tracking the file at `[FILENAME]`.

`git rm [FILENAME]` tells git to delete the file at `[FILENAME]` and to stop tracking it. Wait, delete it, like from the computer? Yep! it will be GONE! to get it back 
(if you've already committed the file once) you can run `git checkout HEAD [FILENAME]` to bring him back. By default, git won't let you delete files which have been changed or added since the last commit. Add the `-f` flag to delete them anyway.

`git rm --cache [FILENAME]` is what you probably wanted. it WILL NOT delete the file at `[FILENAME]`, but will just stop tracking it.

`git diff` shows the changed which have been made since the last commit.

### .gitignore

Now, maybe you have some files that you want around, but you don't want git to see them (files with secret access keys, compiled binaries, or giant data files), but you *also* don't want those obnoxious "untracked file" dialogs whenever you commit and check the status. 

Git has a secret file called `.gitignore` which just sits at the root of your git repository and tells git what to ignore. Git will never complain about untracked files which are listed in your .gitignore. It will also not save or track changes in them.



# Accessing Remote

One of the beauties of git is that it stores all your changes in the great, unknowable and ever-persistent cloud. You will, however, need to access these branches and update them so that everyone can see what you've been working on.

## Push

`git push origin [BRANCHNAME]` will upload new commits on that branch to the cloud.

## Pull 

`git pull origin [BRANCHNAME]` will download new commits from the specified branch into the *current* branch. 

## Remote

`git remote` offers several subcommands to allow you to change remote settings.

`git remote show origin` &mdash; Shows where remote changes are pushed to/pulled from

`git remote add origin [URL]` &mdash; If no remote already exists, then git will begin to push and pull chaged to/from `[URL]`.

`git remote remove origin` &mdash; Deletes removes the remote (removes locally, remote will still exist at its remote location), the local repository will stop following the remote, and can be set to follow another remote with `add`



# Branches

A branch represents an alternate worksite.
The master branch contains the main project and should be updated only occasionally, or as new developments are made.
Each user makes changes to a repository by working on their own branch, and when the changes are ready to be published, these personal branches are merged into master.

## Creating Branches

To create a new branch, you will run:

`git checkout -b [username]/[branchName]`

Where `[username]` is your github.com username and `[branchName]` describes the purpose of the branch.

This specific format is not strictly required, but it's good practice for the branch name to be prefaced by `[username]/`.
This just allows collaborators to know that it is your branch.

Now, this branch only exists locally. To uopload it to the cloud, run:

`git push origin [nameOfBranchToUpload]`

You can also pull changes from remote (the cloud) into your local branches.
Do this by running `git pull origin [branchName]` from within the branch to update, where `[branchName]` is the name of the branch from which you want to bring in changes. This may cause merge conflicts.

## Moving Between Branches

Multiple branches can be maintained on your local device at the same time.
To view the current branches on your computer, run:

`git branch`

This will display all local branches. The one you are on will have a * next to it, and will likely be highlighted green.

`git branch -a` will list *all* branches, including remote (only in the cloud)
branches. 
Most of these don't matter, but sometimes deleted branches will hang around remotely after being deleted (see [Deleting branches](#deleting-branches)).

To switch from one branch to another, use: 

`git checkout [branchName]` (*without* the `-b` we used earlier)

This will switch onto the branch called `[branchName]`.

## Merging Branches

This can be done from command line, but is often easier to manage using the interface at github.com.

Before merging your branch into master, run `git pull origin master` locally and within the branch you want to merge.
This may cause merge conflicts, but this is the best time and place to deal with them.
You will then use `git push origin [branch]` to upload the local version to remote (the cloud).

Now, go to the repository's location at github.com. If you just pushed, there will likely be a notification at the top of the page saying that your branch was just changed, giving you the option to open a pull request.

If this message doesn't appear, then on the top tab bar (under the name of the repository) you will find a "Pull requests" tab (probably the 3rd tab). From there click the green "New Pull Request" button on the top right. The top bar will ask you which branches to merge. "Base" (the first drop down box) should probably be master, or the branch which is receiving the new changes. "Compare" (the second drop down box) is the branch which contains the new changes which will be copied over to Base. Once you have selected the branches, click the "Create Pull Request" button.

Add a message detailing the new changes you have made, then click "Create Pull Request." 
The pull request (PR) is now opened. At the top of the left column, there will be a box labelled "Reviewers."
Click the gear at the top right of the box to select some reviewers. These reviewers can look over the changes, make comments, approve them, or request changes to them. Some repositories may require other users to approve changes before merging a PR is allowed.

Last, the user who started the PR, merges and confirms the pull request. The user who submitted the PR should deal with any associated merge conflicts.

If desired, the branch can be deleted after the merge has been completed.

## Rebasing

This is another way to update your branch to the current state of another branch without creating a merge commit.

Run `git rebase [BRANCH]`.

All commits on `[BRANCH]` will be added to the current branch if there is no interference with current commits. 

## Resolving Merge Conflicts

If two branches have conflicting changes and you try to merge or rebase, get lets you deal with that. It does this by messing with your files like so:

```
This is a code file.
<<<<<<< HEAD
It has a nasty problem
=======
It has a merge conflict
>>>>>>> incoming-branch-name
```

The HEAD, or current branch will be first with the code which was added there. After the equals signs, the incoming change will be displayed. This is the change which was made in the other branch which is being merged in/rebased.

To resolve the conflict, remove the code which you *don't want* to be in the resulting file. Then delete the the lines with angle brackets (>>, <<) and the equal signs.
Once all is done, use `git add [PROBLEM_FILE]`

To resolve conflicting files (a file was added in one branch and removed in another), just do `git add [PROBLEM_FILE]` if you want to keep it, and remove it if you want it removed.

At any time during a merge, use [`git status`](#status) to see where the problems are.

Use `git rebase --abort` or `git merge -- abort` to quit the rebase/merge respectively.

Use `git rebase --continue` or `git merge --continue` once all changes have been resolved to finish up the rebase/merge. Then commit and push your changes.

## Deleting Branches

Branches can be deleted after a pull request (PR) is merged on the github.com website, but there is a difference between deleting a branch locally and remotely.

Branches can be deleted locally using the following command:

`git branch -D [branchName]`

To delete a branch remotely, use one of the following:

1. `git push origin --delete`
1. `git push origin --delete [branchName]`

Use (1.) from within the local version of the branch you want to delete if it still exists locally.
If it doesn't, you can use (2.) from within a different branch substituting `[branchName]` with the name of the branch you want to delete.

Occasionally, branches which have been remotely deleted will still appear as remote branches when using `git branch -a`. When this happens, use 

`git remote prune origin`

to make them go away.

# Reverting

Before reverting, it is important to understand [`git log`](#log).

**Warning:** Turns out that undos can't be undone.

`git reset --hard [COMMIT_ID]` resets the working directory to the state at `[COMMIT_ID]`. All current changed are discarded along with all changes since `[COMMIT_ID]`. The `[COMMIT_ID]` can be taken from the output of `git log`. Use `HEAD` as the commit id to remove all changes since the last commit.

You can also reset a particular file or set of files to a particular commit with `git reset [COMMIT_ID] -- <filenames>`.