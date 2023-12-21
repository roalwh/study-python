def solution(array, n):
    answer = 0
    for x in array:
        if(n==x):
            answer+=1
            
    return answer