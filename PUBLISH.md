# Инструкция по публикации на PyPI

## Перед публикацией

1. **Обновите информацию в файлах:**
   - `setup.py` - замените `Your Name`, email и URL
   - `pyproject.toml` - замените `Your Name`, email и URL
   - `__init__.py` - обновите версию если нужно

2. **Проверьте доступность имени пакета:**
   - Проверьте на https://pypi.org/project/auth-toolkit/
   - Если занято, выберите другое имя и обновите в обоих конфигах

## Шаги публикации

### 1. Установите инструменты

```bash
pip install --upgrade build twine
```

### 2. Соберите пакет

```bash
python -m build
```

Это создаст папку `dist/` с файлами:
- `auth_toolkit-0.1.0.tar.gz`
- `auth_toolkit-0.1.0-py3-none-any.whl`

### 3. Проверьте пакет

```bash
python -m twine check dist/*
```

### 4. Зарегистрируйтесь на PyPI

- Test PyPI: https://test.pypi.org/account/register/
- Production PyPI: https://pypi.org/account/register/

### 5. Создайте API токен

1. Зайдите в аккаунт PyPI
2. Account settings → API tokens
3. Create API token
4. Сохраните токен (показывается один раз!)

### 6. Публикация на Test PyPI (рекомендуется сначала)

```bash
python -m twine upload --repository testpypi dist/*
```

При запросе:
- Username: `__token__`
- Password: ваш API токен (начинается с `pypi-`)

Проверка:
```bash
pip install --index-url https://test.pypi.org/simple/ auth-toolkit
```

### 7. Публикация на Production PyPI

```bash
python -m twine upload dist/*
```

При запросе:
- Username: `__token__`
- Password: ваш API токен для production PyPI

### 8. Проверка

После публикации пакет будет доступен:
- https://pypi.org/project/auth-toolkit/
- Установка: `pip install auth-toolkit`

## Обновление версии

После изменений:

1. Обновите версию в:
   - `setup.py` (version="0.1.1")
   - `pyproject.toml` (version = "0.1.1")
   - `__init__.py` (__version__ = '0.1.1')

2. Соберите и загрузите:
```bash
python -m build
python -m twine upload dist/*
```

## Важно

- ⚠️ Версии нельзя изменить после публикации
- ⚠️ Имя пакета должно быть уникальным
- ⚠️ API токен показывается только один раз - сохраните его!
