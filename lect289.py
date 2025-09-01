# job sequencing first 

class job:
    def __init__(self, id , deadline , profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit


class solution:
    def jobscheduling(self, jobs):
        jobs.sort(key =  lambda x: x.profit , reverse = True) # this will sort the profit in desc order
        maxi = jobs[0].deadline
        for i in range(1, len(jobs)):
            maxi = max(maxi , jobs[i].deadline)
        
        hash = [-1]*(maxi+1)
        countjobs = 0 
        jobprofit = 0 
        for i in range(len(jobs)):
            for j in range(jobs[i].deadline ,0 ,-1):
                if hash[j] == -1:
                    hash[j] = i
                    countjobs +=1
                    jobprofit += jobs[i].profit
                    break
        return countjobs , jobprofit
    



if __name__ == "__main__":
    jobs = [job(1, 4 , 20) , job(2, 1, 10), job(3 , 2 , 40), job(4 ,2,30)]
    count , profit = solution().jobscheduling(jobs)
    print(count, profit)