# lmd-tips
研究や学生生活であると便利なTipsをまとめていきます。

## 目次
- [環境構築]
- [ディレクトリ構成](#ディレクトリ構成)
- GPU monitor
- pdf utils

### 環境構築
コードの実行はすべてanaconda 上での使用を想定しています．
環境構築は以下の通りです。
・anaconda の環境の確認（anaconda 環境が既にあることを想定してます．）
```
conda env list
```


・環境の作成
```
conda create -f environment.yml
```

・パッケージのインストール
```
pip install -r requirements.txt
```


新しいパッケージなどの追加した際の環境やパッケージの保存方法　in anaconda
```
conda env export > environment.yml
conda list -e > requirements.txt
```

### ディレクトリ構成

ディレクトリ構成は以下の通りです。
