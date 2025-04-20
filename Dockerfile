FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*


RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --only main --no-root --no-interaction --verbose

COPY . /app

# CMD ["python", "main.py"]