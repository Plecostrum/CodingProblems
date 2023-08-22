def solution(N,X):
    value = 0
    
    if N == 0:
        return 1
    if N < 0:
        return 0 
    else:
        for x in X:
            value += solution(N - x, X)
    return value

    
if __name__ == "__main__":
    N = 9
    X = [1,3,5]
    print(solution(N,X))