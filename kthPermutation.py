#{ 
 # Driver Code Starts
#Initial Template for Python 34

# } Driver Code Ends
from typing import List


def reverse(array,l,h):
    
    while(l<h):
        array[l],array[h] = array[h],array[l]
        l+=1
        h-=1
    return array

def findCeil(array, c, k,n):
    ans =-1
    val =c
    
    for i in range(k,n+1):
        if(array[i] > c and array[i] < val):
            val = str[i]
            ans =i
    return ans

#Using Heaps
class Solution:
    def kthPermutation(self, n : int, k : int) -> str:
        
        arrayLen = n
        array = [str(x+1) for x in range(0,arrayLen)]
        array = sorted(array)
        
        currentPerm =0
        isFinished = False
        
        while not isFinished:
            
            currentPerm +=1
            print("".join(str(x) for x in array))


            for i in range(arrayLen -2, -1, -1):
                if(array[i] < array[i + 1]):
                    break
            
            if(i == -1):
                isFinished = True
            else:
                
                ceilIndex = findCeil(array,array[i], i+1, arrayLen -1)
                
                array[i], array[ceilIndex] = array[ceilIndex],array[i]
                
                array = reverse(array, i+1,arrayLen -1)
                
                
        return("".join(str(x) for x in array))
        
        
                
                


#{ 
 # Driver Code Starts.
if __name__=="__main__":
        
        N, K = 3,6
        
        obj = Solution()
        res = obj.kthPermutation(N, K)
        
        print(res)
        

# } Driver Code Ends