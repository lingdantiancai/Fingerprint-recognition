

 
import time
import serial
 
ser = serial.Serial(7)  # ע��ѡ�񴮿ںţ� �� 0 ��ʼ������ �ҵ��� COM3 �����Բ����� 2 
line = ser.readline()
while line:
    print(time.strftime("%Y-%m-%d %X\t") + line.strip())
    line = ser.readline()
 
    # ÿ 10 ���򴰿�д��ǰ�����ʱ��
    sep  = int(time.strftime("%S")) % 10
    if sep == 0:
        ser.write('a')
    break
ser.close()







