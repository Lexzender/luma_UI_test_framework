# Фреймворк для автоматизации тестирования сайта  ["LUMA"](https://magento.softwaretestingboard.com/) 

<img align="center" src="https://github.com/Lexzender/luma_UI_test_framework/blob/main/luma_UI_test_framework/pictures/pqJTNJvc6e.png" />

---

## Особенности проекта
* Запуск UI автотестов в Selenoid
* Автоматизация отчетности о тестовых прогонах и тест-кейсах в Jira
* Интеграция с Allure TestOps
* Отчеты Allure Report
* Сборка проекта в Jenkins
* Отчеты с видео, скриншотом, логами, исходной моделью разметки страницы
* Оповещения о тестовых прогонах в Telegram
---
## Список проверок, реализованных в проекте
* Авторизация
* Добавление товара в корзину
* Удаление товара из корзины
* Параметризованный  поиск товара
* Сортировка товара по фильтру
* Добавление товара в список желаний
* Проверка ошибки при добавление тоавара не авторизованны пользователем

 ---
## Запуск проекта
Запустить проект можно локально по команде

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -s -v --browser_version=${BROWSER_VERSION}  --base_url=${BASE_URL} --browserName=${BROWSER_NAME}
```
Или в Jenkins
### Запуск проекта в Jenkins

1) Открыть [проект](https://jenkins.autotests.cloud/job/luma_UI_test_framework/)
2) Нажать "Build with Parameters"
3) Заполнить параметры 
4) Нажать "Build"
<img align="center" src="https://github.com/Lexzender/luma_UI_test_framework/blob/main/luma_UI_test_framework/pictures/jenkins.png" />

---

## Allure report
### После прохождения тестов, результаты можно посмотреть в Allure отчете
<img align="center" src="https://github.com/Lexzender/luma_UI_test_framework/blob/main/luma_UI_test_framework/pictures/ALLURE%20REPORT.png" />

### В отчете для каждого теста указана мета информация, а также приложены результаты прохождения: видео, html страницы, скриншот после прохождения, логи браузера.
<img align="center" src="https://github.com/Lexzender/luma_UI_test_framework/blob/main/luma_UI_test_framework/pictures/allure_Behaviors.png" />

### Пример прохождения UI-теста
https://github.com/Lexzender/luma_UI_test_framework/assets/106764385/89c32aa1-7984-41a8-954f-352cd72c3bc9

---
## Нотификация в Telegram
После прохождения тестов результаты будут отправлены в Telegram
<img align="center" src="https://github.com/Lexzender/luma_UI_test_framework/blob/main/luma_UI_test_framework/pictures/Telegram_mF4OU8TK9I.png" />

---
## Интеграция с Allure TestOps
### Тест кейсы
<img align="center" src="https://github.com/Lexzender/luma_UI_test_framework/blob/main/luma_UI_test_framework/pictures/test%20cases.png" />

### Дашборд
<img align="center" src="https://github.com/Lexzender/luma_UI_test_framework/blob/main/luma_UI_test_framework/pictures/dashboards.png" />

### История запусков
<img align="center" src="https://github.com/Lexzender/luma_UI_test_framework/blob/main/luma_UI_test_framework/pictures/Launches.png" />

### Тестовые артефакты
<img align="center" src="https://github.com/Lexzender/luma_UI_test_framework/blob/main/luma_UI_test_framework/pictures/test_results.png" />

---
## Интеграция с Jira
<img align="center" src="https://github.com/Lexzender/luma_UI_test_framework/blob/main/luma_UI_test_framework/pictures/Jira.png" />

