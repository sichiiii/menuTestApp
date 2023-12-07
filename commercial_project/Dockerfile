FROM python:3.12

WORKDIR /

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install tzdata -y
ENV TZ="Europe/Moscow"

COPY requirements.txt requirements.txt

RUN pip3.12 install -r requirements.txt

COPY . .
WORKDIR /

ENTRYPOINT ["python3.12", "manage.py", "runserver", "0.0.0.0:8000", "--insecure"]