#-*-coding:utf-8-*- 
# @File    : test.py
list1 = ['1','2','3']
list2 = ['A','B','C']
list3 = ['+','-','*']

for l1 in list1:
    for l2 in list2:
        for l3 in list3:
            print(l1 + l2 + l3)
"""
1A+
1A-
1A*
1B+
1B-
1B*
1C+
1C-
1C*
2A+
2A-
2A*
2B+
2B-
2B*
2C+
2C-
2C*
3A+
3A-
3A*
3B+
3B-
3B*
3C+
3C-
3C*
"""
