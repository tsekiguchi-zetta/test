import jpype
import os
import atexit

__kmClass = None
__kmIns = None
__kmLogSW = False

def cleanup():
	global __kmIns
	__kmIns.finalise()
	jpype.shutdownJVM()

def init():
	jpype.startJVM(jpype.getDefaultJVMPath(), '-Xmx48000m', '-XX:+UseG1GC', '-Djava.locale.providers=COMPAT,CLDR')
	jar_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'KadoMatsu.jar')
	jpype.addClassPath(jar_path)
	global __kmClass
	__kmClass = jpype.JClass('jp.co.zetta.zadam.zadamexec.ZAdam')
	global __kmIns
	__kmIns = __kmClass();
	global __kmLogSW
	__kmLogSW = False
	atexit.register(cleanup)

def setLog(
	version: bool = False,
	command: bool = False,
	information: bool = False,
	error: bool = True,
	warning: bool = False,
	debug: bool = False,
	timer: bool = False,
	KadoMatsuInfo: bool = False
	) -> None:
	global __kmIns
	__kmIns.initialise(version, command, information, error, warning, debug, timer)
	global __kmLogSW
	__kmLogSW = KadoMatsuInfo

def createDataMart(
	*dmargs: str,
	csv: str = None,
	useItem: str = ...,
	csv_type: str = "CSV1S",
	csv_code: str = "SHIFT_JIS"):
	global __kmIns
	global __kmLogSW
	dm = __kmIns.createDataMart()
	if __kmLogSW:
		print(">>KadoMatsu:createDataMart")
#	if useItem:
#		if __kmLogSW:
#			print(">>KadoMatsu:DM:useItem ", useItem)
#		dm.useItem(useItem)
	if dmargs:
		if dmargs[0]:
			csv = dmargs[0]
	if __kmLogSW:
		print(">>KadoMatsu:DM:readCSV ", csv)
	dm.readCSV(csv, csv_type, csv_code)
	if __kmLogSW:
		print(">>KadoMatsu:DM:readCSV Finish")
	kmDm = kmDM(__kmLogSW, dm)
	return kmDm

class kmDM:
	_kmLogSW = False
	_DM = None
	def __init__(self, kmLogSW, dm):
		self._kmLogSW = kmLogSW
		self._DM = dm

	def select(self, *args: str):
		if self._kmLogSW:
			print(">>KadoMatsu:DM:select ", args)
		dm = self._DM.select(args)
		if self._kmLogSW:
			print(">>KadoMatsu:DM:select Finish")
		return kmDM(self._kmLogSW, dm)

	def where(self, args: str):
		if self._kmLogSW:
			print(">>KadoMatsu:DM:where ", args)
		dm = self._DM.where(args)
		if self._kmLogSW:
			print(">>KadoMatsu:DM:where Finish")
		return kmDM(self._kmLogSW, dm)

	def groupBy(self, *args: str):
		if self._kmLogSW:
			print(">>KadoMatsu:DM:groupBy ", args)
		dm = self._DM.groupBy(args)
		if self._kmLogSW:
			print(">>KadoMatsu:DM:groupBy Finish")
		return kmDM(self._kmLogSW, dm)

	def toCSV(self, *csv: str, 
			csv_type: str = "CSV1S",
			csv_code: str = "SHIFT_JIS"):
		if self._kmLogSW:
			print(">>KadoMatsu:DM:toCSV ", csv[0])
		self._DM.toCSV(csv[0], csv_type, csv_code)
		if self._kmLogSW:
			print(">>KadoMatsu:DM:toCSV Finish")
