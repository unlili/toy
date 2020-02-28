import time
'''
输入某一天计算到这一天的还有几天

final_year        最终年份  
final_month       最终月份   
final_day         最终日期   

method:
getNowTime()      输出一个列表 0当前年份，1单前月份，2单前日期
isLeapYear()      判断是不是闰年
getDay()          输入年份，输出输入年份的天数
getSurplusDay()   输入日期一个列表[年,月,日]     输出着一年还有多少天
getLiveDay()      输入日期一个列表[年,月,日]     输出着一年已经生活了多少天
getAllSurplusDay()   输出距离最终时间的天数
getTimeDay()      输入两个日期列表               输出两个日期相差的天数
getTimeDay()      输入两个日期列表               输出两个日期相差的小时
getTimeDay()      输入两个日期列表               输出两个日期相差的秒数

''' 
class MyTime:
	def __init__(self,final_year,final_month,final_day):
		self.final_year = final_year
		self.final_month = final_month
		self.final_day = final_day
		self.december  = 31#12 31
		self.noveber   = 30#11 30
		self.october   = 31#10 31
		self.september = 30#9  30
		self.august    = 31#8  31
		self.july      = 31#7  31
		self.june      = 30#6  30
		self.may       = 31#5  31
		self.april     = 30#4  30
		self.march     = 31#3  31
		if ( (self.final_year%4==0) and (self.final_year%100!=0) ) or (self.final_year%400==0):
			self.february  = 29#2  29
		else:
			self.february = 28
		self.january   = 31#1  31

		self.dayList = [
			0,
			self.january,
			self.february,
			self.march,
			self.april,
			self.may,
			self.june,
			self.july,
			self.august,
			self.september,
			self.october,
			self.noveber,
			self.december
		]
		self.surplusDay = 0 #剩余日期

	def getNowTime(self):
		now = time.localtime(time.time())
		now_year = int(now[0])  #
		now_month = int(now[1]) #2
		now_day = int(now[2])   #28
		return [now_year,now_month,now_day]

	def isLeapYear(self,number):
		if ( (number%4==0) and (number%100!=0) ) or (number%400==0):
			return True
		return False

	def getDay(self,number):
		if (self.isLeapYear(number)): return 366
		return 365

	def getLiveDay(self,date):	
		year = date[0]
		if self.isLeapYear(year):
			new_february = 29
		else:
			new_february = 28

		self.dayList[2] = new_february
		month = date[1]    #3
		day = date[2]      #4
		all = 0

		for i in range(1,month):
			all += self.dayList[i]

		return all + day
	
	def getSurplusDay(self,date):
		if self.isLeapYear(date[0]):
			day = 366
		else:
			day = 365
		return day - self.getLiveDay(date)

	def getTimeDay(self,a,b):
		if a[0] > b[0]:
			a,b = b,a

		year = a[0]   # 0
		month = a[1]  # 0
		day = a[2]    # 0
		all = 0
		#b[0] = 2020
		#b[1] = 2
		#b[2] = 29
		offset = b[0] - year - 1

		if offset == -1:
			return self.getLiveDay(b) - self.getLiveDay(a)
		if offset == 0 :
			print('--')
			all += self.getLiveDay(b)
			all += self.getSurplusDay(a)
			return all

		else:
			for i in range(year+1,b[0]):
				all += self.getDay(i)

			all += self.getLiveDay(b)
			all += self.getSurplusDay(a)
			return all
	def getTimeHour(self,a,b):
		return self.getTimeDay(a,b)*60
	def getTimeSecond(self,a,b):
		return self.getTimeHour(a,b)*60
	def getAllSurplusDay(self):
		a = [self.final_year,self.final_month,self.final_day]
		return self.getTimeDay(self.getNowTime(),a)

def main():
	t = MyTime(2020,12,21) 
	print('距离考研还有：{0}天'.format(t.getAllSurplusDay()))
	print("加油！！！！，你是最棒的")
	print("相信你自己。")


if __name__ == '__main__':
	main()