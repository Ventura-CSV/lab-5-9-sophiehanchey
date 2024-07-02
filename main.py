import random


def bubble(numbers):
    #loop through numbers (not last one or else encounter range error)
    currentIdx = 0
    nextIdx = 1
    for n in numbers - 1:
        if n > numbers[nextIdx]:
            # use a dummy variable for swap
            sub = numbers[nextIdx]
            numbers[nextIdx] = n
            numbers[currentIdx] = sub
        
        #increment loop values
        currentIdx += 1
        nextIdx += 1
            
        


def main():
    numbers = [2, 3, 0, 5, 4]
    print(numbers)
    bubble(numbers)
    print(numbers)    # must be [2, 0, 3, 4, 5]

    numbers = [random.randint(0, 10) for i in range(10)]
    print(numbers)
    bubble(numbers)
    print(numbers)


if __name__ == '__main__':
    main()
