class Solution(object):
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        """
        :type nums: List[int]
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        lenNum = len(nums)
        maxNum = max(nums)
        sumNum = sum(nums)
        if cost1*2 <= cost2 or lenNum <= 2: return ((maxNum*lenNum - sumNum)*cost1)%(10**9+7)

        allDiffs = []
        for num in nums:
            allDiffs.append(maxNum - num)
        allDiffs.sort()
        steps1 = allDiffs[-1] - sum(allDiffs[0:lenNum-1])
        totalSteps = sum(allDiffs)
        costOpt = []
        if steps1 <= 0:
            steps1 = totalSteps%2
            steps2 = totalSteps//2
            costOpt.append(steps1*cost1 + steps2*cost2)
            if steps1 != 0 and lenNum%2:
                totalSteps += lenNum
                steps2 = totalSteps//2
                costOpt.append(steps2*cost2)
        else:
            steps2 = (totalSteps - steps1)//2
            if (totalSteps - steps1)%2:
                steps1 += 1
            costOpt.append(steps1*cost1 + steps2*cost2)
            extraHeight = steps1//(lenNum-2)
            totalSteps += lenNum*extraHeight
            if extraHeight*(lenNum-2) < steps1:
                steps2 = (totalSteps - (steps1 - extraHeight*(lenNum-2)))//2
                steps1 = totalSteps - steps2*2
            else:
                steps1 = totalSteps%2
                steps2 = totalSteps//2
            costOpt.append(steps1*cost1 + steps2*cost2)
            if steps1 != 0:
                # totalSteps += lenNum*steps1
                steps2 = (totalSteps + lenNum*steps1)//2
                steps1 = (totalSteps + lenNum*steps1)%2
                costOpt.append(steps1*cost1 + steps2*cost2)
                steps2 = (totalSteps + lenNum)//2
                steps1 = (totalSteps + lenNum)%2
                costOpt.append(steps1*cost1 + steps2*cost2) 
             
        return min(costOpt)%(10**9+7)
nums = [71,74,63,14,60]
cost1 = 82
cost2 = 2
nums = [84,87,84,40,18,90]
cost1 = 72
cost2 = 4
nums = [1,1000000]
cost1 = 1000000
co2 = 1
obj = Solution()
result = obj.minCostToEqualizeArray(nums, cost1, cost2)
print(result)
print(10**9+7) 