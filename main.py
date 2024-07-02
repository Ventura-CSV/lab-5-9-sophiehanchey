import random


def bubble(numbers):
    #loop through numbers (not last one or else encounter range error)
    currentIdx = 0
    nextIdx = currentIdx + 1
    for n in range(len(numbers)-1):
        # swap execution
        if n > numbers[nextIdx]:
            # use a dummy variable for swap
            sub = numbers[nextIdx]
            numbers[nextIdx] = n
            numbers[currentIdx] = sub
        
        #checking each iteration
        print(f'{currentIdx}: {n} -> {numbers}')
        #increment loop values
        currentIdx += 1
        nextIdx += 1
            
        


def main():
    numbers = [2, 3, 0, 5, 4]
    numbers = [5, 4, 3, 2, 1]
    print(numbers)
    bubble(numbers)
    print(numbers)    # must be [2, 0, 3, 4, 5]

    numbers = [random.randint(0, 10) for i in range(10)]
    print(numbers)
    bubble(numbers)
    print(numbers)


if __name__ == '__main__':
    main()
