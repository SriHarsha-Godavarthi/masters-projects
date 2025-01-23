# Git Vs GitHub
Git is where you do changes in your local meachine. GitHub is online User interface where you store your code remotely which also allows other developer to access and contribute changes (or) allow other developer ,temmates to review ,push there code.Git is called version control system(VCS) because it keep track of all changes done previously. the .git file present in repository which is hidden is responsible for version control

## Repositries
A git repository is the place where all the code related to a particular project will reside.

## Branches
git branches allows different developer's to work individualy on different features,bugs and design and merge all the code to the main (or) default branch.when you create a new branch the code is always copied from default branch of the repository.

## Commit
allows you to save changes locally instead of remote and later update to gitHub.

## Push
push will update your locally commited changes to gitHub from git.

## Pull
It is used when you want to get the changes done by other developer to your local meachine (i.e git).

## Some basic Git commands and description

**git status** : tells if your changes are staged (or) not. After staging changes only you will be able to

I)commit those to the github from git.but these changes are not yet committed to the repository.
II)Another aspect is that the status message hints about what to do next.


**git restore --staged folder/fileName**: To undo the changes shown in the status message/staged that were not committed.no changes to file content just will remove from stagging area 

**git add . / fileName**: this command is responsible for staging changes (i.e. If you want to add these changes to the repository)
.staging  means that Git knows about the change, but it is not permanent in the repository. (: A place to prepare changes for a commit.)

.Separating staging and committing, you get the chance to easily customize what goes into a commit.



**git commit -m "commit message"**: the commited changes are stored locally in your meachine and only  when you push these changes only it will be available in remote repository.(these are the changes staged after the previous commit)

to cancel a commit you have to do a new commit.
**git revert HEAD**: cancels the previous commit made


**git push**: This command allows you to push all commits done in that branch to remote branch under same repository.

**git checkout "7characterhashvaluefoundinlog"**: It allows to change the commit/hash under same branch.

**git switch "branchName"**: allows to switch between branches.

**git merge "branchName"**: It allows to merge changes from other branches.but be sure to pull the merging branch code before merging to you branch.

**git revert "commit_sha"**: revert is the command which allows you to remove/delete the changes which you have made. 

**git branch -m "oldbranchName" "newBranchName"**: will change the exsisting branch name

**git status**: will give you current status of the branch your in(i.e. to check the current state of the repository)

**git log --oneline**  is used to view the commit history in a Git repository. It displays a list of commits along with details such as the commit hash, author, date, and commit message.

You fully control what the log shows.Examples

**git log --oneline --max-count=2
git log --oneline --since="5 minutes ago"
git log --oneline --until="5 minutes ago"
git log --oneline --author="Your Name"
git log --oneline --all**

## Tagging versions

Git tags are a fantastic way to label specific commits with human-readable names, typically used to mark important milestones in a project's history, such as releases or major changes. Tags are essentially immutable references to a specific commit.

Creating a tag for the first version/commit/hash
**git tag <tagName>**
Creating a tag for the previous version/commit/hash
**git checkout <tagName>(^|~N)**
**git tag <previousVersionTagName>**
N- refers to n-th version prior to <tag>
^ - refers to previous version
delete a tag 
git tag -d <tagname>

discarding changes before staging/undo changes made and restore to previous commit
**git restore filename**



I think some topics are not covered like staging, cloning repositries securely using SSH

## Clone using SSH:

[SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) is secure way of cloning a repository instead of Https where every time we need to enter username and password manually for every action if we are using local meachine.

In Windows we can use **[gitBash](https://git-scm.com/download/win)** which allows to use git locally.  


