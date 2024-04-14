FROM python:3.12-slim as builder
WORKDIR /bot
RUN pip install --no-cache-dir --upgrade poetry
COPY poetry.lock pyproject.toml ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev

FROM python:3.12-slim
WORKDIR /bot
COPY --from=builder /bot/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
COPY . .

CMD []