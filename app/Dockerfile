FROM python:3.8

ENV PYTHONIOENCODING utf-8
ENV TZ 'Asia/Tokyo'

WORKDIR /app

RUN mkdir /app/src
RUN mkdir /app/data

RUN pip install --upgrade pip
RUN pip install selenium

RUN apt-get install -y curl
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y apt-utils
RUN pip install --upgrade pip

RUN apt-get install -y locales
RUN locale-gen ja-JP.UTF-8
RUN localedef -f UTF-8 -i ja_JP ja_JP
RUN export LANG=ja_JP.UTF-8
RUN export LANGUAGE=ja_JP:jp
RUN export LC_ALL=ja_JP.UTF-8
