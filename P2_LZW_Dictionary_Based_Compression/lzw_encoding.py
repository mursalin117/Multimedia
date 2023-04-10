f = open("input.txt", "r")

string = f.read()
# print(str)

dictionary = {}
for i in range(256):
	dictionary[chr(i)] = i

last = 256
result = []

s = string[0]
string = string[1:]

for c in string:
	temp = s+c
	if temp in dictionary:
		s = temp
	else:
		result.append(dictionary[s])
		dictionary[temp] = last
		last += 1
		s = c

result.append(dictionary[s])

result = str(result)
result = result[1:-1]

print(result)
f = open("lzw-compression.txt", "w")
f.write(result)














# f = open("input.txt", "r")

# string = f.read()
# # print(str)

# # string = "thisisthe"
# # dictionary = {chr(i):i for i in range(0,256)}
# # print(dictionary)

# # dictionary = {}
# # for i in range(256):
# # 	dictionary[i] = chr(i)

# last = 256
# p = ""
# result = []
 
# for c in string:
# 	pc = p+c
# 	if pc in dictionary:
# 		p = pc
# 	else:
# 		result.append(dictionary[p])
# 		dictionary[pc] = last
# 		last += 1
# 		p = c
 
# if p != '':
# 	result.append(dictionary[p])
 
# result = str(result)
# result = result[1:-2]

# print(result)
# f = open("lzw-compression.txt", "w")
# f.write(result)
