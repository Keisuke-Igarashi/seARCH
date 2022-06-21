# ![](/img_for_readme/building.svg)**seARCH**

## **製品概要**
* 製品名
    * seARCH(サーチ)
* 概要
    * 建築家名、住所で著名な建築家の建築をマップ上に表示することが可能なツール

## **動作環境**
Ansibleによって構築した仮想環境上でDockerコンテナを起動することで動作する。
* ホストOS：Windows10
* VMソフトウェア：VMware Workstation    
    * 使用するVM
        * Ansible管理ホスト(Kali linuxのovaをもとに構築)
        * Ansible対象ホスト(CentOS 7のminimal版のisoをもとに構築)

## **使い方**

1. AnsibleでVMに必要なツールをインストール（Ansible管理ホストでの操作）
    
    1. リポジトリのclone

        ```git
        git clone http://172.16.2.11/bootup7/swdev/myarchitecturaljourney_igarashikeisuke.git
        ```

    2. Ansibleによるセットアップコマンドの実行

        ```ansible
        ansible-playbook -i maj_sever_hosts maj_playbook.yml
        ```

2. Docker-composeによるコンテナの起動（Ansible対象ホストでの操作）

    1. リポジトリのclone

        ```git
        git clone http://172.16.2.11/bootup7/swdev/myarchitecturaljourney_igarashikeisuke.git
        ```

    2. Docker-composeの実行

        ```
        sudo docker stop myarchitecturaljourney_igarashikeisuke_web_1
        sudo docker stop mysqldb
        sudo docker rm myarchitecturaljourney_igarashikeisuke_web_1
        sudo docker rm mysqldb
        sudo docker rmi myarchitecturaljourney_igarashikeisuke_web
        sudo docker rmi mysqldb
        sudo docker-compose -f docker-compose.yml up --build
        ```

    3. webサーバーにアクセス（ホストOSでの操作）

        1. ブラウザでURLを入力してアクセス（`http://<Ansible対象ホストのIP>:8000/search`)

## **サイトマップ**
'http://<<Ansible対象ホストのIP>>:8000'までを固定として、それ以下のURLを指定することでアクセス可能なページは以下の通りである。

* '/search'：検索ページ
    * 建築家名、国/都道府県での検索が可能（曖昧検索）
    * 検索結果がある場合、画面上に対象の建築のマーカーが表示される![](/img_for_readme/marker-icon.png)
    * マーカをクリックすることでお気に入り登録が可能
    * マーカーの下に表示される赤い円をクリックすると建物の詳細情報を別タブで確認可能(Google検索)![](/img_for_readme/redround.png)

* '/favorite：お気に入り一覧ページ
    * マップ上で登録したお気に入り一覧を表示可能
    * お気に入りを建築家名・建築名・国/都道府県で検索可能
    * 解除ボタン押下で取り消し可能


* '/register
    * 画面からの建築登録が可能（緯度・経路はマーカー表示に必須）