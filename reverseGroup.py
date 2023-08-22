class Solution:	
    def reverseInGroups(self, arr, n, k):
        # code here
        for i in range(0,n,k):
            if(i+k >n):
                reverse(arr,i,n-1)
            else:
                reverse(arr,i,i+k-1)
        return arr
                
def reverse(arr,start,end):
    i =0
    while start <= end:
        arr[start],arr[end] = arr[end],arr[start]
        start +=1
        end -=1
        
   
            
        
        
		


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    n = 8
    k = 3
    arr = [1,2,3,4,5,6,7,8]
    ob = Solution()
    print (ob.reverseInGroups(arr, n, k))