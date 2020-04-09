FROM python:3.8.0

#WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/stonks

RUN adduser stonks && adduser stonks stonks

ENV APP_HOME=/home/stonks

RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles

WORKDIR ${APP_HOME}


COPY ./requirements.txt ${APP_HOME}
COPY ./entrypoint.sh ${APP_HOME}

RUN apt-get update \
    && apt-get install -y netcat
RUN pip install --upgrade pip
RUN pip install -r ${APP_HOME}/requirements.txt

COPY . ${APP_HOME}
RUN chown -R stonks:stonks ${APP_HOME}
RUN chmod +x /home/stonks/entrypoint.sh
USER stonks

ENTRYPOINT ["/home/stonks/entrypoint.sh"]