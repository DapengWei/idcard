# -*- coding: utf-8 -*-
import geofind
#function

#convert string to int list
def convID(list_num):
	int_num = []
	for i in range(17):
		int_num.append(int(list_num[i]))
	if list_num[17] == "x" or list_num[17] == "X":
		int_num.append(10)
	else:
		int_num.append(int(list_num[17]))
	return int_num
	
#verify ID 
def verifyID(int_verify):
	key=(7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
	key2=(1,0,10,9,8,7,6,5,4,3,2)
	all= 0
	for i in range(17):
		sum = int_verify[i]*key[i]
		all = all + sum	
	verify_num = key2[all%11]
	if int_verify[17] == verify_num:
		return True
	else:
		return False
		
#birthday
def birthdayID(ID_birthday):
	year = int(ID_birthday[0])*1000+int(ID_birthday[1])*100+int(ID_birthday[2])*10+int(ID_birthday[3])
	month = int(ID_birthday[4])*10+int(ID_birthday[5])
	day = int(ID_birthday[6])*10+int(ID_birthday[7])
	birthday_word = str(year)+"年"+str(month)+"月"+str(day)+"日"
	return birthday_word
#begin
while 1:
	print "请输入18位身份证号码:",
	ID_list = raw_input()	
	
	if len(ID_list) != 18:
		print"输入错误，位数不对，重新输入!"
		continue
	else:
		ID_num = convID(ID_list)
		if verifyID(ID_num):
			break
		else:
			print"输入错误，这不是合法的身份证号码，请重新输入!"
			continue		
	




address_num = []
for i in range(6):
	address_num.append(ID_num[i])
address = geofind.geoloc(address_num)

birthday_num = []
for i in range(6,14,1):
	birthday_num.append(ID_num[i])	
birthday = birthdayID(birthday_num)

if int(ID_num[16])%2 == 0 :
	sex = "女"
else:
	sex = "男"

print "该公民 性别:",sex,"籍贯:",address,"生日:",birthday
