#official base-image python
FROM python:3.9.6-slim-buster

#working directroy
RUN mkdir /meetup
WORKDIR /meetup

#environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#install system depedencies
RUN apt-get update \
  && apt-get -y install netcat gcc vim incron \
  && apt-get clean && apt install -y make

#install python depedencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /meetup/

CMD ["make", "migrate-run"]