def main():
    # file read
    f = open("input.txt", "r")
    # file content read
    string = f.read()

    # creating dictionary and index will be character of the string
    dictionary = {}
    for i in range(256):
        dictionary[chr(i)] = i
    
    # next character assign index
    last = 256
    # storing result in list
    result = []

    # algorithm for compression
    s = string[0] # first character of the string
    string = string[1:]

    for c in string:
        temp = s + c
        if temp in dictionary:
            s = temp
        else:
            result.append(dictionary[s])
            dictionary[temp] = last
            last += 1
            s = c
    result.append(dictionary[s])

    # converting result to string
    result = str(result)
    # formatting the string
    result = result[1:-1]

    # output the result in compressed form
    print(result)
    f = open("compressed.txt", "w")
    f.write(result)

if __name__ == '__main__':
    main()
