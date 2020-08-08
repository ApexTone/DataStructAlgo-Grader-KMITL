# Code by Rach (OSAMA)

if __name__ == '__main__':
    print('*** Electrion ***')  # Typo for grader submission
    n = int(input('Enter a number of voter(s) : '))  # for looping purpose which is useless because of next line
    votes = [int(x) for x in input().split()]  # input().split() will automatically separate each value to list
    candidate = 0
    max_ = 0
    for v in votes:
        if votes.count(v) > max_ and v > 0:
            max_ = votes.count(v)
            candidate = v

    if candidate == 0:
        print('*** No Candidate Wins ***')
    else:
        print(candidate)
