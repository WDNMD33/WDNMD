#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

import time
import xlrd
import math

xlrd.Book.encoding = "utf-8"
file_path = 'D:\\��ѧ��ģ\\2018��D��-���ڶ�Դ������ݵĵ�·��ͨ��״̬�ع��о�\\����������\\date=20180325\\f_20180325.xlsx'

def read_file():
    data = xlrd.open_workbook(file_path)  # ���ļ�
    table = data.sheet_by_index(0)  # ȡ��һ�Ź�����
    rows_count = table.nrows  # ������
    cols_count = table.ncols  # ������
    #print(rows_count)

    for row in range(0,rows_count):
        unix_time = math.floor(table.cell(row,0).value)
        time_local = time.gmtime(unix_time)
        # ת�����µ�ʱ���ʽ(2018-03-25 20:28:54)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        print(dt)

read_file()