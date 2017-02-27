# Contribution Guide

Thank you for your interest in contributing to Mobile App Control Center, Systers! There are always bugs to file; bugs to fix in the code; improvements to be made to the documentation; and more.


The instructions given below are for software developers who want to work on [our current code](https://github.com/systers/macc).

## What to work on

1. You can check the [opened issues](https://github.com/systers/macc/issues). They are related to the existing code or for tracking new features.

2. Claim the issue, after approval, work on it and send a pull request.

3. Create a new issue, a community member will get back to you and once approved, send a pull request for the same.

4. Please go through the issue list first (both open as well as closed) amd make sure the issue you are reporting does not replicate the issues already reported. Clearly explain what the exact issue is and provide the steps to recreate it as well, if possible.

5. If you have issues on multiple pages, then report them separately. Do not combine them into a single issue.

6. All the PRs are needed to be sent to the [develop](https://github.com/systers/macc) branch. Do not add merge commits to your PR.

7. If you're sending a PR for UI improvement or fix, make sure you add a screenshot to validate the changes you've made. Give a brief description of the steps taken by you.


## Coding Style and Standards

Follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) and [PEP257](https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings) Style Guides.

Most important things:

 1. Separate top-level function and class definitions with two blank lines.

 2. Keep lines shorter than 100 characters when possible (especially at Python code).

 3. Use whitespace between comma and separate values.

 4. Give classes CamelCase naming.

 5. Give functions lowercase namings.

 6. Refrain from suggesting completely new developments in the issue list. Make you discuss them once in our [slack channel](systers.io/slack-systers-opensource/).



## Git workflow

When you want to start contributing, you should [follow the instructions](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md). After that, follow these steps.

Set your cloned fork to track upstream changes (changes to the main repository), then fetch and merge from the upstream branch:

    `$ git remote add --track upstream https://github.com/systers/macc.git`
    `$ git fetch upstream develop`
    `$ git merge upstream/develop`


Set up a branch for a particular set of changes and switch to it:

    `$ git checkout -b my_branch`

It is important that you create a new branch from the default (develop) branch which is the exact copy of the upstream, else you might mix up commits from different branches. So switch to `develop` branch before creating a new one. 

Run `git remote -v` to check the status, you should see something like this:

    > origin https://github.com/YOUR_USERNAME/macc.git (fetch)

    > origin https://github.com/YOUR_USERNAME/macc.git (push)

    > upstream https://github.com/systers/macc.git (fetch)

    > upstream https://github.com/systers/macc/git (push)

Code!

Commit the changes.

    `$ git add my_changed_files`
    `$ git commit -m "A small but relevant commit message"`


When you're done, figure out how many commits you've made:

    `$ git log`

Push the changes to your forked repository.

    `$ git push origin my_branch`

Issue a pull request on GitHub.

Wait to hear from one of the collaborators.

If you're asked to change your commit message, you can amend the message and commit:

    `$ git commit --amend`
    `$ git push -f origin my_branch`

If you're asked to make changes on your code you can stage them and amend the commit:
    
    `$ git add my_changed_files`
    `$ git commit --amend`
    `$ git push -f origin my_branch`

Avoid doing `$ git add --all` since it also adds the changes needed specifically for your development environment. Manually go through the changes once before you stage them. In case you accidentally stage a file you were not supposed to, you have to unstage all the files again. This can be done by:

    `$ git reset --hard HEAD`

If you need more references and Git expertise, a good resource is the [Git Book](https://git-scm.com/book/en/v2).





