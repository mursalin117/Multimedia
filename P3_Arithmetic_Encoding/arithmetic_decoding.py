f = open("a_compression.txt", "r")
lines = f.readlines()

probability = []
s = []

for i in range(256):
    probability.append(0.0)

i = 0
for line in lines:
    # print(line)
    if (i == 0):
        n = line.strip()
        n = int(n)
        i += 1
        continue
    if (i == n+1):
        value = line.strip()
        value = float(value)
        continue

    num = line.strip().split(' ')
    probability[int(ord(num[0]))] = float(num[1])
    s.append(num[0])
    i += 1

range_low = []
range_high = []

for i in range(256):
    range_low.append(0.0)
    range_high.append(0.0)

range_high[int(ord(s[0]))] = probability[int(ord(s[0]))]

for i in range(1, len(s)):
    range_low[int(ord(s[i]))] = range_high[int(ord(s[i-1]))]
    range_high[int(ord(s[i]))] = range_low[int(ord(s[i]))] + probability[int(ord(s[i]))]

string_out = ''
for i in range(len(s)):
    for c in s:
        if (range_low[int(ord(c))] <= value and value <= range_high[int(ord(c))]):
            string_out += chr(ord(c))
            # print(c)
            low = range_low[int(ord(c))]
            high = range_high[int(ord(c))]
            range = high - low
            value = (value - low) / range
            # print(value) 

for c in s:
    if (range_low[int(ord(c))] <= value and value <= range_high[int(ord(c))]):
        string_out += chr(ord(c))

# for i in s:
#     print("low %4f" % range_low[int(ord(i))] + " high %4f" %range_high[int(ord(i))])

f = open("a_decompression.txt", "w")
f.write(string_out)