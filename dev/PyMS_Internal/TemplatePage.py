class TemplatePage():
	def __init__(self, locationTemplateFile):
		self.content = ""
		
		try:
			file_content = open(locationTemplateFile,"r")
		except IOError:
			print "Error! Template Page: Can't find/read " + locationTemplateFile
		else:
			self.content = file_content.read()
			file_content.close()