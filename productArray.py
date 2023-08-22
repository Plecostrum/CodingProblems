def product(array):
    solution = ["x" for _ in range (0,len(array))]
    for i in range(len(array)):
        for x in array:
            if(x != array[i]):
                if(solution[i] == "x"):
                    solution[i] = (x)
                else:
                    solution[i] *= (x)
    return solution


def main():
    numbers = [1,2,3,4,5]
    print(product(numbers))
    
main()