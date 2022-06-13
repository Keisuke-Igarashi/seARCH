# syntax=docker/dockerfile:1

# pythonイメージを取得
FROM python:3.8-slim-buster

# コンテナの作業ディレクトリ
WORKDIR /majapp

# アプリ資材のコピー
COPY . /majapp/

# poetryを使用可能にするためのビルド時実行コマンド

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install poetry

# poetryの設定ファイルの内容をrequirements.txt化
RUN poetry export -f requirements.txt > requirements.txt

# poetryの設定ファイルの通りのライブラリをインストール
RUN pip install -r requirements.txt

# コンテナの実行
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]