

def leastPrimeFactor (n):
        solution = [0 for _ in range(n+1)]
        solution[1]=1
        # code here
        
        for i in range(2,n+1):
            j =i
            while j < n+1:
                
                if solution[j] ==0:
                    solution[j] = i
                
                j+=i
        return solution

def main():
    n = 50
    print(leastPrimeFactor(n))

    
main()