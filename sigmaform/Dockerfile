FROM python:3.7

ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

RUN useradd --user-group --create-home --no-log-init --shell /bin/bash app

ENV APP_HOME=/home/app/web

RUN mkdir -p $APP_HOME/staticfiles

WORKDIR $APP_HOME

COPY requirements.txt $APP_HOME
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . $APP_HOME
RUN chmod +x entrypoint.sh
RUN chown -R app:app $APP_HOME

USER app:app

ENTRYPOINT ["/home/app/web/entrypoint.sh"]