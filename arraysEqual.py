

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        A.sort()
        B.sort()
        if(A==B):
            return True
        #return: True or False
        else:
            return False
        #code here

        
if __name__ == 'main':
    N = 5
    A = [1,2,5,4,0]
    B = [2,4,5,0,1]
    
    if(Solution.check(A,B,N) == True):
        print("True")
    else:
        print("False")
