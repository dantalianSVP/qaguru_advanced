FROM python:3.10
WORKDIR /code

# Установка pipenv и зависимостей приложения
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Копирование исходного кода
COPY ./app /code/app

# Запуск приложения с uvicorn
CMD ["fastapi", "run", "app/main.py", "--port", "80"]