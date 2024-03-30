# lmd-tips
研究や学生生活であると便利なTipsをまとめていきます。

## 目次
- 環境構築
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
conda env create -f environment.yml
```

・環境のアクティベート
```
conda activate lmd-tips
```

・パッケージのインストール
```
pip install -r requirements.txt
```


新しいパッケージなどの追加した際の環境やパッケージの保存方法　in anaconda
```bash
conda env export > environment.yml
env_name=lmd-tips
conda env export --name $env_name > environment.yml
```

### ディレクトリ構成

ディレクトリ構成は以下の通りです。
```
.
├── README.md
├── environment.yml
├── gpu-monitor
├── pdf-utils
│   ├── kouza_info.pdf
│   ├── output_0.jpg
│   └── trans_pdf_jpeg.py
├── private-files
└── requirements.txt
```

・更新方法
```bash
tree
```

