def main():
    f = open("input.txt", "r")
    string = f.read()

    frequency = []
    
    for i in range(256):
        frequency.append(0)

    for c in string:
        frequency[int(ord(c))] += 1

    probability = frequency
    
    for i in range(256):
        probability[i] = probability[i] / len(string)
    
    s = set(string)
    s = sorted(s)
    # s = s.sort()
    # print(s)

    string_out = str(len(s)) + '\n'
    
    for c in s:
        string_out += c + ' ' + str(probability[int(ord(c))]) + '\n'
    
    range_low = []
    range_high = []

    for i in range(256):
        range_low.append(0.0)
        range_high.append(0.0)
    
    range_high[int(ord(s[0]))] = probability[int(ord(s[0]))]
    
    for i in range(1, len(s)):
        range_low[int(ord(s[i]))] = range_high[int(ord(s[i-1]))]
        range_high[int(ord(s[i]))] = range_low[int(ord(s[i]))] + probability[int(ord(s[i]))]
    
    low = 0.0
    high = 1.0
    range_x = 1.0

    for c in string:
        low_temp = low
        low = low_temp + range_x * range_low[int(ord(c))]
        high = low_temp + range_x * range_high[int(ord(c))]
        range_x = high - low

    value = 1.0
    result = 0.0

    while(result < low):
        value /= 2
        result += value
        if (result > high):
            result -= value
    
    string_out += str(result)
    f = open("compressed.txt", "w")
    f.write(string_out)


if __name__ == '__main__':
    main()