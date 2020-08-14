def mapping(text):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    mapper = dict()
    counter = 0
    for alphabet in alphabets:
        mapper[alphabet] = mapper.get(alphabet, -1)
    # print(mapper)
    output = list()
    for character in text:
        if mapper[character] == -1:
            mapper[character] = counter
            counter += 1
        output.append(mapper[character])
    return output


if __name__ == '__main__':
    word = input('Enter String : ')
    print(mapping(word))
