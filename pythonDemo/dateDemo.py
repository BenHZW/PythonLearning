#获取当前时间
'''
import time
#时间戳
"""
ticks = time.time()
print("当前时间为:",ticks)
"""

#当前时间
"""
localtime = time.localtime(time.time())
print ("本地时间为:",localtime)
"""

#获取格式化的时间
"""
formativeTime = time.asctime(time.localtime(time.time()))
print("格式化后的本地时间为:",formativeTime)
"""

#格式化日期
"""
print(time.strftime("%Y-%m-%d %a %H:%M:%S",time.localtime()))  #年月日 星期 时分秒
"""

#格式化字符串转换成时间戳
"""
char = "Mon Jan 28 11:07:20 2019"
print(time.mktime(time.strptime(char,"%a %%b d %H:%M:%S %Y")))
"""
'''

#获取某月日历
"""
import calendar

'''
calendars = calendar.month(2019,1)
print("以下输出2016年1月的日历:")
print(calendars)
'''
"""
