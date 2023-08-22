

def solveProblem(k,array):
    for x in array:
        if(array.count(k-x) !=0):
            return True
    return False





def main():
    array = [10,15,3,7]
    k = 13
    print(solveProblem(k,array))

main()