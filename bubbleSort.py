#!/usr/bin/python3
def bubbleSort(lst, reverse=False):
	length = len(lst)

	for i in range(length - 1):
		for j in range(length - 1):
			if not reverse and lst[j] > lst[j+1] or reverse and lst[j] < lst[j+1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]
		length -= 1

	return lst

if __name__ == "__main__":
	n = int(input())
	lst = []
	for i in range(n):
		lst.append(int(input()))

	print(bubbleSort(lst))