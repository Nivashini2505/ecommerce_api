# 🎨 Ruff Linter Customization Guide

## Overview

Ruff allows you to customize which linting rules to **enable**, **ignore**, and how they behave. This guide shows you how to configure it for your project.

---

## 📍 Configuration File Location

**File:** `pyproject.toml`

```toml
[tool.ruff]                    # Ruff general settings
line-length = 100
target-version = "py39"

[tool.ruff.lint]               # Ruff linting rules
select = [...]                 # Rules to ENABLE
ignore = [...]                 # Rules to DISABLE

[tool.ruff.lint.per-file-ignores]  # Ignore rules in specific files
"test_*.py" = ["F401"]

[tool.ruff.lint.isort]         # isort import ordering
known-first-party = ["app", "models"]
```

---

## 🔧 How to IGNORE Rules

### **Method 1: Ignore Globally (for all files)**

In `pyproject.toml`:

```toml
[tool.ruff.lint]
select = ["E", "W", "F", "I", "N", "UP", "B", "A", "C4"]

# Add rules to ignore here
ignore = [
    "E501",  # line too long
    "W503",  # line break before binary operator
    "N806",  # variable name in function should be lowercase
]
```

**Your current config:**
```toml
[tool.ruff.lint]
ignore = [
    "E501",  # line too long (handled by formatter)
]
```

### **Method 2: Ignore for Specific Files**

In `pyproject.toml`:

```toml
[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "F403"]        # Ignore unused imports
"test_*.py" = ["F401", "F811"]          # Ignore duplicate definitions in tests
"conftest.py" = ["F811"]                # Ignore duplicate fixtures
"migrations/*.py" = ["E501", "F401"]    # Ignore line length in migrations
```

**Your current config:**
```toml
[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "F403"]
"test_*.py" = ["F401", "F811"]
```

### **Method 3: Ignore in Code (Inline)**

Suppress warnings in specific lines:

```python
# Ignore single line
import os  # noqa: F401

# Ignore multiple rules on one line
result = eval(user_input)  # noqa: F821, B307

# Ignore entire function
def legacy_function():  # noqa
    x = 1
    return x + 2

# Ignore entire file
# ruff: noqa
```

---

## ➕ How to ADD/ENABLE New Rules

### **Method 1: Add to `select` List**

In `pyproject.toml`:

```toml
[tool.ruff.lint]
select = [
    "E",      # pycodestyle errors
    "W",      # pycodestyle warnings
    "F",      # Pyflakes
    "I",      # isort imports
    "N",      # pep8-naming
    "UP",     # pyupgrade
    "B",      # flake8-bugbear
    "A",      # flake8-builtins
    "C4",     # flake8-comprehensions
    "RUF",    # NEW: Ruff-specific rules
    "SIM",    # NEW: simplification rules
    "ARG",    # NEW: unused arguments
    "PTH",    # NEW: pathlib usage
]
```

### **Popular Rule Sets to Add**

| Code | Name | What It Checks |
|------|------|----------------|
| `RUF` | Ruff | Extra Ruff-specific rules |
| `SIM` | flake8-simplify | Code simplification opportunities |
| `ARG` | flake8-unused-arguments | Unused function arguments |
| `PTH` | flake8-use-pathlib | Suggests pathlib over os.path |
| `LOG` | flake8-logging | Logging best practices |
| `PIE` | flake8-pie | Misc improvements |
| `D` | pydocstyle | Docstring formatting |
| `T20` | flake8-print | Finds print statements |
| `COM` | flake8-commas | Trailing comma enforcement |

---

## 📋 Example Configurations

### **Minimal (Production)**
```toml
[tool.ruff.lint]
select = ["E", "F", "W"]  # Only critical errors
ignore = ["E501"]          # Ignore line length
```

### **Balanced (Current Project)**
```toml
[tool.ruff.lint]
select = ["E", "W", "F", "I", "N", "UP", "B", "A", "C4"]
ignore = ["E501"]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "F403"]
"test_*.py" = ["F401", "F811"]
```

### **Strict (Best Practices)**
```toml
[tool.ruff.lint]
select = [
    "E", "W", "F", "I", "N", "UP", "B", "A", "C4",
    "SIM", "ARG", "LOG", "RUF"
]
ignore = ["E501", "ARG001"]  # Allow single-arg functions

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "F403"]
"test_*.py" = ["F401", "F811", "ARG001"]
```

---

## 🎯 Common Rule Codes Reference

### **Error Categories**

| Code | Category | Examples |
|------|----------|----------|
| `E` | PEP8 Errors | E201 (extra spaces), E302 (missing blank lines) |
| `W` | PEP8 Warnings | W293 (blank line with spaces), W503 (line break before operator) |
| `F` | Pyflakes | F401 (unused import), F821 (undefined variable) |
| `I` | isort | I001 (unsorted imports) |
| `N` | Naming | N802 (function names should be lowercase), N806 (variables lowercase) |
| `UP` | Upgrade | UP009 (use dict() instead of {}) |
| `B` | Bugbear | B101 (assertion used), B605 (shell injection) |
| `A` | Builtins | A001 (argument shadows builtin), A002 (variable shadows builtin) |
| `C4` | Comprehensions | C400 (set list comp), C403 (import * in function) |

---

## 💡 **RECOMMENDED for Your Project**

Based on your Flask API project, I recommend:

### **Current Configuration (Good)**
```toml
[tool.ruff.lint]
select = ["E", "W", "F", "I", "N", "UP", "B", "A", "C4"]
ignore = ["E501"]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "F403"]
"test_*.py" = ["F401", "F811"]
```

### **Enhanced Configuration (Better)**
```toml
[tool.ruff.lint]
select = [
    "E", "W", "F", "I", "N", "UP", "B", "A", "C4",
    "SIM",    # Code simplification
    "ARG",    # Unused arguments
    "LOG",    # Logging best practices
    "T20",    # Print statement detection
]
ignore = ["E501", "ARG001"]  # Allow single-arg functions

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "F403"]
"test_*.py" = ["F401", "F811", "T20"]  # Allow print in tests
"conftest.py" = ["F811"]

[tool.ruff.lint.isort]
known-first-party = ["app", "models"]
```

**What this adds:**
- ✅ **SIM** - Finds simplification opportunities
- ✅ **ARG** - Identifies unused arguments
- ✅ **LOG** - Ensures proper logging (important for APIs!)
- ✅ **T20** - Catches print() statements (use logging instead!)

---

## 🚀 How to Implement

### **Step 1: Update `pyproject.toml`**

Replace your `[tool.ruff.lint]` section with your chosen configuration.

### **Step 2: Run Ruff**

```bash
# Check for violations with new rules
ruff check .

# Auto-fix what can be fixed
ruff check . --fix

# Show detailed output
ruff check . --show-settings
```

### **Step 3: Handle New Violations**

Ruff will find new issues. You can:

1. **Fix them** (recommended)
   ```bash
   ruff check . --fix
   ```

2. **Ignore them per-file**
   ```toml
   [tool.ruff.lint.per-file-ignores]
   "app.py" = ["SIM105"]
   ```

3. **Ignore them globally**
   ```toml
   [tool.ruff.lint]
   ignore = ["SIM105"]
   ```

4. **Suppress inline**
   ```python
   result = x if y else z  # noqa: SIM108
   ```

---

## 📊 Your Current Rules

| Rule | Enabled | Purpose |
|------|---------|---------|
| E | ✅ | PEP8 errors |
| W | ✅ | PEP8 warnings |
| F | ✅ | Pyflakes (undefined vars, unused imports) |
| I | ✅ | Import sorting |
| N | ✅ | Naming conventions |
| UP | ✅ | Upgrade syntax |
| B | ✅ | Bug detection |
| A | ✅ | Builtin shadowing |
| C4 | ✅ | Comprehensions |

**Currently Ignored:**
- E501 (line too long) - Good! Handled by formatter

---

## 🔗 Resources

- [Ruff Rules Documentation](https://docs.astral.sh/ruff/rules/)
- [Ruff Configuration](https://docs.astral.sh/ruff/configuration/)
- [Full Rule List](https://docs.astral.sh/ruff/rules/)

---

## ✅ Checklisting

- [ ] Read the configuration section above
- [ ] Decide which rules to add/ignore
- [ ] Update `pyproject.toml`
- [ ] Run `ruff check . --fix`
- [ ] Commit changes with message like: "chore: customize ruff linting rules"

---

**Next Step:** Update your `pyproject.toml` with the rules you want to add/ignore!
