import os
import requests
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('GITHUB_USERNAME')
TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')


def test_create_repo():
    url = f'https://api.github.com/user/repos'
    headers = {'Authorization': f'token {TOKEN}'}
    data = {
        'name': REPO_NAME,
        'description': 'Test repo',
        'public': True
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f'\nРепозиторий {REPO_NAME} создан!')
    else:
        print(f'\nНе удалось создать репозиторий: {response.text}')


def test_check_repo():
    url = f'https://api.github.com/users/{USERNAME}/repos'
    headers = {
        'Authorization': f'token {TOKEN}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            if repo['name'] == REPO_NAME:
                print(f'\nРепозиторий {REPO_NAME} существует!')
                return
        print(f'\nРепозиторий {REPO_NAME} не существует!')
    else:
        print(f'\nОшибка проверки репозитория: {response.text}')


def test_delete_repo():
    url = f'https://api.github.com/repos/{USERNAME}/{REPO_NAME}'
    headers = {
        'Authorization': f'token {TOKEN}'
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f'\nРепозиторий {REPO_NAME} удален!')
    else:
        print(f'\nОшибка удаления репозитория: {response.text}')