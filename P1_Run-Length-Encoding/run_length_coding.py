file_in = open("input.txt", "r")

string_in = file_in.read()
# print(string_in)

string_out = ''

i = 0
while (i < len(string_in)):
    cnt = 1
    j = i+1
    while (j < len(string_in)):
        if (string_in[i] == string_in[j]): 
            cnt += 1
        j += 1

    # if (cnt > 1):
    #     # temp = chr(255) + ' ' + chr(cnt) + ' ' + string_in[i] + ' '
    #     temp = + chr(cnt) + ' ' + string_in[i] + ' '
    # else:
    #     temp = string_in[i] + ' '
    temp = chr(cnt) + ' ' + string_in[i] + ' '   
    string_out += temp
    
    i = j-1
    i += 1

file_com = open("rle_compressed.txt", "w")
file_com.write(string_out)