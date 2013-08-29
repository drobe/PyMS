from PyMS_Internal.Config import Config
from PyMS_Internal.ContentPage import ContentPage
from PyMS_Internal.FrontPage import FrontPage
from PyMS_Internal.Record import Record
from PyMS_Internal.TemplatePage import TemplatePage
import os, shutil

config = Config("./config/config.cfg")
#config.RestoreDefaults()
#config.SaveConfig()
#quit()

# Scan the directory for new files
directoryList = os.listdir(config.GetValue("path_inputDir"))
if (1): # Create new scope
	trimmedDirectoryList = []
	extension = "zip".lower()
	for count in range(0, len(directoryList)):
		file = directoryList[count]
		filePair = file.rsplit('.',1)
		if (len(filePair) == 2 and filePair[1].lower() == extension):
			trimmedDirectoryList.append(file)
		count += 1
		
	# Collect File paths
	directoryList = trimmedDirectoryList

# If no new files, End prgram
if (len(directoryList) <= 0):
	print "Nothing new to process"
	quit()

# Load Templates
template_frontPage = TemplatePage(config.GetValue("path_frontTemplate"))
template_contentPage = TemplatePage(config.GetValue("path_pageTemplate"))

# Load Record
record = Record(config.GetValue("path_record"))
record.Read()

# Load FrontPage
frontPage = FrontPage(config.GetValue("path_frontPage"))

# Process Content Pages
contentPages = []
for file in directoryList:
	contentPage = ContentPage(config.GetValue("path_inputDir") + file)
	contentPages.append(contentPage)
	
	loop = [True,False]
	count = 0
	while(loop[0] or loop[1]):
		loop[0] = False
		filePath = config.GetValue("path_outputDir") + contentPage.title
		try:
			os.mkdir(filePath + (" - " + str(count) if loop[1] else ""))
		except OSError:
			if (count < 10):
				count += 1
				loop[1] = True
				
			else:
				loop[1] = False
		else:
			filePath += (" - " + str(count) if loop[1] else "")
			contentPage.url = contentPage.title
			contentPage.Write(filePath, template_contentPage)
			loop[1] = False
	#shutil.move(config.GetValue("path_inputDir") + file, "../Archive/" + file + (" - " + str(count) if (count != 0) else ""))

# Update Record
record.Write(contentPages)

# Update FrontPage
frontPage.Write(record, template_frontPage)



