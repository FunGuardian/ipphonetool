writefile = open('serial_number.txt','w')
with open('ipphone_web_content.txt', "r") as ifile:
	for line in ifile:
		if line.startswith((" Serial Number","Serial Number")):
			writefile.write(next(ifile, '').strip()+'\n')