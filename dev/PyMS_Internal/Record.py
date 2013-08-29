class Record():
	def __init__(self, recordLocation):
		self.path_record = recordLocation
		self.string_chunks = []
	
	def Read(self):
		self.string_chunks = []
		
		try:
			file_record = open(self.path_record,'r')
		except IOError:
			print "Error! Record: No record file found at " + self.path_record
			return
		else:
			pass
		
		string_recordContent = file_record.read()
		lines = string_recordContent.split('\n')
		file_record.close()

		lineIndex = 0
		charIndex = 0
		
		#print len(lines), len(string_recordContent)
		
		while((lineIndex < len(lines)) and (charIndex < len(string_recordContent))):
			if (lineIndex + 3 > len(lines)):
				break
			
			title = lines[lineIndex + 0]
			url = lines[lineIndex + 1]
			date = lines[lineIndex + 2]
			contentLength = lines[lineIndex + 3].split(':',1)[0]
			charIndex += len(title) + len(url) + len(date) + len(contentLength) + 1 + 3
			content = string_recordContent[charIndex:charIndex+int(contentLength)]
			charIndex += len(content) + 2
			lineIndex += 4 + content.count("\n") + 1
			
			chunk = [title,url,date,content]
			self.string_chunks.append(chunk)
		
		
	def Write(self, contentPages):
		for page in contentPages:
			chunk = [page.title, page.url, page.date, page.content]
			self.string_chunks.append(chunk)
		
		try:
			file_record = open(self.path_record,'w')
		except IOError:
			print "Error! Record: Couldn't write to " + self.path_record
			return
		else:
			string_output = ""
			for c in self.string_chunks:
				outputChunk = c[0] + '\n' + c[1] + '\n' + c[2] + '\n' + str(len(c[3])) + ':' + c[3] + '\n' + '\n'
				string_output += outputChunk
			file_record.write(string_output)
			file_record.close()
			
		self.Read()
	
	def chunks(self):
		return self.string_chunks