#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, subprocess

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
		#download drush in directory
		subprocess.call("drush dl", shell=True)
		os.chdir(r"/Applications/MAMP/htdocs/"+self.dbAndDirectoryName+"/drupal-7.15")
		#install basic site
		subprocess.call("drush site-install standard --account-name="+self.user+" --account-pass="+self.password+" --db-url=mysql://"+self.user+":"+self.password+"@localhost/"+self.dbAndDirectoryName, shell=True)

initD = initDrupal()
initD.fetchArguments()
initD.createDatabase()
initD.downloadDrupal()