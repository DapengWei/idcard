# -*- coding: utf-8 -*-
def geoloc(ID_geonum):
	geofile = file("geo.txt","r")
	geoline = geofile.readlines()
	for i in range(len(geoline)):
		geoline[i]=geoline[i].strip("\n")
	address_dict = {}
	for i in range(0,len(geoline),2):
		address_dict[int(geoline[i])] = geoline[i+1]
	address_num_a = 0
	address_num_b = 0
	address_num_c = 0
	for i in range(2):
		address_num_a=address_num_a+int(ID_geonum[i])*(10**(5-i))
	for i in range(4):
		address_num_b=address_num_b+int(ID_geonum[i])*(10**(5-i))
	for i in range(6):
		address_num_c=address_num_c+int(ID_geonum[i])*(10**(5-i))
	address_word_a = address_dict[address_num_a]
	address_word_b = address_dict[address_num_b]
	address_word_c = address_dict[address_num_c]
	address_word = address_word_a + address_word_b  +address_word_c
	return address_word  