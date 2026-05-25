# GitHub Actions Integration Guide

This project uses GitHub Actions for automated code quality, testing, and security analysis.

## 📋 Workflows

### 1. Tests, Coverage, Lint & Security (`tests-and-analysis.yml`)

**Triggers:**
- On every push to `main` or `develop` branches
- On every pull request to `main` or `develop` branches

**Jobs:**
- **tests-and-coverage**: Runs pytest with coverage on Python 3.9, 3.10, 3.11
  - Generates HTML and JSON coverage reports
  - Uploads to Codecov automatically
  - Creates artifacts for download
  
- **ruff-lint**: Runs ruff linting
  - Generates GitHub-compatible output
  - Creates JSON report artifact
  
- **bandit-security**: Runs security checks
  - Generates text and JSON reports
  - Creates artifacts for download
  
- **comment-pr**: Automatically comments on pull requests
  - Summarizes coverage, linting, and security results
  - Only runs on pull requests

### 2. Scheduled Quality Check (`scheduled-quality-check.yml`)

**Triggers:**
- Runs daily at 2 AM UTC
- Can be triggered manually via `workflow_dispatch`

**Features:**
- Runs all quality checks even if they fail
- Generates comprehensive reports
- Creates downloadable artifacts

## 🚀 Setup Instructions

### 1. Enable GitHub Actions
- Go to your repository settings
- Click "Actions" → "General"
- Ensure "Allow all actions and reusable workflows" is selected

### 2. Codecov Integration (Optional)
For coverage badges and tracking:

```bash
# Go to https://codecov.io and sign in with GitHub
# Select your repository
# Copy the Codecov token (optional, auto-detection usually works)
```

### 3. Add Repository Secrets (Optional)
If using private tools or services:

```
Settings → Secrets and variables → Actions
```

### 4. View Workflow Runs
- Go to "Actions" tab in your repository
- Click on any workflow to see details
- Check artifacts for detailed reports

## 📊 Accessing Reports

### Coverage Report
1. Go to Actions → Recent workflow run
2. Download "coverage-report-3.9" artifact
3. Extract and open `htmlcov/index.html` in browser

### Ruff Report
1. Download "ruff-report" artifact
2. Open `ruff_report.json` to see all linting issues

### Bandit Report
1. Download "bandit-report" artifact
2. Check `bandit_report.txt` for summary
3. Check `bandit_report.json` for details

## 🔍 Customization

### Run on different branches
Edit workflow files and modify:
```yaml
on:
  push:
    branches: [ main, develop, staging ]  # Add more branches
  pull_request:
    branches: [ main, develop, staging ]
```

### Run on schedule
Edit `scheduled-quality-check.yml`:
```yaml
schedule:
  - cron: '0 2 * * *'  # Change time (UTC format)
```

### Change Python versions
Edit `tests-and-analysis.yml`:
```yaml
strategy:
  matrix:
    python-version: ['3.9', '3.10', '3.11', '3.12']  # Add versions
```

### Fail on specific conditions
Add to any job:
```yaml
- name: Fail if coverage below threshold
  run: |
    coverage report --fail-under=80
```

## 📈 Badge Integration

Add to your `README.md`:

```markdown
![Tests](https://github.com/Nivashini2505/ecommerce_api/actions/workflows/tests-and-analysis.yml/badge.svg)
[![codecov](https://codecov.io/gh/Nivashini2505/ecommerce_api/branch/main/graph/badge.svg)](https://codecov.io/gh/Nivashini2505/ecommerce_api)
```

## 🛠️ Troubleshooting

### Workflow not running
- Check branch name matches workflow configuration
- Ensure workflow file is in `.github/workflows/` directory
- Verify YAML syntax (use YAML validator online)

### Tests failing in CI but passing locally
- Check Python version differences
- Ensure all dependencies in `requirements.txt`
- Check for environment-specific code

### Coverage not uploading to Codecov
- Check Codecov token in Settings → Secrets
- Ensure `codecov/codecov-action@v3` is using correct version
- Check Codecov website for repository status

## 📝 Example Workflow Output

```
✅ Tests: 19 passed
📊 Coverage: 67% overall
📝 Ruff: 12 issues found
🔒 Bandit: 1 HIGH, 33 LOW severity issues
```

## 🔐 Security Considerations

1. **Never commit sensitive data** (API keys, passwords)
2. Use GitHub Secrets for sensitive information
3. Review bandit HIGH severity issues before pushing
4. Keep dependencies updated via Dependabot

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Coverage.py Documentation](https://coverage.readthedocs.io/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Bandit Documentation](https://bandit.readthedocs.io/)
