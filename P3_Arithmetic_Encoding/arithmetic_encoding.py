f = open("input.txt", "r")
string = f.read()

# string = input('Enter the string: ')
# print(string)

frequency = []
# frequency = np.array((1, ))
for i in range(256):
    frequency.append(0)

# print(frequency[33])
# print(frequency)

# characters = list()
# characters.extend(string)
# print(characters)

for c in string:
    frequency[int(ord(c))] += 1
# print(frequency)

probability = frequency
for i in range(256):
    probability[i] = probability[i]/len(string)
# print(probability)

s = set(string)
s = sorted(s)
# s = list(s)
print(s)
string_out = str(len(s)) + '\n'

# string_out = ''
for i in s:
    string_out += i + ' ' + str(probability[int(ord(i))]) + '\n'

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
range = 1.0

for i in string:
    low_temp = low
    low = low_temp + range * range_low[int(ord(i))]
    high = low_temp + range * range_high[int(ord(i))]
    range = high - low 

# print(low)
# print(high)

value = 1.0
result = 0.0
while (result < low):
    value /= 2
    result += value
    if (result > high):
        result -= value 

# print(result)
string_out += str(result)

f = open("a_compression.txt", "w")
f.write(string_out)