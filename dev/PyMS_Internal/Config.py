class Config():
	def __init__(self, locationConfigFile):
		self.path_config = locationConfigFile
		self.dict_valueStore = dict()
		
		try:
			file_config = open(self.path_config, "r")
		except IOError:
			print "Error! Config: Could open " + self.path_config
		else:
			self.dict_valueStore.clear()
			for line in file_config:
				line = line.split(':',1)
				if (len(line) == 2):
					self.dict_valueStore[line[0]] = line[1].strip('\n')
			file_config.close()
		
	def SaveConfig(self):
		try:
			file_config = open(self.path_config, "w")
		except IOError:
			print "Error: SaveConfig() in class Config"
		else:
			for pair in self.dict_valueStore.items():
				line = pair[0] + ":" + pair[1] + "\n"
				file_config.write(line)
			file_config.close()
			
			
	def ReadConfig(self):
		try:
			file_config = open(self.path_config, "r")
		except IOError:
			print "Error: ReadConfig() in class Config"
		else:
			self.dict_valueStore.clear()
			for line in file_config:
				line = line.split(':',1)
				if (len(line) == 2):
					self.dict_valueStore[line[0]] = line[1].strip('\n')
			file_config.close()
			
	def ReadConfigS(self, configContent):
		configContent = configContent.split('\n')
		self.dict_valueStore.clear()
		for line in configContent:
			line = line.split(':',1)
			if (len(line) == 2):
				self.dict_valueStore[line[0]] = line[1].strip('\n')
	
	def GetList(self):
		return self.dict_valueStore.items()
		
	def GetValue(self, value):
		try:
			output = self.dict_valueStore[value]
		except KeyError:
			print "Invalid Config Key: " + value
			print "Aborting.."
			quit()
			return 
		else:
			return output
			
	def RestoreDefaults(self):
		configString  = ""
		configString += "path_inputDir:../Input/" + "\n"
		configString += "path_outputDir:../Output/" + "\n"
		configString += "path_pageTemplate:./config/Page_Template.html" + "\n"
		configString += "path_frontTemplate:./config/Front_Template.html" + "\n"
		configString += "path_frontPage:../Output/index.html" + "\n"
		configString += "path_record:./config/Record.log" + "\n"
		configString += "path_relativeOut:" + "\n"

		self.ReadConfigS(configString)