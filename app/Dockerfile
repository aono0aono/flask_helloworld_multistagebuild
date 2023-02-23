# ビルド用コンテナ
FROM python:3.11.2-bullseye as builder

WORKDIR /opt/app

COPY requirements.lock /opt/app
RUN pip install -r requirements.lock

# 実行用コンテナ
FROM python:3.11.2-slim-bullseye as runner

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/uwsgi /usr/local/bin/uwsgi

# アプリをインストール
RUN apt update && \
    apt install -y libxml2 && \
    apt autoremove -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# PythonのDocker用環境変数 ref:https://www.lifewithpython.com/2021/05/python-docker-env-vars.html
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \    
    PYTHONUTF8=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    # タイムゾーン指定
    TZ=Asia/Tokyo

# ホームディレクトリ
ENV APP_HOME=/var/www/src
RUN mkdir -p $APP_HOME
    
# ワークディレクトリ
WORKDIR $APP_HOME

# ソースをワークディレクトリにコピー
COPY ./src $APP_HOME

EXPOSE 8000
#VOLUME ["/var/www/src"]

CMD ["uwsgi", "--ini", "/var/www/src/uwsgi.ini"]