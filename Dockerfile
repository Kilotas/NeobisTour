FROM python:3.9

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY ./requirments.txt .

RUN pip install -r requirments.txt

COPY . .

