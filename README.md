# Test Cookbook

Test Cookbook is an open-source book of testing recipes. Each chapter shows how to set up a
testing tool or technique and use it, in a language or framework of your choice.

The site is built with [Jekyll](https://jekyllrb.com/) and published with GitHub Pages at
[testcookbook.com](https://www.testcookbook.com).

## Run the site locally

You need Ruby 3.3 (see `.ruby-version`) and Bundler.

```
$ bundle install
$ bundle exec jekyll serve
```

Then open http://localhost:4000.

Generated output goes to `_site/`. That directory is built by CI and is not committed.

## Contribute

Found a mistake, want to add a recipe, or have an idea for a chapter? Open an issue or send a
pull request.

* Keep chapters short and runnable. Show the commands and the code, then explain what happened.
* Link to a full example repository when one exists.
* Add new chapters to the navigation in `_includes/menu.html`.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the chapter template and pull request notes.
