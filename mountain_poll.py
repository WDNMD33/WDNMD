# -- coding: utf-8 --

responses = {}

#����һ����־���ж�ѭ���Ƿ����
polling_active = True

while polling_active:
	#��ʾ���뱻�����ߵ����ֺͻش�
	name = input("\nWhat's your name?")
	response = input("\nWhich mountain would you like to clib someday?")
	
	#���𰸴������ֵ���
	responses[name] = response
	
	#�����Ƿ�����Ҫ�μӵ���
	repeat = input("\nWould you like to let another person respond?(yes/no)")
	if repeat == 'no':
		polling_active = False
		
#�����������ʾ���
print("\n---Poll Results---")
for name , response in responses.items():
	print(name + " would like to climb " + response + '.')




