#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

class initDrupal(object):

	def user(self):
		self.user = ""

	def password(self):
		self.password = ""

	def dbAndDirectoryName(self):
		self.dbAndDirectoryName = ""
		
	def fetchArguments(self):
		if len(sys.argv) == 4:
			self.user = sys.argv[1]
			self.password = sys.argv[2]
			self.dbAndDirectoryName = sys.argv[3]
			print sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3]
		else:
			print "un des trois argument obligatoire est manquants"
	def test2(self):
		print self.user + " " + self.password + " " + self.dbAndDirectoryName

	def createDatabase(self):
		os.system("mysqladmin -u root --password=root create "+self.dbAndDirectoryName+";")

	def downloadDrupal(self):
		os.system("mkdir /Applications/MAMP/htdocs/"+self.dbAndDirectoryName)
		os.chdir(r"/Applications/MAMP/htdocs/"+self.dbAndDirectoryName)
		os.system("drush dl")

initD = initDrupal()
initD.fetchArguments()
initD.createDatabase()
initD.downloadDrupal()