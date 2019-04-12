#!/usb/bin/python

__metaclass__ = type # new sytle classes

class Person:
	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def greet(self):
		print "Hello, world! I'm %s" % self.name
