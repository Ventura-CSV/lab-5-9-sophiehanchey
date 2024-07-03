import random


def bubble(numbers):
    #loop through numbers (not last one or else encounter range error)
    for i in range(len(numbers)-1):
        # swap execution
        if numbers[i] > numbers[i+1]:
            # use a dummy variable for swap
            sub = numbers[i+1]
            numbers[i+1] = numbers[i]
            numbers[i] = sub

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
