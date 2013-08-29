import zipfile
import os

class FrontPage():
	def __init__(self, frontPageLocation):
		self.path_frontPage = frontPageLocation
	
	def Write(self, record, template):
		try:
			file_frontPage = open(self.path_frontPage,'w')
		except IOError:
			print "Error! FrontPage: Couldn't open " + self.path_frontPage + " for writing"
			return
		else:
			pass
		
		string_template = template.content
		string_chunks = record.chunks()
		string_chunks.reverse()
		for chunk in string_chunks:
			string_outputChunk = "<a href=<!--URL-->><h1><!--TITLE--></h1></a><small><!--DATE--></small><br><p><!--CONTENT--></p>"
			string_outputChunk = string_outputChunk.replace("<!--TITLE-->",chunk[0])
			string_outputChunk = string_outputChunk.replace("<!--URL-->",chunk[1])
			string_outputChunk = string_outputChunk.replace("<!--DATE-->",chunk[2])
			string_outputChunk = string_outputChunk.replace("<!--CONTENT-->",chunk[3])
			string_template = string_template.replace("<!--INSERT TEXT HERE-->",string_outputChunk,1) # This is potentially dangerous (what if a new replacement string is inserted?)
		file_frontPage.write(string_template)
		file_frontPage.close()