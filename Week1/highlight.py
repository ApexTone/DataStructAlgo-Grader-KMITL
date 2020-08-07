if __name__ == '__main__':
    print('*** Reading E-Book ***')
    text, highlight = input('Text , Highlight : ').split(',')  # highlight will be just a single character
    out=''
    for i in range(len(text)):
        if text[i] == highlight:
            out += "[" + text[i] + "]"
        else:
            out += text[i]
    print(out)