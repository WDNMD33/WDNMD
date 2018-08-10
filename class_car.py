#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

"""һ�������ڱ�ʾ��������"""

class Car():
	"""һ��ģ�������ļ򵥳���"""
	
	def __init__(self,make,model,year):
		"""��ʼ����������"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_discriptive_name(self):
		"""�������������������"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		"""��ӡһ����Ϣ��ָ���������"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self,mileage):
		"""
		����̱����ó��ض�ֵ
		�ܾ�����̱����ز�
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can not roll back an odometer!")
			
	def increment_odometer(self,miles):
		"""����̱��������ָ����"""
		self.odometer_reading += miles
		
class Battery():
    """һ��ģ��綯������ƿ�ļ򵥳���"""
    def __init__(self,battery_size = 60):
        """��ʼ����ƿ����"""
        self.battery_size = battery_size

    def describe_battery_size(self):
        """��ӡһ��������ƿ��������Ϣ"""
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def get_range(self):
        """��ӡһ��������ƿ������̵���Ϣ"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."

        print(message)

class ElectricCar(Car):
    """ģ��綯�����Ķ���֮��"""
    def __init__(self,make,model,year):
        """
        ��ʼ���������ԣ��ٳ�ʼ���綯������ʼ����
        """
        super().__init__(make,model,year)
        self.battery = Battery()

