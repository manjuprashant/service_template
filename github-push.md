# Push to GitHub and set branch protection

1. Create repo
```bash
gh repo create my-org/service-template --private --source=. --remote=origin --push
```

2. Push branch protection (via UI or gh api)
- Require PR reviews
- Require status checks: CI
- Require signed commits (optional)

3. Create initial release using CHANGELOG.md
