# KadoMatsu (preview)

## 関数

### setLog
コンソールに出力するログのOn/Offを設定
```python
setLog(
	version: bool = False,
	command: bool = False,
	information: bool = False,
	error: bool = True,
	warning: bool = False,
	debug: bool = False,
	timer: bool = False,
	charset: str = "SHIFT_JIS",
	KadoMatsuInfo: bool = False
) -> None
```
例
```python
KadoMatsu.setLog(version=True, information=True, debug=True)
```

### createDataMart
CSVデータをデータマートの読み込み
```python
createDataMart(
  csvfile: str = None,
	usecolumn: str = ...,
	csvtype: str = "CSV1S",
	csvcharset: str = "SHIFT_JIS"
) -> kmDM
```
例
```python
dm = KadoMatsu.createDataMart(
	'maker.csv',
	usecolumn=['商品エリアCD', '大分類CD', '販売売上'])
```

## クラス

### kmDM
データマート クラス

#### select
SQLのselectに準拠
```python
select(*items: str) -> kmDM
```
例
```python
dm.select('商品エリアCD', '大分類CD', '販売売上')
```

#### where
SQLのwhereに準拠
```python
where(condition: str) -> kmDM
```
例
```python
dm.where('商品エリアCD > 50 & 大分類CD < 5')
```

#### groupBy
SQLのgroupByに準拠
```python
groupBy(*items: str) -> kmDM
```
例
```python
dm.groupBy('商品エリアCD', '大分類CD')
```

#### toCSV
CSV形式のファイルに保存
```python
toCSV(
  csvfile: str = None,
	csvtype: str = "CSV1S",
	csvcharset: str = "SHIFT_JIS"
) -> None
```
例
```python
dm.toCSV('maker.result.csv')
```
