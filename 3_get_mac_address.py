writefile = open('mac_address.txt','w')
with open('ipphone_web_content.txt', "r") as ifile:
	for line in ifile:
		if line.startswith((" MAC Address","MAC Address")):
			writefile.write(next(ifile, '').strip()+'\n')