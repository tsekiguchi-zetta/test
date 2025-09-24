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
	jvm_path = os.path.join(os.path.dirname(__file__), 'jdk-17.0.2', 'bin', 'server', 'jvm.dll')
	jpype.startJVM(jvm_path, '-Xmx48000m', '-XX:+UseG1GC', '-Djava.locale.providers=COMPAT,CLDR')

	jar_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'zadamexec.jar')
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

def createDM():
	global __km
	dm = kmDM(__km.createDM());
	return dm;

class kmDM:

	_DM = None

	def __init__(self, dm):
		self._DM = dm

	def item(self, item_list):
		for item in item_list:
			self._DM.defineItem(item[0], item[1], item[2])
		return self

	def addCalcItem(self, item_list):
		for item in item_list:
			self._DM.createCalcItem(item[0], item[1])
		return self

	def readCSV(self, name):
		self._DM.readCSV(name, "CSV1S", "SHIFT_JIS")
		return self

	def createSummary(self):
		sm = kmSM(self._DM.toSummary())
		return sm

class kmSM:

	_SM = None

	def __init__(self, sm):
		self._SM = sm

	def item(self, key_list, stat_list):
		for key in key_list:
			self._SM.defineKey(key)
		for stat in stat_list:
			self._SM.defineStat(stat[0], stat[1])
		return self

	def tabulate(self):
		self._SM.tabulate()
		return self

	def toCSV(self, name):
		self._SM.toCSV(name, "CSV1S", "SHIFT_JIS")
		return self
