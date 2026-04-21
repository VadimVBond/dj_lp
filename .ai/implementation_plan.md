# План деплоя на GitHub Pages

Этот план описывает шаги для превращения динамического Django-сайта в статический и его автоматического деплоя на GitHub Pages.

## User Review Required

> [!IMPORTANT]
> Для работы GitHub Actions потребуется добавить секрет `DJANGO_SECRET_KEY` в настройки репозитория (Settings -> Secrets and variables -> Actions), либо мы можем использовать значение по умолчанию для сборки.

> [!WARNING]
> GitHub Pages не поддерживает серверные редиректы Django. Мы создадим статический `index.html` в корне, который будет перенаправлять пользователей на `/en/`.

## Proposed Changes

### Настройка GitHub Actions

#### [NEW] [deploy.yml](file:///k:/PROJECTS/Django/0%20GitHub/dj_lp/.github/workflows/deploy.yml)
Создание workflow для автоматической сборки и деплоя при пуше в ветку `main`.

### Исправление генерации статики

#### [MODIFY] [urls.py](file:///k:/PROJECTS/Django/0%20GitHub/dj_lp/landing_project/urls.py)
Изменим способ обработки корневого пути для `django-distill`, чтобы создать статический файл редиректа.

#### [MODIFY] [distill.py](file:///k:/PROJECTS/Django/0%20GitHub/dj_lp/core/distill.py)
Уточним функцию генерации URL для корректной работы мультиязычности.

### Подготовка окружения

#### [NEW] [requirements.txt](file:///k:/PROJECTS/Django/0%20GitHub/dj_lp/requirements.txt)
Создание файла зависимостей для GitHub Actions.

## Verification Plan

### Automated Tests
1. Запуск `python manage.py collectstatic --noinput` локально.
2. Запуск `python manage.py distill-local dist --force` локально и проверка содержимого папки `dist`.

### Manual Verification
1. Проверка работы локально сгенерированных HTML-файлов (открытие `dist/en/index.html` в браузере).
2. После пуша — проверка статуса GitHub Actions и доступности сайта по адресу `https://<username>.github.io/<repo>/`.
