#!/usr/bin/env python3
#잠깐 생각나는거 썼다가 지웠다 하는 파일입니다.

'''
numbers = [1, 2, 3, 4, 5, 6]

# unpacking의 좌변은 리스트 또는 튜플의 형태를 가져야하므로 단일 unpacking의 경우 *a,를 사용
*a, = numbers
# a = [1, 2, 3, 4, 5, 6]

*a, b = numbers
# a = [1, 2, 3, 4, 5]
# b = 6

a, *b, = numbers
# a = 1
# b = [2, 3, 4, 5, 6]

a, *b, c = numbers
# a = 1
# b = [2, 3, 4, 5]
# c = 6

a, b, c, *c = numbers
# a = 1
# b = 2
# c = [4, 5, 6]
'''

for i in range(2, 2):
    print(i)