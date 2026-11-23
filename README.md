# GoodDeeds

Сторінка-презентація GoodDeeds (`index.html`), яку віддає невеликий Flask-сервер.

## Запуск
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Відкрийте http://127.0.0.1:5000 — це головна сторінка.

Без Flask можна й так: `python -m http.server 5000` у цій папці.

## Тести
```bash
python -m unittest -v
```

Змінні середовища (необов'язково): `HOST` (127.0.0.1), `PORT` (5000).
