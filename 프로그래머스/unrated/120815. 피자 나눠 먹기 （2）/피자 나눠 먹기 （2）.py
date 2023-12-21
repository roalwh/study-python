def solution(n):
    answer = 0
    for x in range(1,100):
        if((x*6)%n == 0):
            answer = x
            break
            
    return answer