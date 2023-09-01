FROM python:3.9

RUN mkdir -p /opt/services/tbm-music-backend

WORKDIR /opt/services/tbm-music-backend

ADD . /opt/services/tbm-music-backend/

RUN chmod 755 /opt/services/tbm-music-backend/scripts/* && \
        chmod +x /opt/services/tbm-music-backend/scripts/* && \
            export DJANGO_SETTINGS_MODULE=tbm-music.settings && \
                pip install -r requirements.txt 