# 🎯 Ruff Rules Quick Reference

## How Ruff Configuration Works

```
[tool.ruff.lint]
select = [...]           ← Which rules to ENABLE
ignore = [...]           ← Which rules to SKIP (global)

[tool.ruff.lint.per-file-ignores]
"file.py" = [...]        ← Ignore specific rules in specific files
```

---

## ✅ ENABLE Rules

### **Add these to `select` list in pyproject.toml:**

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
    "RUF",    # ← ADD: Ruff-specific rules
    "SIM",    # ← ADD: Code simplification
    "ARG",    # ← ADD: Unused arguments
    "LOG",    # ← ADD: Logging best practices
]
```

---

## ❌ IGNORE Rules

### **Add these to `ignore` list in pyproject.toml:**

```toml
[tool.ruff.lint]
ignore = [
    "E501",     # line too long
    "ARG001",   # unused positional argument (fixtures use this)
    "SIM105",   # use ternary instead of if-else
]
```

### **Or ignore per-file:**

```toml
[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "F403"]           # unused imports OK
"test_*.py" = ["F401", "F811", "T20"]      # unused, duplicates, print OK
"conftest.py" = ["F811"]                   # duplicate fixtures OK
"migrations/*.py" = ["E501"]                # long lines OK
```

---

## 📋 All Available Rules (Popular Ones)

### **Code Quality**
- `E` - PEP8 errors
- `W` - PEP8 warnings
- `F` - Pyflakes (undefined vars, unused imports)
- `I` - Import sorting (isort)
- `N` - Naming conventions
- `UP` - Upgrade syntax
- `B` - Bug detection
- `A` - Builtin shadowing
- `C4` - Comprehensions

### **New Features to Add**
- `RUF` - Ruff-specific rules
- `SIM` - Code simplification
- `ARG` - Unused arguments
- `LOG` - Logging best practices
- `T20` - Print statement detection
- `COM` - Trailing commas
- `PIE` - Misc improvements
- `D` - Docstring formatting

---

## 🔧 Example: Ignore vs Enable

### **IGNORE Example (skip this rule)**
```toml
[tool.ruff.lint]
select = ["E", "W", "F"]
ignore = ["E501"]  # Ignore line too long

# Result: Checks E and W but NOT E501
```

### **ENABLE Example (add this rule)**
```toml
[tool.ruff.lint]
select = ["E", "W", "F", "SIM"]  # Added SIM

# Result: Checks for simplification suggestions
```

---

## 🚀 3 Common Setups

### **1. Minimal (Production)**
```toml
[tool.ruff.lint]
select = ["E", "F", "W"]
ignore = ["E501"]
```
**Use when:** You want quick, basic checks only

---

### **2. Balanced (Current Project)**
```toml
[tool.ruff.lint]
select = ["E", "W", "F", "I", "N", "UP", "B", "A", "C4"]
ignore = ["E501"]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "F403"]
"test_*.py" = ["F401", "F811"]
```
**Use when:** You want good coverage with reasonable strictness

---

### **3. Strict (Best Practices)**
```toml
[tool.ruff.lint]
select = [
    "E", "W", "F", "I", "N", "UP", "B", "A", "C4",
    "RUF", "SIM", "ARG", "LOG", "T20"
]
ignore = ["E501", "ARG001", "T201"]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "F403"]
"test_*.py" = ["F401", "F811", "ARG001", "T201"]
"conftest.py" = ["F811", "ARG001"]
```
**Use when:** You want maximum code quality

---

## 🎯 For YOUR Flask API Project

**Recommended additions:**

```toml
[tool.ruff.lint]
select = [
    "E", "W", "F", "I", "N", "UP", "B", "A", "C4",
    "SIM",    # Find simplification opportunities
    "LOG",    # Enforce logging over print()
    "ARG",    # Find unused arguments
    "RUF",    # Extra Ruff checks
]
ignore = ["E501", "ARG001"]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "F403"]
"test_*.py" = ["F401", "F811"]
"conftest.py" = ["F811"]
```

---

## 💻 Commands to Use

```bash
# Check violations
ruff check .

# Fix automatically
ruff check . --fix

# See current settings
ruff check . --show-settings

# Check specific file
ruff check app.py

# Show rule details
ruff rule E501
```

---

## ✨ Common Rules by Purpose

### **For Security**
```toml
select = ["B", "SIM", "LOG", "T20", "ARG"]
```
- B (bugbear): Dangerous patterns
- SIM: Simplification (avoids overcomplicated code)
- LOG: Proper logging
- T20: No print() in production
- ARG: Unused args (hiding bugs)

### **For Style**
```toml
select = ["E", "W", "N", "A", "UP"]
```
- E/W: PEP8 compliance
- N: Naming conventions
- A: No builtin shadowing
- UP: Modern Python syntax

### **For Organization**
```toml
select = ["I", "C4", "COM"]
```
- I: Import sorting
- C4: Comprehension improvements
- COM: Trailing commas

---

## 🔍 How to Check Current Settings

```bash
ruff check . --show-settings
```

Output shows:
- Which rules are enabled
- Which rules are ignored
- Per-file overrides
- Max line length

---

## 📝 Summary

| Action | How | Example |
|--------|-----|---------|
| **Enable rule** | Add to `select` | `select = ["E", "W", "F", "SIM"]` |
| **Disable rule** | Add to `ignore` | `ignore = ["E501"]` |
| **Disable per file** | Use `per-file-ignores` | `"test_*.py" = ["F401"]` |
| **Inline suppress** | Use `# noqa` | `import os  # noqa: F401` |
| **See all rules** | `ruff rule` | `ruff rule` |

---

**Next:** Update your pyproject.toml and run `ruff check . --fix`!
