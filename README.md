# Coding_Utilities
## GIT

https://www.atlassian.com/git/tutorials/

#### SSH KEY
```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
git clone git@mygithub.com:<path/to/the/git/repo.git>
eval "$(ssh-agent -s)"
```
#### GPG KEY
```

https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key

https://docs.github.com/en/authentication/managing-commit-signature-verification/adding-a-new-gpg-key-to-your-github-account

gpg --full-generate-key
echo "test" | gpg --clearsign  --user-local D64103B307307189D82FD80591F451305FEB2443
export GPG_TTY=$(tty)
gpg --list-secret-keys --keyid-format LONG

git config --global user.name "USER@EMAIL.com"
git config --global user.email "USER@EMAIL.com"
git config --global user.signingkey D64103B307307189D82FD80591F451305FEB2443
```
#### REV-PARSE
```
git rev-parse --show-toplevel
```
#### Move .git
```
mv .git ./../../... 
```
#### REMOTE
```
NAME
       git-remote - Manage set of tracked repositories

SYNOPSIS
       git remote [-v | --verbose]
       git remote add [-t <branch>] [-m <master>] [-f] [--[no-]tags] [--mirror=(fetch|push)] <name> <URL>
       git remote rename [--[no-]progress] <old> <new>
       git remote remove <name>
       git remote set-head <name> (-a | --auto | -d | --delete | <branch>)
       git remote set-branches [--add] <name> <branch>...
       git remote get-url [--push] [--all] <name>
       git remote set-url [--push] <name> <newurl> [<oldurl>]
       git remote set-url --add [--push] <name> <newurl>
       git remote set-url --delete [--push] <name> <URL>
       git remote [-v | --verbose] show [-n] <name>...
       git remote prune [-n | --dry-run] <name>...
       git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)...]
       
EXAMPLE
       git remote add My_https https://gitlab.moet-hennessy.net/data/dwh-profit-and-loss/dwh-profit-and-loss.git
       git remote -v
       git fetch My_https
```
#### CLONE
https://docs.github.com/en/github/writing-on-github
```
git clone <git@github.com:url.git>
```
#### PULL --ALL
```
git branch -r | grep -v '\->' | sed "s,\x1B\[[0-9;]*[a-zA-Z],,g" | while read remote; do git branch --track "${remote#origin/}" "$remote"; done

or

git fetch --all
git pull --all

or 

for remote in `git branch -r `; do git branch --track $remote; done
```
#### ADD
```
git add .
git add -u 
git add <file>
```
#### COMMIT
```
git  commit -m '[PROJECT-308](feat) <message>'
git commit -a
git commit -am "[PROJECT-308](feat) commit message"
```
##### COMMIT AMEND
```
git commit --amend
```
#### RESTORE
```
git restore <file>
git restore --staged <file>
```
#### STASH
```
git stash
git stash -u
git stash pop
git stash list
git stash pop stash@{2}
git stash show
git stash drop stash@{1}
git stash clear
git log --oneline --graph stash@{0}
```
#### RESET
```
git reflog <branch>
git reset –hard ooooooo
```
#### RESET LAST
```
git reset HEAD~1
git resert --hard HEAD~3
```
#### RESET SOFT
```
git reset --soft HEAD~1
(if the changes are not pushed)
```
#### REVERT
```
git revert <commit-hash>
```
#### BRANCH
```
git checkout -b <new-branch>
git checkout <branch>
```
#### PUSH
```
git push --set-upstream origin <branch>
git push origin
git push --force
```
#### MERGE
```
git reset --merge
```
#### REBASE
```
git config --local pull.rebase true
git config --local pull.ff only
git checkout master && git pull --rebase && git checkout <branch> && git rebase master
```
#### REBASE -i
```
git log --pretty=oneline
git rebase -i  3bc43603fe43665669f29d1ee3415e2ce12c96ba(hash of the commit)

===>

pick b3f7c43 fix japan adjustment
squash d8774df fix japan adjustment
squash 4d3656f add concurrency arg

# Rebase 5a371b0..4d3656f onto 5a371b0 (3 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
#                    commit's log message, unless -C is used, in which case
#                    keep only this commit's message; -c is same as -C but
#                    opens the editor
# x, exec <command> = run command (the rest of the line) using shell
# b, break = stop here (continue rebase later with 'git rebase --continue')
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, reset <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
# .       create a merge commit using the original merge commit's
# .       message (or the oneline, if no original merge commit was
# .       specified); use -c <commit> to reword the commit message
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#

Update the commit message , then click escape,then clieck :wq to leave and save the editor

git status
git add
git commit
git rebase --continue
```
#### REBASE CONTINUE
```
git rebase master
------------>--->--
  git status  
  git add -u
  git commit -m '[PROJECT-911](feat) <MESSAGE_COMMIT>'
  git rebase --continue
--<------<---------
 git push --force
```
#### REBASE INCIDENT
https://www.git-tower.com/blog/make-git-rebase-safe-on-osx/
```
git config --global core.trustctime false
```
#### PULL REQUEST
```
git request-pull v1.0 https://git.ko.xz/project master
```
#### PULL REQUEST DESCRIPTION
```
This PR implements ...

<details open>
<summary><b>How to test</b></summary>
<p>
1. ...
2. ...
3. ...
</p>
</details>
---
Hereafter the commit message:
\`\`\`
[PROJECT-911](feat) <message>
- <message 1>
- <message 2>
- ...
Issue: PROJECT-911
\`\`\`
```
#### CHERRY-PICK
https://git-scm.com/docs/git-cherry-pick
```
git cherry-pick [--edit] [-n] [-m <parent-number>] [-s] [-x] [--ff][-S[<keyid>]] <commit>…​
git cherry-pick (--continue | --skip | --abort | --quit)

    a - b - c - d   Main
         \
           e - f - g Feature

git checkout main
git cherry-pick f

    a - b - c - d - f   Main
         \
           e - f - g Feature
```
#### LOG
```
git log --all --decorate --oneline --graph
git log --graph --oneline --graph --decorate --date-order --full-history @{push}..
git log
git reflog <branch>
```

## Pre-commit
```
Pre-commit will run various checks each time you commit changes to a local branch. Some hooks will try to automatically fix some issues by directly modifying the affected files. If changes were applied to any the file, the commit is cancelled so you can review those changes. You can then stage the changes to take them into account, and run the commit again.
```
### Install pre-commit
```
See official documentation: https://pre-commit.com/#install
```
### Setup git hook scripts
In order to setup git hooks, run the following command once at the root of the repo:
```
pre-commit install
```
### Skip hooks during a commit
To disable all hooks for a commit, add the `--no-verify` flag to your commit command:

```
git commit -m "some changes" --no-verify
```

To only skip specific hooks, use the `SKIP` environment variable:
```
SKIP=sqlfluff-lint,sqlfluff-fix git commit -m "some changes"
```
