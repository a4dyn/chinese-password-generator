# A python script used to generate password dictionary with custom settings
# Created by Junhan Duan, Aug. 18, 2020

from pypinyin import *
import itertools

customListNum = []
customListLet = []
customListRes = []
customListSym = []
customListSym2 = []
extraList = []
resultList = []
symbolList = ['!', '@', '#', '$', '%', '&', '*', '_']

def doCartesian(head, tail, writeTo):
    for x in itertools.product(head, tail):
        temp = ''.join(list(x[0]))
        temp += ''.join(list(x[1]))
        writeTo.append(temp)

def containsChinese(str):
    for _char in str:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

def readExtra(filename):
    file = open(filename, 'r')
    for line in file:
        line = line.replace('\n', '').replace('\r', '')
        extraList.append(line.strip())

def readCustom(filename):
    file = open(filename, encoding='utf-8')
    for line in file:
        line = line.replace('\n', '').replace('\r', '')
        # 英文字符自动加入Head，数字加入Tail
        if not containsChinese(line):
            if line.isnumeric():
                customListNum.append(line.strip())
            else:
                customListLet.append(line.strip())
        # 中文字符转字母
        else:
            # 中文字符的拼音整体
            customListLet.append(''.join(lazy_pinyin(line)))
            # 中文字符的拼音整体 - 首字母大写
            customListLet.append(''.join(lazy_pinyin(line)).capitalize())
            # 中文字符的拼音整体 - 全部大写
            customListLet.append(''.join(lazy_pinyin(line)).upper())
            # 中文字符的拼音首字母
            tempList = []
            combLetters = pinyin(line, style=Style.FIRST_LETTER)
            for _char in combLetters:
                tempList.append(''.join(_char))
            customListLet.append(''.join(tempList))
            # 中文字符的拼音首字母 - 首字母大写
            tempList = []
            combLetters = pinyin(line, style=Style.FIRST_LETTER)
            for _char in combLetters:
                tempList.append(''.join(_char))
            customListLet.append(''.join(tempList).capitalize())
            # 中文字符的拼音首字母 - 全部大写
            tempList = []
            combLetters = pinyin(line, style=Style.FIRST_LETTER)
            for _char in combLetters:
                tempList.append(''.join(_char).upper())
            customListLet.append(''.join(tempList))
            # 中文字符的前两个字
            if len(line) >= 2:
                firstTwo = line[:2]
                customListLet.append(''.join(lazy_pinyin(firstTwo)))
            # 中文字符的后两个字（通常为名字)
            if len(line) > 2:
                lastFirst = line[-1]
                lastSecond = line[-2]
                lastTwo = ''.join([lastSecond, lastFirst])
                customListLet.append(''.join(lazy_pinyin(lastTwo)))
            # 中文字符的前两个字 - 全部大写
            if len(line) > 2:
                firstTwo = line[:2]
                customListCN.append(''.join(lazy_pinyin(firstTwo)).upper())
            # 中文字符的后两个字（通常为名字) - 全部大写
            if len(line) > 2:
                lastFirst = line[-1]
                lastSecond = line[-2]
                lastTwo = ''.join([lastSecond, lastFirst])
                customListLet.append(''.join(lazy_pinyin(lastTwo)).upper())
    # 搭配自定字母 & 自定数字 & 符号
    # 字母 + 数字
    doCartesian(customListLet, customListNum, customListRes)
    # 字母 + 符号 + 数字
    doCartesian(customListLet, symbolList, customListSym)
    doCartesian(customListSym, customListNum, customListRes)
    # 字母 + 数字 + 符号
    tempList = []
    doCartesian(customListLet, customListNum, tempList)
    doCartesian(tempList, symbolList, customListRes)

# 将file内容添加至CustomResult
def includeFile(filename):
    includeList = []
    tempList = []
    file = open(filename, 'r')
    for line in file:
        line = line.replace('\n', '').replace('\r', '')
        includeList.append(line.strip())
    # 分别对字母与符号做精算笛卡尔乘
    # 字母 + file内容
    for x in itertools.product(customListLet, includeList):
        temp = ''.join(list(x[0]))
        temp += ''.join(list(x[1]))
        customListRes.append(temp)
        tempList.append(temp)
    # 字母 + 符号 + file内容
    for x in itertools.product(customListSym, includeList):
        temp = ''.join(list(x[0]))
        temp += ''.join(list(x[1]))
        customListRes.append(temp)
    # 字母 + file内容 + 符号
    for x in itertools.product(tempList, symbolList):
        temp = ''.join(list(x[0]))
        temp += ''.join(list(x[1]))
        customListRes.append(temp)

def writeFile(filename, fromList):
    with open(filename, 'w') as file:
        for x in fromList:
            if len(x) <= 16:
                file.write("{}\n".format(x))

def removeRedundant(finalList):
    finalList = list(dict.fromkeys(finalList))

# 将部分纯数字密码加入Result
def pureNumAsPswd(srcFile, dstList):
    srcLine = []
    file = open(srcFile, 'r')
    for line in file:
        line = line.replace('\n', '').replace('\r', '')
        srcLine.append(line.strip())
    for x in srcLine:
        if 6 <= len(x) <= 16:
            dstList.append(x)

# 构造经典密码词典 + 数字
def typicalGen():
    numLine = []
    typicalLine = []
    file1 = open('Typical.txt', 'r')
    for line in file1:
        line = line.replace('\n', '').replace('\r', '')
        typicalLine.append(line.strip())
    file2 = open('Numbers.txt', 'r')
    for line in file2:
        line = line.replace('\n', '').replace('\r', '')
        numLine.append(line.strip())
    for x in itertools.product(typicalLine, numLine):
        temp = ''.join(list(x[0]))
        temp += ''.join(list(x[1]))
        customListRes.append(temp)

if __name__ == '__main__':

    decision = int(input('请输入密码生成等级（1~3）：'))
    if decision >= 1:
        typicalGen()
        readExtra('Top100.txt')
    if decision >= 2:
        readCustom('Custom.txt')
        includeFile('Numbers.txt')
        pureNumAsPswd('Numbers.txt', customListRes)
    if decision == 3:
        readExtra('Top500.txt')
        readExtra('Numbers.txt')
        readExtra('Extra.txt')

    resultList = customListRes + extraList
    removeRedundant(resultList)
    writeFile('Result.txt', resultList)
