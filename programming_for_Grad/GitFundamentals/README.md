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
                  commit those to the github from git.

**git add . / fileName**: this command is responsible for staging changes

**git commit -m "commit message"**: the commited changes are stored locally in your meachine and only     when you push these changes only it will be available in remote repository.

**git push**: This command allows you to push all commits done in that branch to remote branch under same repository.

**git checkout "branchName"**: It allows to change the branch under same repositories.

**git merge "branchName"**: It allows to merge changes from other branches.but be sure to pull the merging branch code before merging to you branch.

**git revert "commit_sha"**: revert is the command which allows you to remove/delete the changes which you have made. 


I think some topics are not covered like staging, cloning repositries securely using SSH

## Clone using SSH:

[SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) is secure way of cloning a repository instead of Https where every time we need to enter username and password manually for every action if we are using local meachine.

In Windows we can use **[gitBash](https://git-scm.com/download/win)** which allows to use git locally.  


