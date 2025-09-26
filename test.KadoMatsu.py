import sys
import os
import time
import string

print("###################################################################################################")
print("KadoMatsu : Start")
start = time.time()

import KadoMatsu

KadoMatsu.setLog(KadoMatsuInfo=True)

dm = KadoMatsu.createDataMart(
	csvfile="C:/Users/Administrator/Desktop/Z-AdamPy/maker.csv",
	usecolumn=['商品エリアCD', '大分類CD', '販売売上'])

dm.select('商品エリアCD', '大分類CD', '販売売上')\
  .where('商品エリアCD > 50 & 大分類CD < 5')\
  .groupBy('商品エリアCD', '大分類CD')\
  .toCSV(csvfile="C:/Users/Administrator/Desktop/Z-AdamPy/maker.結果.csv")

t = time.time() - start
print("KadoMatsu : End")
print('>>>Time : ',t,'(sec)')

