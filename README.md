Tron Network Information Service

FastAPI микросервис для получения информации о кошельках в сети Tron.

Описание

Сервис предоставляет API для получения информации о кошельках в сети Tron:
- Bandwidth
- Energy
- Баланс TRX
- История запросов с пагинацией
   
у сервиса 2 эндпоинта:
  1. Для парсинга данных в сети трон и добавления информации в бд.
  2. Для получения информации из бд.

Приложение протестированно с помощью библиотеки pytest.

Требования
- Python 3.7+
- FastAPI
- Uvicorn/Gunicorn
- SQLAlchemy
- TronPy
- Pytest
- PostgreSQL

Для запуска приложения необходимо:
  1. Выполнить команду - git clone https://github.com/Oleg-Spider-Man/tron.git
  2. установить зависимости указанные в файле requirements.txt
  3. добавить в репозиторий проекта файл .env и заполнить его на основе файла .env.example в корне проекта.
  4. Для запуска тестов нужно выполнить команду из корня проекта - python -m pytest
  5. Для запуска приложения нужно выполнить команду из корня проекта - uvicorn my_app.main:app --reload

Для запуска с использованием Docker: Для запуска всех сервисов (PostgreSQL, приложение FastAPI) выполните:

docker-compose up --build

Приложение будет доступно по адресу: http://localhost:8000/docs
