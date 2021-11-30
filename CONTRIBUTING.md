# Contributing to this repository

Thanks for taking the time to contribute! The following is a set of guidelines for contributing to this project.

## Git Client Configuration

Please be sure that Git clinet is properly configured.

- [Customizing Git](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).
- [Maintaining Different Git Identities](https://xam.io/2017/gitconfig/).
- [Check for existing GPG keys](https://docs.github.com/en/articles/checking-for-existing-gpg-keys).
- [Generate a new GPG key](https://docs.github.com/en/articles/generating-a-new-gpg-key).
- [Tell Git about your signing key](https://docs.github.com/en/articles/telling-git-about-your-signing-key).
- [How to sign commits](https://docs.github.com/en/articles/signing-commits).
- [Configuring Git to handle line endings](https://docs.github.com/en/github/using-git/configuring-git-to-handle-line-endings).

## Making Your Changes Clear

- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for commit message structure.
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/).

## Creating a Pull Request

- **Title**. Use a well descriptive but not too long message about what this change is about.
- **Description**. Do your best to put only relevant information. Don't leave all your commit messages there.

## Branching Strategy

This is the set of rules that drives the workflow.

### Default branch

**main**. Changes come from a `feat` or `fix` branch. Merge strategy is **always** `--squash`

### Supporting branches

**feature branches**
- One branch per *feature*. May branch off from `main`. Naming convention is `feat/FEAT-NAME`

**bugfix branches**
- One branch per *bugfix*. May branch off from `main`. Naming convention is `fix/FIX-NAME`

**revert branches**
- One branch per *revert*. May branch off from `main`. Naming convention is `revert/REVERT-NAME`