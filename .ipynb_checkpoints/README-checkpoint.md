# Elasticsearch_tutorial

https://qiita.com/ikawaha/items/c654f746cfe76b888a27

今までRDBでデータを格納してたけど、Elasticsearchなるものを使うと検索スピードが爆速いらしい。

『データの加工なども楽になる・・・と思うのですよ』、ほんまか？

## Javaのインストール

https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-20-04-ja

よくわかんないけど、Javaとかもインストールしなきゃいけないらしい

JREとJDKの違いが良くわかってないけど、まあ、ええやろ



まずはおまじない

```
sudo apt update
sudo apt upgrade
```

既にJavaがインストールされているかをチェック

まだなら怒られる

```
java -version

###Output###
Command 'java' not found, but can be installed with:

sudo apt install default-jre              # version 2:1.11-72, or
sudo apt install openjdk-11-jre-headless  # version 11.0.7+10-3ubuntu1
sudo apt install openjdk-13-jre-headless  # version 13.0.3+3-1ubuntu2
sudo apt install openjdk-14-jre-headless  # version 14.0.1+7-1ubuntu1
sudo apt install openjdk-8-jre-headless   # version 8u252-b09-1ubuntu1
```

デフォルトのJava Runtime Environment（JRE）をインストール

```
sudo apt install default-jre
```

こんな感じで表示されたらOK

```
java -version

###Output###
openjdk version "11.0.10" 2021-01-19
OpenJDK Runtime Environment (build 11.0.10+9-Ubuntu-0ubuntu1.20.04)
OpenJDK 64-Bit Server VM (build 11.0.10+9-Ubuntu-0ubuntu1.20.04, mixed mode, sharing)
```

次にJava Development Kit（JDK）をインストール

```
sudo apt install default-jdk
```

```
javac -version

###output###
javac 11.0.10
```



## Elasticsearchのインストール

https://roy29fuku.com/infra/elasticsearch/elasticsearch-python-tutorial/#Elasticsearch

公式ページから落としてきて解答

```
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.12.0-linux-x86_64.tar.gz
tar -zxvf elasticsearch-7.12.0-linux-x86_64.tar.gz
```

解凍フォルダに移動して実行

```
bin/elasticsearch
```

別のコンソールを開いて起動を確認

```
curl http://localhost:9200/
```

