# KadoMatsu

KadoMatsuパッケージです。

## インストール方法
```bash
pip install git+https://github.com/KadoMatsu/KadoMatsu.git
```

## 使い方
```python
import KadoMatsu

KadoMatsu.setLog(version=True, information=True)

dm = KadoMatsu.createDM()

dm.item([["年月日",   "n", 1 ],
	 ["商品名",   "a", 11],
	 ["販売売上", "a", 15]])

#dm.addCalcItem([["計算売上","販売売価 * 数量"]])

dm.readCSV("C:/Users/Administrator/Desktop/Z-AdamPy/maker.csv")

sm = dm.createSummary();

sm.item(["年月日", "商品名"], [["合計", "SUM(販売売上)"]])
sm.tabulate().toCSV("C:/Users/Administrator/Desktop/Z-AdamPy/maker.summary.csv")
```
