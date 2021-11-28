# Contributing to this repository

Thanks for taking the time to contribute! The following is a set of guidelines for contributing to this project.

## Table of Contents

* [The Essentials](#the-essentials)
  * [Git Client Configuration](#git-client-configuration)
  * [Making Your Changes Clear](#making-your-changes-clear)
* [Creating a Pull Request](#creating-a-pull-request)
* [Branching Strategy](#branching-strategy)

## The Essentials

### Git Client Configuration

Please be sure that Git clinet is properly configured.

- Configure `user.name` and `user.email` as explained in [Customizing Git](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration). In case you need to keep multiple identities configured there is a good site on [Maintaining Different Git Identities](https://xam.io/2017/gitconfig/).
- Sign and verify your commits with GPG to verify commits are from a trusted source.
  - GitHub has good duides that will help like [check for existing GPG keys](https://docs.github.com/en/articles/checking-for-existing-gpg-keys),
  [generate a new GPG key](https://docs.github.com/en/articles/generating-a-new-gpg-key) in case you don't already have one,
  [tell Git about your signing key](https://docs.github.com/en/articles/telling-git-about-your-signing-key) and of course show you how to [sign commits](https://docs.github.com/en/articles/signing-commits).
- Of course, line endings.Check [Configuring Git to handle line endings](https://docs.github.com/en/github/using-git/configuring-git-to-handle-line-endings) for Mac, Windows and Linux.

### Making Your Changes Clear

Be sure you only modify what is related to the purpose of the change and be sure your commits are small and atomic. Following this rules they are easier to read, understand, review, track and revert.

This project uses [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for commit message structure. A well-crafted Git commit message is the best way to communicate context about a change. Here is a good resource on [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/) or just skip to the [guidelines](https://chris.beams.io/posts/git-commit/#seven-rules).

## Creating a Pull Request

There are three important parts in a pull request:
- **Title**. Use a well descriptive but not too long message about what this change is about.
- **Description**. Do your best to put only relevant information. It is perfectly valid to leave it empty! But please, don't leave all your commit messages there.

## Branching Strategy

This is the set of rules that drives the workflow.

### Default branch

**main**. Protected branch, only changes through pull request are accepted. Changes come from a `feat` or `fix` branch. Merge strategy is **always** `--squash`

### Supporting branches

**feature branches**
- One branch per *feature*. May branch off from `main`. Naming convention is `feat/FEAT-NAME`

**bugfix branches**
- One branch per *bugfix*. May branch off from `main`. Naming convention is `fix/FIX-NAME`

**revert branches**
- One branch per *revert*. May branch off from `main`. Naming convention is `revert/REVERT-NAME`