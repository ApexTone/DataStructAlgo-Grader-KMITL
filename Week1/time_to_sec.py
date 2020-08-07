if __name__ == '__main__':
    print('*** Converting hh.mm.ss to seconds ***')
    h, m, s = input("Enter hh mm ss : ").split()
    if int(h) < 0:
        print(f"hh({h}) is invalid!")
        quit()
    elif int(m) < 0 or int(m) >= 60:
        print(f"mm({m}) is invalid!")
        quit()
    elif int(s) < 0 or int(m) >= 60:
        print(f"ss({s}) is invalid!")
        quit()
    sec = int(s)
    sec += int(m)*60
    sec += int(h)*3600
    if len(s) == 1:
        s = '0'+s
    if len(m) == 1:
        m = '0'+m
    if len(h) == 1:
        h = '0'+h
    print(f"{h}:{m}:{s} =", format(sec, ',d'), "seconds")
