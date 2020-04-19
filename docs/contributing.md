# Contributing

## Simple Git workflow using rebase
Feature development workflow consists of these steps:

```sh
# 1. Pull to update your local master
git checkout master
git pull origin master

# 2. Check out a feature branch
git checkout -b be-feature

# 2. Or switch to it if it already exists
git checkout be-feature

# 3. Do work in your feature branch, committing early and often
git add -p
git commit -m "my changes"

# 4. Rebase frequently to incorporate upstream changes
git fetch origin master
git rebase origin/master

# 5. Interactive rebase (squash) your commits
git rebase -i origin/master

# 6. Merge your changes with master
git checkout master
git merge be-feature

# 7. Push your changes to the upstream
git push origin master

# optional: tag important things, such as releases
git tag 1.0.0

# push single tag
git push origin 1.0.0

# Push all tags
git push origin --tags
```

