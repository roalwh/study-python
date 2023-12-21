from math import floor
def solution(array):
    array.sort()
    return array[floor(len(array)/2)]