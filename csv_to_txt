import sys
import csv

f = open("첨단.csv", "r", encoding='cp949')
reader = csv.reader(f)

f2 = open("returned_list.txt", 'w')

search = input("책 이름 입력:")
for line in reader:
    if search in line[4]:
        f2.write(str(line))
    print(' ')






f.close()
f2.close()


