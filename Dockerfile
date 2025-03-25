# syntax=docker/dockerfile:1
FROM python:3.8-alpine
WORKDIR /app
RUN apk add --no-cache gcc musl-dev
ENV TZ=Asia/Seoul
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3", "app.py"]