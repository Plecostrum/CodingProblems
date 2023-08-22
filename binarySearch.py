#User function template for Python

class Solution:	
    def binarysearch(self, arr, n, k):
        # code here
        low = 0
        high = n-1
        while low <= high:
            mid = low + (high-low)//2
            if(arr[mid] == k):
                return mid
            elif (arr[mid] > k):
                high = mid -1 
            else:
                low = mid +1
        return -1
		


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    n = 65
    arr = [2, 3, 4, 5, 7, 8, 9, 11, 12, 14, 15, 19, 20, 22, 25, 26, 28, 32, 33, 35, 36, 37, 38, 41, 43, 44, 45, 46, 49, 50, 51, 52, 53, 55, 59, 60, 61, 62, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 88, 92, 93, 94, 95, 96, 98, 99,] 
    k = 222
    ob = Solution()
    print (ob.binarysearch(arr, n, k))


# } Driver Code Ends