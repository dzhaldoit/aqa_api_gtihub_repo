# GitHub API

## Цель
Создать автоматический тест для проверки работы с GitHub API на языке Python. Тест должен уметь создавать, проверять наличие и удалять репозиторий на GitHub. Необходимо предоставить решение, которое легко воспроизводимо на любом компьютере.

## Создание токена
https://ru.stackoverflow.com/questions/1379428/Как-создать-токен-персонального-доступа-на-github

## Перед запуском тестов производить следующие действия:
````
copy .env-example .env

в созданном .env файле необходимо указать значения USERNAME/TOKEN/REPO_NAME
Пример:

GITHUB_USERNAME="тут имя пользогвателя"
GITHUB_TOKEN="тут токен пользователя"
REPO_NAME="тут имя репозитория"

````

### Установка вертуального окружения:
```
python -m venv venv     - создание виртуального окружения
venv\Scripts\activate   - активация виртуального окружения
```
### Установка зависимостей:
```
pip install -r requirements.txt
```
### Запуск тестов:
```
pytest tests
```
