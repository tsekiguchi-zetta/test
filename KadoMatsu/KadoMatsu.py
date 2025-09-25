import jpype
import os
import atexit

global __kmClass
global __km

def cleanup():

	global __km
	__km.finalise()

	jpype.shutdownJVM()

	print('>>KadoMatsu::jpype.shutdownJVM')


def init():
	jpype.startJVM(jpype.getDefaultJVMPath(), '-Xmx48000m', '-XX:+UseG1GC', '-Djava.locale.providers=COMPAT,CLDR')

	jar_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'KadoMatsu.jar')
	jpype.addClassPath(jar_path)

	global __kmClass
	__kmClass = jpype.JClass('jp.co.zetta.zadam.zadamexec.ZAdam')

	global __km
	__km = __kmClass();

	atexit.register(cleanup)

	print('>>KadoMatsu::jpype.startJVM')


def setLog(
	version: bool = False,
	command: bool = False,
	information: bool = False,
	error: bool = True,
	warning: bool = False,
	debug: bool = False,
	timer: bool = False
	) -> None:
	global __km
	__km.initialise(version, command, information, error, warning, debug, timer)

def createDataMart(
	*dmargs: str,
	csv: str = None,
	useItem: str = ...,
	csv_type: str = "CSV1S",
	csv_code: str = "SHIFT_JIS"):

	global __km
	dm = __km.createDataMart()
	print(">>KadoMatsu:createDataMart")

#	if useItem:
#		print(">>KadoMatsu:DM:useItem ", useItem)
#		dm.useItem(useItem)

	if dmargs:
		if dmargs[0]:
			csv = dmargs[0]

	print(">>KadoMatsu:DM:readCSV ", csv)
	dm.readCSV(csv, csv_type, csv_code)
	print(">>KadoMatsu:DM:readCSV Finish")

	kmDm = kmDM(dm);
	return kmDm;

class kmDM:

	_DM = None

	def __init__(self, dm):
		self._DM = dm

	def select(self, *args: str):
		print(">>KadoMatsu:DM:select ", args)
		dm = self._DM.select(args)
		print(">>KadoMatsu:DM:select Finish")
		kmDm = kmDM(dm);
		return kmDm;

	def where(self, args: str):
		print(">>KadoMatsu:DM:where ", args)
		dm = self._DM.where(args)
		print(">>KadoMatsu:DM:where Finish")
		kmDm = kmDM(dm);
		return kmDm;

	def groupBy(self, *args: str):
		print(">>KadoMatsu:DM:groupBy ", args)
		dm = self._DM.groupBy(args)
		print(">>KadoMatsu:DM:groupBy Finish")
		kmDm = kmDM(dm);
		return kmDm;

	def toCSV(self, *csv: str, 
			csv_type: str = "CSV1S",
			csv_code: str = "SHIFT_JIS"):
		print(">>KadoMatsu:DM:toCSV ", csv[0])
		self._DM.toCSV(csv[0], csv_type, csv_code)
		print(">>KadoMatsu:DM:toCSV Finish")
