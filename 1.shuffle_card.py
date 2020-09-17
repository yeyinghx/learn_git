#序列随机排序。
import random
import numpy as np
def shuffle_system(cards):
    random.shuffle(cards)#序列排序

def shuffle_1(cards):
    for k in range(len(cards)):
        i=random.randint(0,len(cards)-1)#生成随机序列
        j=random.randint(0,len(cards)-1)
        cards[i],cards[j]=cards[j],cards[i]#元素交换值

def shuffle_2(cards):
    for k in range(len(cards)):
        i=random.randint(0,len(cards)-1)
        cards[i],cards[k]=cards[k],cards[i]

def shuffle_correct(cards):
    for k in range(len(cards)):
        i=random.randint(k,len(cards)-1)
        cards[i],cards[k]=cards[k],cards[i]

def test_shuffle(func):
    result=[[0 for i in range(10)]for j in range(10)]
    for k in range(1000):
        T=[i for i in range(10)]
        func(T)
        for j in range(len(T)):
            result[T[j]][j]+=1
    print(np.array(result))#二维数组换行打印。下面那行看不懂。
    #print('\n'.join([''.join(['{:6}'.format(item)for item in row]) for row in result)]



A=[i for i in range(8)];print("初始列表:",A)
shuffle_1(A);print("错误1:",A)
#test_shuffle(shuffle_1)
shuffle_2(A);print("错误2:",A)
#test_shuffle(shuffle_2)
shuffle_system(A);print("系统算法:",A)
#test_shuffle(shuffle_system)
shuffle_correct(A);print("正确:",A)
#test_shuffle(shuffle_correct)