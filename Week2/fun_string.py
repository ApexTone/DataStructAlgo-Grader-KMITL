def fun_string(text, choice):
    if choice == 1:  # len
        return len(text)
    elif choice == 2:  # switch lower/upper
        buffer = ''
        for i in range(len(text)):
            if text[i].isupper():
                buffer += chr(ord(text[i]) + 32)
            else:
                buffer += chr(ord(text[i]) - 32)
        return buffer
    elif choice == 3:  # reverse
        buffer = ''
        for i in range(len(text)-1, -1, -1):
            buffer = buffer + text[i]
        return buffer
    elif choice == 4:
        buffer = ''
        for i in range(len(text)):
            if text[i] not in buffer:
                buffer += text[i]
        return buffer


if __name__ == '__main__':
    word, number = input('Enter String and Number of Function : ').split()
    number = int(number)
    print(fun_string(word, number))
