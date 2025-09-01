
# fractional knapsack 

class item:
    def __init__(self, value,weight):
        self.value = value
        self.weight = weight


class Solution:
    def function(self, arr,w):
        arr.sort(key = lambda x: x.value/x.weight , reverse = True)
        total = 0
        for i in range(len(arr)):
            if arr[i].weight <= w:
                total += arr[i].value
                w = w - arr[i].weight
            else:
                total += float(arr[i].value/arr[i].weight)*w
                break
        return total
    
    
if __name__ == "__main__":
    n = 4
    w = 90
    arr = [item(100 , 20),item(60 , 10), item(100,50),item(200,50)]
    obj = Solution()
    print(obj.function(arr,w))

