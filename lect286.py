
#  lemonade change 

bills = list(map(int , input().split()))

def function(bills):
    five = 0 
    ten = 0 
    twenty = 0 
    for i in range(len(bills)):
        if bills[i] == 5:
            five +=1
        elif bills[i] ==10:
            if five:
                ten+=1
                five -=1
            else:
                return False
        else:
            if ten and five:
                ten = ten -1
                five =  five -1
            elif five >= 3:
                five -=3
            else:
                return False
    return True    

print(function(bills))