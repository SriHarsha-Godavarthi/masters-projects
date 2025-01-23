# Git vs GitHub

Git is a distributed version control system (VCS) that allows you to track changes in your code locally. GitHub, on the other hand, is an online platform where you can store your Git repositories remotely. GitHub provides features for collaboration, such as allowing other developers to review, push, or contribute changes to your project.

The `.git` folder in a repository is the hidden directory responsible for tracking changes, making Git a powerful tool for version control.

---

## Repositories

A Git repository is where all the code and its history for a particular project reside. It acts as a central location for all the changes and versions of the project.

### Example:

```bash
# Initialize a new Git repository
mkdir my-project
cd my-project
git init
```

---

## Branches

Git branches allow developers to work on different features, bugs, or designs independently. When you create a new branch, it is copied from the default branch (often called `main`). Once development on a branch is complete, the changes can be merged back into the main branch.

### Example:

```bash
# Create a new branch
git branch feature-branch

# Switch to the new branch
git switch feature-branch
```

---

## Key Concepts and Commands

### Commit

A **commit** saves your changes locally. These changes are not yet visible on GitHub until you push them to the remote repository.

### Example:

```bash
# Stage changes
git add .

# Commit changes
git commit -m "Add new feature"
```

### Push

The **push** command uploads your locally committed changes to GitHub or another remote repository.

### Example:

```bash
# Push changes to the remote repository
git push origin feature-branch
```

### Pull

The **pull** command fetches and integrates changes made by other developers from the remote repository into your local repository.

### Example:

```bash
# Pull changes from the remote repository
git pull origin main
```

---

## Basic Git Commands

### **git status**

Displays the current status of your working directory and staging area. It shows:

- Files that have been modified.
- Files that are staged for a commit.
- Suggestions for the next steps.

### Example:

```bash
# Check the status of the repository
git status
```

### **git add . / **

Stages changes for a commit. Staging means Git knows about the changes, but they are not yet permanent in the repository.

### Example:

```bash
# Stage all changes
git add .

# Stage a specific file
git add file.txt
```

### **git restore --staged \<folder/filename>**

Removes changes from the staging area without altering the file contents. Useful if you mistakenly stage a file.

### Example:

```bash
# Unstage a file
git restore --staged file.txt
```

### **git commit -m "commit message"**

Saves the staged changes locally with a descriptive message. These changes will only be available in the remote repository after a push.

### Example:

```bash
# Commit staged changes
git commit -m "Fix a bug in login feature"

# Undo the last commit
git revert HEAD
```

### **git push**

Pushes all local commits from your branch to the corresponding remote branch in the repository.

### Example:

```bash
# Push commits to the remote repository
git push origin feature-branch
```

### **git pull**

Fetches changes from the remote repository and integrates them into your local branch.

### Example:

```bash
# Pull changes from the remote repository
git pull origin main
```

### **git checkout **

Switches to a specific commit using its hash value (from `git log`). This puts you in a **detached HEAD** state.

### Example:

```bash
# Checkout a specific commit
git checkout abc1234
```

### **git switch **

Switches between branches.

### Example:

```bash
# Switch to an existing branch
git switch feature-branch
```

### **git merge **

Merges the changes from another branch into the current branch. Always ensure you pull the latest changes from the target branch before merging.

### Example:

```bash
# Merge changes from feature-branch into main
git merge feature-branch
```

### **git branch -m **** **

Renames a branch.

### Example:

```bash
# Rename a branch
git branch -m old-branch new-branch
```

### **git log --oneline**

Shows a concise view of the commit history.

### Example:

```bash
# View the last two commits
git log --oneline --max-count=2

# View commits by a specific author
git log --oneline --author="Your Name"
```

### **git revert \<commit\_sha>**

Creates a new commit that undoes the changes introduced in the specified commit.

### Example:

```bash
# Revert a specific commit
git revert abc1234
```

### **git restore **

Discards changes made to a file and restores it to the state of the last commit.

### Example:

```bash
# Restore a file to its last committed state
git restore file.txt
```

---

## Tagging Versions

Tags are used to label specific commits with human-readable names, often for marking milestones like releases.

### Creating Tags

1. Create a lightweight tag:
   ```bash
   git tag v1.0
   ```
2. Create an annotated tag with a message:
   ```bash
   git tag -a v1.0 -m "Release version 1.0"
   ```
3. Tag a specific commit:
   ```bash
   git tag v0.9 abc1234
   ```

### Viewing Tags

List all tags:

```bash
git tag
```

### Deleting Tags

1. Delete a local tag:
   ```bash
   git tag -d v1.0
   ```
2. Delete a remote tag:
   ```bash
   git push --delete origin v1.0
   ```

---

## Cloning Repositories Securely Using SSH

SSH is a secure way to clone and interact with repositories, as opposed to HTTPS, which requires you to enter your username and password repeatedly.

### Setting Up SSH

1. [Generate an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh):
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
2. Add the SSH key to your GitHub account.
3. Clone the repository using SSH:
   ```bash
   git clone git@github.com:username/repository.git
   ```

---

## Summary of Git Commands

| Command                             | Description                                                 |
| ----------------------------------- | ----------------------------------------------------------- |
| `git status`                        | Shows the status of the working directory and staging area. |
| `git add . / <filename>`            | Stages changes for the next commit.                         |
| `git commit -m "message"`           | Saves staged changes locally.                               |
| `git push`                          | Uploads local commits to the remote repository.             |
| `git pull`                          | Fetches and merges changes from the remote repository.      |
| `git restore --staged <filename>`   | Removes changes from the staging area.                      |
| `git log --oneline`                 | Shows a compact view of the commit history.                 |
| `git tag <tagName>`                 | Creates a tag for the current commit.                       |
| `git branch -m <oldName> <newName>` | Renames a branch.                                           |
| `git merge <branchName>`            | Merges changes from one branch to another.                  |

---

This README provides a comprehensive overview of Git basics, GitHub features, and secure repository cloning. For more advanced topics, check the [gitDocumentation](https://git-scm.com/doc).
