# -*- coding: utf-8 -*-
def geoloc(ID_geonum):
	try:
		with file("geo.txt","r") as geofile:
			geoline = geofile.readlines()
	except IOError:
		print u"文件读取错误!请检查地理信息文件geo.txt是否存在并在同一级目录"
		return u"文件错误！"
	for i in xrange(len(geoline)):
		geoline[i]=geoline[i].strip("\n")
	address_dict = {}
	for i in xrange(0,len(geoline),2):
		address_dict[int(geoline[i])] = geoline[i+1]
	
	address_num_a = 0
	address_num_b = 0
	address_num_c = 0
	for i in xrange(2):
		address_num_a=address_num_a+int(ID_geonum[i])*(10**(5-i))
	for i in xrange(4):
		address_num_b=address_num_b+int(ID_geonum[i])*(10**(5-i))
	for i in xrange(6):
		address_num_c=address_num_c+int(ID_geonum[i])*(10**(5-i))
	address_word_a = address_dict[address_num_a]
	address_word_b = address_dict[address_num_b]
	address_word_c = address_dict[address_num_c]
	address_word = address_word_a + address_word_b  + address_word_c
	return address_word.decode()