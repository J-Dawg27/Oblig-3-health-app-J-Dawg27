FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

RUN mkdir -p /app/data

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "src.health_app.api:app", "--host", "0.0.0.0", "--port", "8000"]
