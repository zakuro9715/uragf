FROM python:3.4
MAINTAINER YuZakuro <zakuro@yuzakuro.me>

ENV NODE_VERSION v0.12.4

RUN  curl -SL http://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION-linux-x64.tar.gz \
    | tar xvzC /usr/local --strip-components=1

RUN npm install -g less

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY . /app
ENV DATABASE_URL sqlite:////app/db.sqlite3

ENTRYPOINT ["python", "/app/manage.py"]
