# syntax=docker/dockerfile:1

# pythonイメージを取得
FROM python:3.8-slim-buster

# コンテナの作業ディレクトリ
WORKDIR /maj

# アプリ資材のコピー
COPY . .

# dockerizeのインストール
ENV DOCKERIZE_VERSION v0.6.1
RUN apt-get update && apt-get install -y wget \
 && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# poetryを使用可能にするためのビルド時実行コマンド

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install poetry

# poetryの設定ファイルの内容をrequirements.txt化
RUN poetry export -f requirements.txt > requirements.txt

# poetryの設定ファイルの通りのライブラリをインストール
RUN pip install -r requirements.txt

# 環境変数の設定
ENV FLASK_APP majapp
ENV FLASK_ENV development

# コンテナの実行
CMD ["flask", "run", "--host=0.0.0.0"]