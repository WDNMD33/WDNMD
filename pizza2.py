#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

def make_pizza(size,*toppings):
	"""����Ҫ����������"""
	print("\nMaking a " + str(size) + "-inch pizza with following toppings:")
	for topping in toppings:
		print("-" + topping)
