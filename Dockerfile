FROM python:3.11-slim

ENV APP_HOME=/app

COPY . ${APP_HOME}
WORKDIR ${APP_HOME}
RUN mkdir -p $APP_HOME/static
RUN mkdir -p $APP_HOME/media

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt && \
    chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]