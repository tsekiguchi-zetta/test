# KadoMatsu

KadoMatsuパッケージ

## インストール方法

### JAVAのインストール
JAVAをインストールしてください。\
\
KadoMatsuの主要モジュールはJAVA製でJPypeによりPythonからのアクセスを実現しています。\
\
(Windows環境)\
　JAVAインストールした後は、環境変数 PATH / JAVA_HOME の設定を行ってください。\
　環境変数 PATH に C:\jdk-17.0.2\bin などを追加してください。\
　環境変数に JAVA_HOME に C:jdk-17.0.2 などを設定してください。\

### パッケージのインストール
```bash
pip install git+https://github.com/KadoMatsu/KadoMatsu.git
```

## 使い方
```python
import KadoMatsu

KadoMatsu.setLog(version=True, information=True, debug=True)

dm = KadoMatsu.createDataMart(
	'maker.csv',
	useitem=['商品エリアCD', '大分類CD', '販売売上'])

dm.select('商品エリアCD', '大分類CD', '販売売上')\
  .where('商品エリアCD > 50 & 大分類CD < 5')\
  .groupBy('商品エリアCD', '大分類CD')\
  .toCSV('maker.result.csv');

```
