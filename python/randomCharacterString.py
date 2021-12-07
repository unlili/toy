'''
随机字符生成
2021年12月7日 23:39:48
主要是注册各种账号时生成各种各样的字符串来充当密码
'''

import random

#不要包含的字符
WHITE_LIST = "" 
#生成字符串长度
LEN = 40

#是否包含数字
IS_INCLUDE_NUMBER     = 1  # 1 true 0 false
#是否包含大写字母
IS_INCLUDE_BIG_WORD   = 1 # 1 true 0 false
#是否包含小写字母
IS_INCLUDE_SMALL_WORD = 1 # 1 true 0 false
#是否包含特殊字符
IS_INCLUDE_SPECIAL    = 1 # 1 true 0 false

#字符串中是否有重复
IS_REPEAT             = 1 # 1 true 0 false

#生成数量
COUNT                 = 5


#特殊字符
special_char = "~!@#$%^&*()_+{}[]\\;':\",./<>?" 
#小写字母
word_small = "abcdefghijklmnopqrstuvwxyz"
#大写字母
word_big = word_small.upper()
#大小写字母
word = word_small+word_big
#数字
number = "0123456789"

def getRandomIsRepeat():
	str = ''
	data = ''
	if IS_INCLUDE_NUMBER == 1 :
		data += number
	if IS_INCLUDE_BIG_WORD == 1:
		data += word_big
	if IS_INCLUDE_SMALL_WORD == 1:
		data += word_small
	if IS_INCLUDE_SPECIAL == 1:
		data += special_char
	for i in range(1,LEN+1):		
		index = random.randint(0,len(data)-1)
		str += data[index]
	return str

def getRandomIsNotRepeat():

	str = ''
	data = ''
	if IS_INCLUDE_NUMBER == 1 :
		data += number
	if IS_INCLUDE_BIG_WORD == 1:
		data += word_big
	if IS_INCLUDE_SMALL_WORD == 1:
		data += word_small
	if IS_INCLUDE_SPECIAL == 1:
		data += special_char

	if LEN > len(data) :
		return getRandomIsRepeat()

	for i in range(1,LEN+1):		
		index = random.randint(0,len(data)-1)
		if str.find(data[index],0,len(str)) == -1:
			str += data[index]
	return str

def getRandom():
	if IS_REPEAT == 1:
		return getRandomIsRepeat()
	elif IS_REPEAT == 0:
		return getRandomIsNotRepeat()
	elif IS_REPEAT != 0 or IS_REPEAT != 1:
		return getRandomIsRepeat()

def main():
	if COUNT < 0 :
		print("haha")
	elif COUNT==1 :
		print(getRandom())
	else :
		for i in range(1,COUNT+1):
			print(getRandom())

if __name__ == '__main__':
	main()
