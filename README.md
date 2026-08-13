# Playwright Autotests Litres.ru

![CI](https://github.com/yoqattttt/playwright-ui-tests/actions/workflows/ci.yml/badge.svg)

Automated UI tests for litres.ru built with Python + Playwright + pytest.
Implemented using the Page Object Model pattern, with data-driven
parametrization from JSON and Allure report generation.

## Stack

- Python 3.14
- Playwright (sync API)
- Pytest
- Allure (reports)
- Page Object Model

## Project structure

```├── .github/
│ └── workflows/
│ └── ci.yml # GitHub Actions CI
├── pages/ # Page Object classes
│ ├── init.py
│ ├── base_page.py
│ ├── home_page.py
│ └── search_results_page.py
├── test_data/
│ └── search_data.json # data for parametrized tests
├── tests/ # main tests (Page Object Model)
│ ├── init.py
│ └── test_search.py
├── sandbox/ # tests without POM, written while learning Playwright
│ ├── init.py
│ ├── test_locators.py
│ ├── test_search.py
│ └── test_titles.py
├── reports/ # Allure reports (generated, not stored in git)
├── conftest.py # fixtures (home, results, screen_on_fail)
└── requirements.txt
```

> `sandbox/` — tests without the Page Object Model, written while learning
> Playwright. Also run in CI alongside the main tests in `tests/`.

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
playwright install
```

## Running tests

All tests:
```bash
pytest
```

A specific file:
```bash
pytest tests/test_search.py
```

A specific test:
```bash
pytest tests/test_search.py::test_filters
```

## Allure report

```bash
pytest --alluredir=reports/allure_report
allure serve reports/allure_report
```

## Technical details

- Page Object Model with locators and actions separated
- Test parametrization using data from `search_data.json`
- Automatic screenshot on test failure (`screen_on_fail` fixture)
- Resilient locators (`data-testid`, `get_by_role`) preferred over fragile CSS/XPath where possible