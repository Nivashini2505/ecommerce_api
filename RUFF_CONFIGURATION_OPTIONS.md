# 🔧 Ruff Configuration Examples for Your Project

## Your Current Configuration (pyproject.toml)

```toml
[tool.ruff]
line-length = 100
target-version = "py39"

[tool.ruff.lint]
select = [
    "E",    # pycodestyle errors
    "W",    # pycodestyle warnings
    "F",    # Pyflakes
    "I",    # isort
    "N",    # pep8-naming
    "UP",   # pyupgrade
    "B",    # flake8-bugbear
    "A",    # flake8-builtins
    "C4",   # flake8-comprehensions
]
ignore = [
    "E501",  # line too long (handled by formatter)
]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "F403"]
"test_*.py" = ["F401", "F811"]

[tool.ruff.lint.isort]
known-first-party = ["app", "models"]
```

---

## Option 1: Keep Current (Simple)

**Description:** Keep your current configuration as-is  
**Use when:** You're satisfied with current checks

```toml
[tool.ruff]
line-length = 100
target-version = "py39"

[tool.ruff.lint]
select = [
    "E",    # pycodestyle errors
    "W",    # pycodestyle warnings
    "F",    # Pyflakes
    "I",    # isort
    "N",    # pep8-naming
    "UP",   # pyupgrade
    "B",    # flake8-bugbear
    "A",    # flake8-builtins
    "C4",   # flake8-comprehensions
]
ignore = [
    "E501",  # line too long (handled by formatter)
]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "F403"]
"test_*.py" = ["F401", "F811"]

[tool.ruff.lint.isort]
known-first-party = ["app", "models"]
```

**Rules enabled:** 9  
**Strictness level:** ⭐⭐⭐ Medium

---

## Option 2: Add Best Practices Rules (Recommended ✨)

**Description:** Add simplification, logging, and unused argument checks  
**Use when:** You want better code quality suggestions

```toml
[tool.ruff]
line-length = 100
target-version = "py39"

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
    "SIM",    # NEW: Code simplification
    "LOG",    # NEW: Logging best practices
    "ARG",    # NEW: Unused arguments
    "RUF",    # NEW: Ruff-specific checks
]
ignore = [
    "E501",    # line too long (handled by formatter)
    "ARG001",  # unused positional argument (fixtures use this)
]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "F403"]
"test_*.py" = ["F401", "F811", "ARG001"]  # Allow unused args in tests
"conftest.py" = ["F811", "ARG001"]        # Allow duplicate fixtures

[tool.ruff.lint.isort]
known-first-party = ["app", "models"]
```

**What's new:**
- ✅ `SIM` - Detects code that can be simplified
- ✅ `LOG` - Ensures logging is done properly (important for APIs!)
- ✅ `ARG` - Finds unused arguments
- ✅ `RUF` - Extra Ruff-specific checks

**Rules enabled:** 13  
**Strictness level:** ⭐⭐⭐⭐ High

---

## Option 3: Strict Mode (Very Picky)

**Description:** Maximum code quality checks  
**Use when:** You want comprehensive checks

```toml
[tool.ruff]
line-length = 100
target-version = "py39"

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
    "SIM",    # Code simplification
    "LOG",    # Logging best practices
    "ARG",    # Unused arguments
    "RUF",    # Ruff-specific checks
    "T20",    # NEW: Detects print() - use logging instead!
    "COM",    # NEW: Trailing comma enforcement
    "PIE",    # NEW: Misc improvements
]
ignore = [
    "E501",    # line too long
    "ARG001",  # unused positional argument
    "T201",    # Allow print in specific cases
    "SIM105",  # if-else to ternary (sometimes less readable)
]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "F403"]
"test_*.py" = ["F401", "F811", "ARG001", "T201"]  # Allow print in tests
"conftest.py" = ["F811", "ARG001", "T201"]        # Allow in conftest

[tool.ruff.lint.isort]
known-first-party = ["app", "models"]
```

**Rules enabled:** 16  
**Strictness level:** ⭐⭐⭐⭐⭐ Very High

---

## Comparison Table

| Feature | Option 1 | Option 2 | Option 3 |
|---------|----------|----------|----------|
| Current setup | ✅ | — | — |
| Add SIM | — | ✅ | ✅ |
| Add LOG | — | ✅ | ✅ |
| Add ARG | — | ✅ | ✅ |
| Add RUF | — | ✅ | ✅ |
| Add T20 (print detection) | — | — | ✅ |
| Add COM (commas) | — | — | ✅ |
| Add PIE | — | — | ✅ |
| **Rules enabled** | 9 | 13 | 16 |
| **Strictness** | Medium | High | Very High |
| **Recommended for** | Beginners | APIs/Production | Teams |

---

## How Each Option Works

### **Option 1: Keep Current**
- Checks basic code quality
- Good for getting started
- Simple configuration

```bash
ruff check .  # ~few rules violated typically
```

---

### **Option 2: Recommended (Add Best Practices)**
- Checks basic + simplification + logging
- **BEST FOR YOUR FLASK API PROJECT**
- Prevents common mistakes

```bash
ruff check .  # Will catch:
# - Unused arguments in functions
# - Overly complex code
# - print() statements (use logging!)
# - Poor logging practices
```

---

### **Option 3: Strict Mode**
- Checks everything
- Highest code quality
- May be "too picky"

```bash
ruff check .  # Very comprehensive
# Catches everything + trailing commas, etc
```

---

## What Each New Rule Does

### **SIM (Code Simplification)**
Finds code that can be simplified:
```python
# Bad (SIM105)
if condition:
    x = 1
else:
    x = 2

# Good
x = 1 if condition else 2
```

### **LOG (Logging Best Practices)**
Ensures proper logging:
```python
# Bad
print("User logged in")  # Wrong: use logging!

# Good
logger.info("User logged in")
```

### **ARG (Unused Arguments)**
Finds unused function parameters:
```python
# Bad (ARG001)
def process_data(user_id, unused_param):
    return user_id * 2

# Good
def process_data(user_id):
    return user_id * 2
```

### **T20 (Print Detection)**
Detects print() statements:
```python
# Bad
print("Debug info")

# Good
logger.debug("Debug info")
```

---

## 🚀 How to Apply Changes

### **Step 1: Choose Your Option**
Read the options above and pick one

### **Step 2: Update pyproject.toml**
- Open `pyproject.toml`
- Replace `[tool.ruff.lint]` section with your choice
- Save file

### **Step 3: Run Ruff**
```bash
# See what violations are found
ruff check .

# Auto-fix what can be fixed
ruff check . --fix
```

### **Step 4: Review Changes**
```bash
# See detailed output
ruff check . -v
```

### **Step 5: Commit**
```bash
git add pyproject.toml
git commit -m "chore: enhance ruff configuration with SIM, LOG, ARG rules"
```

---

## ⚡ Quick Start

### If you want to upgrade (Recommended):

1. Copy **Option 2** configuration
2. Replace your `[tool.ruff.lint]` section
3. Run: `ruff check . --fix`
4. Review changes
5. Commit

---

## 📊 Expected Changes from Option 1 → Option 2

When you upgrade from Option 1 to Option 2, Ruff will likely find:

- 5-10 code simplification opportunities (SIM)
- 2-5 unused argument warnings (ARG)
- 0-3 logging issues (LOG)
- 0-2 print statement issues

**Most can be auto-fixed!**

```bash
ruff check . --fix  # Fixes most issues automatically
```

---

## 🎯 Recommendation

**For your Flask API project, I recommend Option 2:**

✅ **Why:**
- Better code quality checks
- Catches logging issues (important for APIs!)
- Detects unused arguments
- Not "too strict"
- Good balance

**Steps to apply:**
1. Copy Option 2 configuration
2. Save to `pyproject.toml`
3. Run `ruff check . --fix`
4. Commit with message: "chore: enhance ruff rules with SIM, LOG, ARG"

---

## 📚 See Also

- RUFF_CUSTOMIZATION_GUIDE.md - Full guide
- RUFF_RULES_QUICK_REFERENCE.md - Quick lookup
- [Official Ruff Docs](https://docs.astral.sh/ruff/)

