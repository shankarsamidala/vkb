FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1 

RUN mkdir /7

WORKDIR /7

COPY . /7/

RUN pip install -r requirements.txt

RUN pip install pillow

EXPOSE 8000