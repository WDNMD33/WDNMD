#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

def print_models(unprinted_designs,completed_models):
	"""
	ģ��ÿ����ƣ�ֱ��û��δ��ӡ�����Ϊֹ
	��ӡÿ����ƺ󣬶������ƶ����б�completed_models��
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		
		#ģ�����
		print("Printing model:" + current_design)
		completed_models.append(current_design)
		
def show_completed_models(completed_models):
	"""��ʾ�ô�ӡ�õ�ģ��"""
	print("\nFolowing models have been printed:")
	for completed_model in completed_models:
		print(completed_model)
		
unprinted_designs = ['iphone','cake','cat']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)	
	
	
	
	
	
