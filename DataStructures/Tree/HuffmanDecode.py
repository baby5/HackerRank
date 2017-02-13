#coding:utf-8

from __future__ import print_function

def docode(S, root):
    cur = root
    for char in S:
        if char == '0':
            if cur.data == 'ϕ':
                cur = cur.left
            else:
                cur = root
                print(cur.data, end='')
        elif char == '1':
            if cur.data == 'ϕ':
                cur = cur.right
            else:
                cur = root
                print(cur.data, end='')


def docode_improve(S, root):
    cur = root
    for char in S:
        cur = cur.left if char == '0' else cur.right
        if cur.data != 'ϕ':
            print(cur.data, end='')
            cur = root  
