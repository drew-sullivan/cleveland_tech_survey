# Tech Survey
#
# TODO: Needs "LABEL maintainer" added
FROM alpine:3.6

RUN apk add --update \
    build-base \
    ca-certificates \
    freetype-dev \
    gcc \
    gfortran \
    openblas-dev \
    postgresql-dev \ 
    python \
    python-dev \
    && python -m ensurepip

RUN mkdir -p /opt/app

COPY . /opt/app

RUN cd /opt/app && \
    pip install -r requirements.txt 

WORKDIR /opt/app

EXPOSE 5000

CMD ["python", "manage.py", "runserver", "--host", "0.0.0.0"]

