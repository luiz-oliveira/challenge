FROM python:3

ARG PUID=1000
ARG PGID=1000
ARG HOME="/customer_service"

RUN addgroup -g ${PGID} customer_service && \ 
    adduser -S -h ${HOME} -G customer_service -u ${PUID} customer_service

USER customer_service

ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src/
RUN pip install -r requirements.txt
ADD . /src/

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000