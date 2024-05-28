FROM python:3.12-alpine as builder

WORKDIR /app

RUN apk add --no-cache \
    build-base \
    linux-headers

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


FROM python:3.12-alpine

ENV PYTHONPATH=/app

WORKDIR /app

RUN apk add --no-cache libstdc++

COPY --from=builder /install /usr/local

COPY . .

EXPOSE 8080

CMD ["python", "app/main.py"]
