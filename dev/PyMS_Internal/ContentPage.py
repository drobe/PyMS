import datetime
import zipfile
import os
class ContentPage():
	def __init__(self, locationContentFile, outputPath = ""):
		self.title = locationContentFile.rsplit('/',1)[-1].rsplit('.',1)[0]
		self.url = datetime.datetime.now().strftime("%B-%d-%Y") + "-" + self.title
		self.date = datetime.datetime.now().strftime("%A %B %d, %Y, %I:%M:%S %p")
		self.content = ""
		
		try:
			container = zipfile.ZipFile(locationContentFile)
		except IOError:
			print "Error! ContentPage - Can't find the zip: " + locationContentFile
			return
		except zipfile.BadZipfile:
			print "Error! ContentPage - Bad zip: " + locationContentFile
			return
		else:
			pass
		#if Valid
		path_content = "text.txt"
		file_content = ""
		try:
			file_content = container.open(path_content,"r")
		except KeyError:
			print "Error! ContentPage: Invalid container - " + file + " - can't find/open " + path_content
		else:
			self.content = file_content.read()
	
	def Write(self, outputPath, pageTemplate):
		string_output = pageTemplate.content.replace("<!--INSERT TEXT HERE-->",self.content,1)
		try:
			file_output = open(outputPath + "/index.html", 'w')
		except IOError:
			print "Error! ContentPage - Can't write to file: " + outputPath + "/index.html"
			return
		else:
			file_output.write(string_output)
			file_output.close()
		