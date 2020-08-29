# this code may not produce correct result format for grader
if __name__ == '__main__':
    print(" *** Multiples of 3 or 5 or 7 ***")
    number = int(input("Enter number : "))
    result = 0
    if number > 0:
        for i in range(3, number):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                result += i
        print(result)
    else:
        print(f"{number} is too low")
