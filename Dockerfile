FROM python:3.10
WORKDIR /code

# Установка pipenv и зависимостей приложения
COPY Pipfile /code/Pipfile
RUN pip install --no-cache-dir pipenv
RUN pipenv install --deploy --ignore-pipfile

# Копирование исходного кода
COPY ./app /code/app

# Запуск приложения с uvicorn
CMD ["pipenv", "run", "uvicorn", "app.asgi:app", "--host", "0.0.0.0", "--port", "80"]