#coding=utf-8
#Author: kun
#Create time: 2012-11-16 10:47:50

#

import urllib

#Gameid
gameid = '000045'

#pid &　account不会影响测试结果可以写一个固定值
account = 'test4'
pid = '8c89a57230e4'

#账号类型与后台对应  0/1/2/3/4/5/100
List_Account_Type = ['0','1','2','3','4','5']

#服务器id
serverid = ''

#安装包类型id 1/2/1000
List_Cid = ['1006','1000']

fp = open('serverid.txt','r')
for line in fp:
	serverid = line.strip('\n')
#	print serverid
	for i in List_Account_Type:
		 accounttype = i
		 for j in List_Cid:
			cid = j

			url_prefix = 'http://svr.servers.xm.youxi.gigaget.com:8991/tipquery?'
			url = url_prefix + 'gameid=' + gameid +'&accounttype=' + accounttype + '&account=' + account + '&serverid=' + serverid + '&cid=' + cid + '&pid=' + pid
			
			u = urllib.urlopen(url)
			buffer = u.read()
			fp1 = open("result.txt","a")
			fp1.write(buffer+'  serverid='+serverid+',accounttype='+accounttype+',cid='+cid+'\n')

			fp1.close()
fp.close()
#print url