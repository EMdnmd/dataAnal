'''
模板介绍：
coding: utf-8
Team : 无
Author：张恒瑞
Date ：2021/5/26 16:44
Tool ：PyCharm
'''
import  requests
ua={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
,'cookie': 'UM_distinctid=179a7b8dab4398-075c53120ac21a-2363163-1fa400-179a7b8dab54c5; CNZZDATA1275796416=280229462-1622014041-%7C1622014041; Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2=1622016581; Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2=1622018619'
}
xianindex=requests.get("https://lishi.tianqi.com/xian/index.html",params=ua)
print(xianindex.text)