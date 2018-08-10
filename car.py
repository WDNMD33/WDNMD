#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

class Car():
	"""һ��ģ�������ļ򵥳���"""
	
	def __init__(self,make,model,year):
		"""��ʼ����������"""
		self.make = make
		self.model = model
		self.year = year
		self.odometre_reading = 0

	def get_descriptive_name(self):
		"""�����������������Ϣ"""
		long_name = str(self.year) + ' ' + self.make + ' ' +self.model
		return long_name.title()
		
	def read_odometre(self):
		"""��ӡһ��ָ��������̵���Ϣ"""
		print("This car has " + str(self.odometre_reading) + " miles on it.")
		 
	def update_odometre(self,mileage):
		"""
		����̱����ó�ָ����ֵ
		��ֹ����̱�ָ�����ص�
		"""
		if mileage >= self.odometre_reading:
			self.odometre_reading = mileage
		else:
			print("You can't roll back an odometre!")	 
		 
	def increment_odometre(self,miles):
		"""����̱�������ָ������"""
		self.odometre_reading += miles	 
	
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometre(23500)
my_new_car.read_odometre()

my_new_car.increment_odometre(100)
my_new_car.read_odometre()

class Battery():
	"""һ��ģ��綯������ƿ�ļ򵥳���"""
	
	def __init__(self,battery_size = 70):
		"""��ʼ����ƿ����"""
		self.battery_size = battery_size
		
	def describe_battery(self):
		"""��ӡһ��������ƿ��������Ϣ"""
		print("This car has a " + str(self.battery_size) + "-KWh battery.")

	def get_range(self):
		"""��ӡһ����Ϣ��ָ����ƿ���������"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 275
		
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
	
	def upgrade_battery(self):
		self.battery_size = 85
	
	
class ElectricCar(Car):
	"""
	�綯�����Ķ���֮��
	��ʼ���������ԣ��ٳ�ʼ���綯������������
	"""
	
	def __init__(self,make,model,year):
		"""��ʼ����������"""
		super().__init__(make,model,year)
		self.battery = Battery()
		
	def describe_battery(self):
		"""��ӡһ��������ƿ��������Ϣ"""
		print("This car has a " + str(self.battery_size) + "-KWh battery.")
		
	def fill_gas_tank(self):
		"""�綯����û������"""
		print("This car doesn't need a gas tank!")
	

	
	
	
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

