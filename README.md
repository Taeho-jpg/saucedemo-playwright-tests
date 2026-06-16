# 🧪 SauceDemo Playwright Test Suite

Automated End-to-End (E2E) test suite for [SauceDemo](https://www.saucedemo.com/) built with **Playwright** and **Pytest**, following the **Page Object Model (POM)** pattern.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Playwright](https://img.shields.io/badge/Playwright-1.50-green)
![Pytest](https://img.shields.io/badge/Pytest-8.3-orange)
![CI](https://github.com/Taeho-jpg/saucedemo-playwright-tests/actions/workflows/playwright.yml/badge.svg)

---

## 📋 Test Coverage

| Module | Test Cases |
|--------|-----------|
| Login | ✅ Success, ❌ Wrong password, ❌ Wrong username, ❌ Empty fields, ❌ Locked user |
| Cart | ✅ Add single item, ✅ Add multiple items, ✅ Item count, ✅ Continue shopping |
| Checkout | ✅ Complete order, ❌ Missing first name, ❌ Missing last name, ❌ Missing postal code |

**Total: 14 test cases** covering positive and negative scenarios.

---

## 🏗️ Project Structure

```
saucedemo-playwright-tests/
├── pages/                  # Page Object Model classes
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/                  # Test cases
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
├── reports/                # HTML test reports (auto-generated)
├── .github/workflows/      # CI/CD with GitHub Actions
├── conftest.py             # Pytest fixtures (browser, page)
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Taeho-jpg/saucedemo-playwright-tests.git
cd saucedemo-playwright-tests
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Run tests
```bash
# Run all tests
pytest tests/ -v

# Run with HTML report
pytest tests/ --html=reports/report.html --self-contained-html -v

# Run specific test file
pytest tests/test_login.py -v
```

---

## ⚙️ CI/CD

Tests run automatically on every **push** and **pull request** to `main` via **GitHub Actions**.  
HTML report is uploaded as an artifact after each run.

---

## 🛠️ Tech Stack

- **Python 3.11**
- **Playwright** — Browser automation
- **Pytest** — Test framework
- **pytest-html** — HTML report generation
- **GitHub Actions** — CI/CD pipeline
