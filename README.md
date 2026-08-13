# Litres.ru — Playwright автотесты
 
Автоматизированные UI-тесты сайта litres.ru на Python + Playwright + pytest.
Реализовано в стиле Page Object Model, с параметризацией данных из JSON и
генерацией отчётов Allure.
 
## Стек
 
- Python 3.14
- Playwright (sync API)
- pytest
- Allure (отчёты)
- Page Object Model
## Структура проекта
 
```
├── pages/                    # Page Object классы
│   ├── base_page.py
│   ├── home_page.py
│   └── search_results_page.py
├── test_data/
│   └── search_data.json      # данные для параметризованных тестов
├── tests/                    # основные тесты (Page Object Model)
│   └── test_search.py
├── sandbox/                  # черновые/учебные тесты без POM
│   ├── test_locators.py
│   ├── test_search.py
│   └── test_titles.py
├── reports/                  # allure-отчёты (генерируются, не хранятся в git)
├── conftest.py                # фикстуры (home, results, screen_on_fail)
└── requirements.txt
```
 
> `sandbox/` — черновые тесты, написанные в процессе изучения Playwright,
> без Page Object Model. Оставлены для истории, актуальные тесты — в `tests/`.
 
## Установка
 
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
playwright install
```
 
## Запуск тестов
 
Все тесты:
```bash
pytest
```
 
Конкретный файл:
```bash
pytest tests/test_search.py
```
 
Конкретный тест:
```bash
pytest tests/test_search.py::test_filters
```
 
## Отчёт Allure
 
```bash
pytest --alluredir=reports/allure_report
allure serve reports/allure_report
```
 
## Особенности реализации
 
- Page Object Model с разделением на локаторы и действия
- Параметризация тестов данными из `search_data.json`
- Автоматический скриншот при падении теста (фикстура `screen_on_fail`)
- Устойчивые локаторы (`data-testid`, `get_by_role`) вместо хрупких CSS/XPath где возможно
