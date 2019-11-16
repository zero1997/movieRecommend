#!/usr/bin/python
# -*- coding: utf-8 -*-
class mysqlDB:
	ip = "39.100.226.136"
	user = "root"
	pwd = ""
	db = "recommendation"
	
	def __init__(self,eip="39.100.226.136",usr="root",pwd="",db="recommendation"):
		self.ip = eip
		self.user = usr
		self.pwd = pwd
		self.db = db