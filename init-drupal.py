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
		else:
			print "un des trois argument obligatoire est manquants"
	
	def createDatabase(self):
		os.system("mysqladmin -u root --password=root create "+self.dbAndDirectoryName+";")
		print "==== la base de données "+self.dbAndDirectoryName+" a été crée avec succès"

	def downloadDrupal(self):
		os.system("mkdir /Applications/MAMP/htdocs/"+self.dbAndDirectoryName)
		print "==== le dossier "+self.dbAndDirectoryName+" a été crée avec succès"

		os.chdir(r"/Applications/MAMP/htdocs/"+self.dbAndDirectoryName)
		#download drush in directory
		subprocess.call("drush dl", shell=True)
		print "==== le core drupal a été downloadé avec succès"

		subprocess.call("mv drupal*/* ./", shell=True) #move all file out of default install directory
		subprocess.call("rm -rf drupal*/", shell=True) #remove default install directory
		#install basic site
		subprocess.call("drush site-install -y standard --account-name="+self.user+" --account-pass="+self.password+" --db-url=mysql://"+self.user+":"+self.password+"@localhost/"+self.dbAndDirectoryName, shell=True)
		print "==== le site local drupal a été créé avec succès"
		subprocess.call("open -a /Applications/Google\ Chrome.app 'http://localhost:8888/'"+self.dbAndDirectoryName+"", shell=True) #open site in chrome

initD = initDrupal()
initD.fetchArguments()
initD.createDatabase()
initD.downloadDrupal()