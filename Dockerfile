FROM python


RUN mkdir /app
WORKDIR /app

COPY . /app

ENV PYTHONUNBUFFERED 1

RUN pip install pipenv

RUN pipenv install --system --deploy
