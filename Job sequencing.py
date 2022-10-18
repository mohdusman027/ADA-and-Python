# A class to store job details. Each job has an identifier, 
# a deadline, and profit associated with it. 
 
 
class Job: 
    def _init_(self, taskId, deadline, profit): 
        self.taskId = taskId 
        self.deadline = deadline 
        self.profit = profit 
  
  
# Function to schedule jobs to maximize profit 
def scheduleJobs(jobs, T): 
  
    # stores the maximum profit that can be earned by scheduling jobs 
    profit = 0 
  
    # list to store used and unused slots info 
    slot = [-1] * T 
  
    # arrange the jobs in decreasing order of their profits 
    jobs.sort(key=lambda x: x.profit, reverse=True) 
  
    # consider each job in decreasing order of their profits 
    for job in jobs: 
        # search for the next free slot and map the task to that slot 
        for j in reversed(range(job.deadline)): 
            if j < T and slot[j] == -1: 
                slot[j] = job.taskId 
                profit += job.profit 
                break 
  
    # print the scheduled jobs 
    print('The scheduled jobs are', list(filter(lambda x: x != -1, slot))) 
  
    # print total profit that can be earned 
    print('The total profit earned is', profit) 
  
  
if __name__== '__main__': 
  
    # List of given jobs. Each job has an identifier, a deadline, and 
    # profit associated with it 
    jobs = [ 
        Job(1, 9, 15), Job(2, 24, 2), Job(3, 5, 18), Job(4, 7, 1), Job(5, 4, 25), 
        Job(6, 2, 20), Job(7, 5, 8), Job(8, 7, 10), Job(9, 4, 12), Job(10, 3, 5) 
    ] 
  
    # stores the maximum deadline that can be associated with a job 
    T = 15 
  
    # schedule jobs and calculate the maximum profit 
    scheduleJobs(jobs, T)
