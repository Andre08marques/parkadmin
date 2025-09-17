FROM python:3.12

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code/media
WORKDIR /code
RUN touch info.log error.log
ADD requirements.txt /code/
RUN pip install --upgrade pip -r requirements.txt 
RUN pip3 install gunicorn
ADD . /code/

