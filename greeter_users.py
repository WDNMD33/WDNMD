#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

def greeter_user(names):
	"""���б���ÿλ�û����ͼ򵥵��ʺ�"""
	for name in names:
		msg = "Hello, " + name.title() + '!'
		print(msg)
		
user_names = ['cuiwei','liuxueshu','liuxuan']
greeter_user(user_names)
