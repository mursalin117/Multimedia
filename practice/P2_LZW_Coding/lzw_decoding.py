def main():
    # file read
    f = open("compressed.txt", "r")
    # file content read as an array
    arr_old = f.read().split(', ')

    # formatting the input as integer
    arr = []
    for i in range(len(arr_old)):
        arr.append(int(arr_old[i]))

    # creating dictionary and index will be the integer
    dictionary = {}
    for i in range(256):
        dictionary[i] = chr(i)
    
    # next character assign index
    last = 256
    # storing result in string
    result = ""

    # algorithm for decompression
    s = None
    
    for k in arr:
        try:
            entry = dictionary[k]
        except:
            entry = None
        finally:
            if (entry == None):
                entry = s + s[0]
            
            result += entry

            if (s != None):
                dictionary[last] = s + entry[0]
                last += 1
            
            s = entry

    # output the result in decompressed form
    print(result)
    f = open("decompressed.txt", "w")
    f.write(result)

if __name__ == '__main__':
    main()
