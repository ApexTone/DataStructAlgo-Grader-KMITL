if __name__ == '__main__':
    inp = list(map(int, input('Enter number end with (-1) : ').split()))
    if inp.count(-1) <= 0:
        print('Invalid INPUT !!!')
    else:
        new_inp = list()
        for i in inp:
            if i == -1:
                break
            new_inp.append(i)
        if new_inp != []:
            inp = new_inp
            ans = dict()
            set_inp = set(inp)
            for i in set_inp:
                ans[i] = inp.count(i)

            m = 0
            key_ans = 0
            all_freq = 0
            for k, v in ans.items():
                all_freq += v
                if v > m:
                    m = v
                    key_ans = k
            if ans[key_ans] > all_freq/2:
                print(key_ans)
            else:
                print('Not found')
        else:
            print('Not found')
