# Pull base image
FROM python:3.10-slim-buster as builder

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/code
ENV DEBUG=1

WORKDIR /code

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /code/

RUN poetry install --no-root && \
    poetry export -f requirements.txt --output requirements.txt --without-hashes


FROM builder as development
COPY ./app/ /code/app/
COPY ./tests/ /code/tests/
COPY .env /code/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]