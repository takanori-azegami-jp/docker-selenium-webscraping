# DockerBuild-SeleniumServer-WebScraping
Docker+Selenium ServerでWebブラウザ自動操作環境を作る
 
## コンテナ起動
~~~powershell
PS C:\>  docker-compose up -d --build
~~~

## コンテナ接続
~~~powershell
#コンテナID取得
PS C:\>  docker ps 
#コンテナに接続
PS C:\>  docker exec -it コンテナID bash
~~~

## コンテナでPython実行
~~~console
$ python /root/opt/HelloWorld.py
~~~


## コンテナとイメージの削除
不要になったコンテナとイメージを削除
~~~powershell
#コンテナ削除
PS C:\> $ docker ps
PS C:\> $ docker rm コンテナID
#イメージを削除
PS C:\> $ docker images
PS C:\> $ docker rmi イメージID
~~~

## 参考
[docker-selenium環境 構築方法 メモ](https://qiita.com/KWS_0901/items/5076a2f4cff544505c5d)
