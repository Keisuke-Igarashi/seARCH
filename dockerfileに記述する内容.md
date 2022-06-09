
(最初にpythonインストールのコマンドを記述)
python -m venv venv
./venv/Script/activate
pip install flask

//kaliだとこっち
```
python --version
sudo apt update
sudo apt search venv
sudo apt install python3.9-venv
```

```
$ source ./venv/bin/activate
```




以下コマンド実行
```bash
$ export FLASK_APP=python
$ export FLASK_ENV=development
$ flask run
```