#coding:utf-8

first, second = None, None
string = ''
num_array = map(int, raw_input().split())
for i in xrange(26):
    num = num_array[i]
    if num != 0:
        if first == None:
            first = (chr(97+i), num)
        elif second == None:
            second = (chr(97+i), num)
            temp = (chr(97+i), num)
        elif num < second[1]:
            second = (chr(97+i), num)
            string = ''   
        else:
            string += chr(97+i) * num   

if first != None and second != None:
    first_char, first_num = first
    second_char, second_num = second
    if first_num > second_num:
        first_string = ''
        for i in xrange(ord(first_char)-97, ord(second_char)-97):
            num = num_array[i]
            if num != 0:
                first_string += chr(97+i) * num
        print ''.join((second_char, first_string, second_char*(second_num-1), string))
    else:
        if first_num <= 2:
            print ''.join((first_char*first_num, second_char*second_num, string))
        else:
            first_string = ''
            for i in xrange(ord(temp[0])-97+1, ord(second_char)-97+1):
                num = num_array[i]
                if num != 0:
                    first_string += chr(97+i) * num
            repeat_num = first_num - 2
            print ''.join((first_char*2, (temp[0]+first_char)*repeat_num, temp[0]*(temp[1]-repeat_num), first_string, string))
elif first != None:
    print first[0] * first[1]

"""
#全计算，太慢了
#实际上是有规律的
def next_permutation(string):
    '''
    获得下一个字典序
    in : 'aabb'
    out: 'abab'
    '''
    index = None
    for i in xrange(len(string)-1, 0, -1):
        if string[i] > string[i-1]:
            index = i-1
            break
    if index == None:
        return ''

    str_list = list(string)
    right = sorted(str_list[index+1:])
    for i in xrange(len(right)):
        if right[i] > str_list[index]:
            right[i], str_list[index] = str_list[index], right[i]
            break
    return ''.join(str_list[:index+1] + right)

num_array = map(int, raw_input().split())
string = ''
num_sum = 0
for i in xrange(26):
    char = chr(97+i)
    num_sum += num_array[i]
    string += char*num_array[i]

minimum = 1000001
smallest_string = ''
while 1:
    if string == '':
        break
    
    kmp = [0]
    for i in xrange(1, num_sum):
        l = kmp[i-1]
        while l > 0 and string[i] != string[l]:
            l = kmp[l-1]
        if string[i] == string[l]:
            kmp.append(l+1)
        else:
            kmp.append(0)
    kmp_sum = sum(kmp)
    
    if kmp_sum < minimum:
        smallest_string = string
        minimum = kmp_sum
    string = next_permutation(string)

print smallest_string
"""
