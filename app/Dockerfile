# pull official base image
#FROM python:3.9.6-slim-buster
FROM python:3.11.2-slim-bullseye

# set environment variables ref:https://www.lifewithpython.com/2021/05/python-docker-env-vars.html
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \    
    PYTHONUTF8=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    # タイムゾーン指定
    TZ=Asia/Tokyo

# create itemsearch directory for the itemsearch user
ENV APP_HOME=/var/www/src
RUN mkdir -p $APP_HOME
    
# set work directory
WORKDIR $APP_HOME

COPY ./requirements.txt .
# Install applications
 
RUN apt update && \
    #apt install -y build-essential net-tools python3-dev python3-pandas libpq-dev && \
    apt install -y build-essential && \
    apt autoremove -y && \
    apt clean && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# copy project
COPY ./src $APP_HOME

EXPOSE 8000
VOLUME ["/var/www/src"]

CMD ["uwsgi", "--ini", "/var/www/src/uwsgi.ini"]
