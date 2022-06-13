# 使用するイメージ(バージョンの指定の方法が不明)
FROM python:3

# アプリ資材のコピー
COPY ./ /majapp/

# コンテナの作業ディレクトリ
WORKDIR /majapp

# MySQLコンテナの起動状況を確認するため
# dockerizeのバイナリを取得

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