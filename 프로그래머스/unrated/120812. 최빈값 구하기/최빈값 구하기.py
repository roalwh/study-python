from collections import Counter
def solution(array):
        array_counter = Counter(array).most_common(2)
        tmp = []

        for key,val in array_counter:
            tmp.append(key)
            tmp.append(val)
        
        if(len(array_counter)>1):
            if(tmp[1]>tmp[3]):
                return tmp[0]
            elif(tmp[1]==tmp[3]):
                return -1
        else:
             return tmp[0]