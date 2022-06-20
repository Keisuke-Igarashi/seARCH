import requests
import sqlite3
import pytest

from majapp import create_app
from majapp.db import get_db
# from majapp import search
# from flask import (
#     request
# )

# flaskインスタンスの作成
@pytest.fixture
def app():
    app = create_app({'TESTING': True})

    return app


# test実行用clientの作成
@pytest.fixture
def client(app):

    return app.test_client()

# def search(client, architecture_name):
#     return client.post('/search')


def test_search(client):

    # response = client.get('/hello')
    # assert response.data ==  b'Hello, World!'

    response = client.get('/search')
    assert b'seARCH' in response.data

    # response = client.post('/search', data = {'architect_name':''})
    # assert b'Hikari' in response.data

    response = client.post('/search', data = {'architect_name': 'tadao'})
    assert b'Hikari' in response.data
    