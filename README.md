# Practice Software Testing: Playwright E2E UI Tests

End-to-end UI test suite for [Practice Software Testing](https://practicesoftwaretesting.com), a demo e-commerce shop built for test automation practice. The suite is written in **Python** with **Playwright** and **pytest**, and follows the **Page Object Model (POM)** pattern.

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.14 | Language |
| [uv](https://docs.astral.sh/uv/) | Dependency and environment management |
| [Playwright](https://playwright.dev/python/) (`pytest-playwright`) | Browser automation |
| pytest | Test runner |
| pytest-html | HTML reports |
| pytest-repeat | Re-running tests to check for flakiness |
| Chromium | Target browser |

## Project Structure

```
playwright/
├── pages/                  # Page Objects (locators + actions per page)
│   ├── base_page.py        # Shared navigation helpers
│   ├── home_page.py        # Product listing, search, sort, filter
│   ├── product_page.py     # Product details, add to cart
│   ├── cart_page.py        # Cart line items and totals
│   ├── checkout_page.py    # Sign-in step, billing address, payment
│   ├── login_page.py       # Login and sign out
│   ├── register_page.py    # Registration form
│   └── invoices_page.py    # Account invoices list
├── tests/
│   └── ui/
│       ├── conftest.py     # Fixtures (registered_user, logged_in_page)
│       ├── test_account.py # Order appears in invoices, sign out
│       ├── test_cart.py    # Add to cart, quantity and totals
│       ├── test_checkout.py# Full checkout flow
│       ├── test_login.py   # Valid, invalid and empty credentials
│       ├── test_products.py# Search, sort, category filter, details
│       └── test_register.py# Registration happy path and validation
├── pyproject.toml          # Dependencies and pytest configuration
└── uv.lock
```

## Coverage

| Area | What is tested |
|---|---|
| **Auth** | Login page loads, valid / invalid / empty credentials, registered user login, saved login state, sign out |
| **Registration** | New user, empty required fields, invalid email, weak password, duplicate email |
| **Catalog** | Home page products, search (with and without matches), sort by price (asc / desc), filter by category, product details page |
| **Cart** | Add product, change quantity and verify line price and total |
| **Checkout** | Full order flow with cash on delivery |
| **Account** | Placed order appears in the invoices list |

## Getting Started

### Prerequisites

- Python 3.14
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Git

### Setup

```bash
git clone <your-repo-url>
cd playwright

# Install dependencies into a virtual environment
uv sync

# Download the Chromium browser used by Playwright
uv run playwright install chromium
```

## Running the Tests

```bash
# Whole suite
uv run pytest tests/ui --browser chromium

# Watch the browser
uv run pytest tests/ui --browser chromium --headed

# One file or one test
uv run pytest tests/ui/test_checkout.py --browser chromium
uv run pytest tests/ui/test_login.py::test_login_with_empty_fields --browser chromium

# Smoke tests only
uv run pytest tests/ui --browser chromium -m smoke

# Repeat to check for flakiness
uv run pytest tests/ui/test_account.py --browser chromium --count 5

# Generate an HTML report
uv run pytest tests/ui --browser chromium --html=report.html --self-contained-html
```

### Debugging

```bash
# Record a trace and open it after a failure
uv run pytest tests/ui --browser chromium --tracing retain-on-failure
uv run playwright show-trace test-results/<test-folder>/trace.zip

# Find locators interactively
uv run playwright codegen https://practicesoftwaretesting.com
```

## Design Notes

- **Page Object Model.** Locators and page actions live in `pages/`. Tests contain only the scenario and assertions.
- **Auto-waiting assertions.** Tests use `expect(...)` instead of fixed sleeps, so they adapt to how long the app takes.
- **Shared fixtures.** `registered_user` creates a user once per session. `logged_in_page` gives a test an already authenticated page.
- **Checkout billing form.** The postal code, street and city are auto-filled by the app. Only the house number is typed, and `fill_billing_address` retries if a form refresh clears it.

##