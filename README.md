# KadoMatsu

KadoMatsuパッケージ

## インストール方法
```bash
pip install git+https://github.com/KadoMatsu/KadoMatsu.git
```

## 使い方
```python
import KadoMatsu

KadoMatsu.setLog(version=True, information=True, debug=True)

dm = KadoMatsu.createDataMart(
	"maker.csv",
	useItem=['商品エリアCD', '大分類CD', '販売売上'])


dm.select('商品エリアCD', '大分類CD', '販売売上')\
  .where('商品エリアCD > 50 & 大分類CD < 5')\
  .groupBy('商品エリアCD', '大分類CD')\
  .toCSV(maker.result.csv");

```
