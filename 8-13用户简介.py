#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

def build_profile(first,last,**user_info):
	"""����һ���ֵ䣬��������֪�����й��û���һ��"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	
	for key,value in user_info.items():
		profile[key] = value
		
	return profile
	
user_profile = build_profile('cui','wei',
						  age='20',
						  weight='80kg')
						  
print(user_profile)

