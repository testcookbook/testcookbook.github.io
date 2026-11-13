# Contributing to Test Cookbook

Thanks for helping. Every chapter should read the same way, so a reader can jump from one
tool to another and know where to look.

## Chapter template

Each recipe is a Markdown file under `book/<language>/` (or `book/common-automation-concepts/`
for ideas that apply to many tools). Start the file with the Jekyll front matter, then use
these sections in this order:

```markdown
---
layout: default
---
# Title of the chapter

One or two sentences on what the tool or technique is and when you would use it.

## Why
What problem this solves, and how it compares to the nearest alternative. Keep it short.

## Install
The commands needed to install the tool. Show one supported path and say where to find the
others. Use fenced code blocks with a `$` prompt for shell commands.

## Hello world
The smallest runnable example: the test file, the code it exercises, and the command that
runs it. Show the expected output or result.

## Gotchas
A short bulleted list of things that tripped people up: version differences, platform quirks,
common error messages and their fixes.

## Full example
A link to a complete example repository, when one exists. If none exists, leave this section
out rather than linking to an empty repo.
```

Notes:

* `Why`, `Install`, `Hello world` and `Gotchas` are required. `Full example` is optional.
* Keep the chapter runnable. Show the commands and the code, then explain what happened.
* Link to other chapters with site-relative paths, for example
  `[Gherkin](/book/common-automation-concepts/gherkin.html)`.
* Put the chapter in the navigation in `_includes/menu.html`.
* Name the tool version you tested with, if it matters for the examples.

## Local preview

```
$ bundle install
$ bundle exec jekyll serve
```

Then open http://localhost:4000 and check the page renders and the links work.

## Pull requests

* Open an issue first for a new chapter, or reference an existing one.
* Keep each pull request to one chapter or one fix.
* Describe what you changed and how you checked the examples still run.
