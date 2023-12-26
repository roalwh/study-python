from math import floor

def solution(price):
    answer = 0
    if(price>=500000):
        return floor(price*0.8)
    elif(price>=300000):
        return floor(price*0.9)
    elif(price>=100000):
        return floor(price*0.95)
    else:
        return floor(price)
    
    