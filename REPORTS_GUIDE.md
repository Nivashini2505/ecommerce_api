# Code Analysis Reports - Download Guide

## 📍 Report Locations

### Local Machine (Direct Access)
Reports are available in your project directory:

```
d:\Unit_testing_eShipz\ecommerce_api\
├── htmlcov/                    # Coverage HTML Report
│   ├── index.html              ✅ OPEN THIS for visual coverage
│   ├── app_py.html             
│   └── models_py.html          
├── ruff_report.json            # Ruff Linting Report (JSON format)
├── bandit_report.json          # Bandit Security Report (JSON format)
└── bandit_report.txt           # Bandit Security Report (Text format)
```

---

## 📊 Coverage Report

**File**: `htmlcov/index.html`

**Summary**:
- Overall Coverage: **78%**
- app.py: 76% (136 statements, 32 missing)
- models.py: 100% (10 statements, 0 missing)

**How to View**:
1. Open in browser: `file:///d:/Unit_testing_eShipz/ecommerce_api/htmlcov/index.html`
2. Click on file names to see line-by-line coverage
3. Red lines = not covered by tests
4. Green lines = covered by tests

---

## 📝 Ruff Linting Report

**File**: `ruff_report.json`

**Status**: ✅ All checks passed! (0 issues remaining after fixes)

**What was Fixed**:
- ✅ Import sorting (app.py, test_api.py)
- ✅ Removed f-string prefixes (3 instances)
- ✅ Renamed parameter `id` → `product_id` (3 instances)
- ✅ Fixed blank lines with whitespace (50 instances)
- ✅ Added trailing newlines (3 files)

**Total Fixes Applied**: 50 errors

---

## 🔒 Bandit Security Report

**Files**: 
- `bandit_report.json` (structured data)
- `bandit_report.txt` (human readable)

**Security Findings**:
- High Severity: 1 issue
  - Flask debug=True (line 280 in app.py)
    - Recommendation: Set debug=False in production
- Low Severity: 33 issues (informational)

---

## 📥 Download from GitHub Actions

To download reports from GitHub Actions workflow:

1. Go to: https://github.com/Nivashini2505/ecommerce_api
2. Click **"Actions"** tab
3. Select the latest successful workflow run
4. Scroll to **"Artifacts"** section
5. Download:
   - `coverage-report-3.9` (or 3.10, 3.11)
   - `ruff-report`
   - `bandit-report`

---

## 📈 Key Metrics

| Tool | Status | Details |
|------|--------|---------|
| **Tests** | ✅ PASS | 19/19 tests passing |
| **Coverage** | ✅ 78% | app.py: 76%, models.py: 100% |
| **Ruff Linting** | ✅ PASS | 0 issues (50 fixed) |
| **Bandit Security** | ⚠️ WARN | 1 HIGH (debug=True), 33 LOW |
| **GitHub Actions** | ✅ PASS | All workflows passing |

---

## 🔧 Recommendations

1. **Security**: Disable Flask debug mode in production
2. **Coverage**: Focus on improving app.py coverage (target 90%+)
3. **Testing**: Add more edge case tests for app.py endpoints

---

Generated: 2026-05-25
Repository: https://github.com/Nivashini2505/ecommerce_api
