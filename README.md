# DockerBuild-SeleniumServer-WebScraping
Docker+Selenium ServerでWebブラウザ自動操作環境を構築
 
## コンテナ起動
docker-compose.ymlを配置したフォルダに移動して実行
~~~powershell
PS C:\>  docker-compose up -d --build
~~~

## コンテナ接続
~~~powershell
#コンテナID取得
PS C:\>  docker ps 
#コンテナに接続(NAME：python)
PS C:\>  docker exec -it コンテナID bash
~~~

## コンテナでPython実行
~~~console
$ python /app/src/Sample_Scraping.py
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
