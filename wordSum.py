# coding=utf-8
# auther: 44886
# 2019-03-16
'''
如果把英语的ABCDEFGHIJKLMNOPQRSTUVWXYZ
对应数字的 1 2 3 4 5 6 7 8 9 10 ……
那是每个单词的得分是多少呢？
本计算使用ascii小写字母和数字的对应关系：
a在ascii中是97，但我们在此认为它是1，所以，每个字母都是 ascii - 96
'''

while True:  # 使用循环，这样可以不停让用户输入单词
    word = input('请输入一个单词来计算:').lower()
    if word == "exit":
        break
    sum = 0
    for i in word:
        sum = sum+ord(i)-96
    print('您输入的单词是:{},值为:{}%'.format(word, sum))
