import heapq

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''
    def __lt__(self, nxt):
        return self.freq < nxt.freq

def printNodes(node, val=''):
    newVal = val + node.code

    if (node.left):
        printNodes(node.left, newVal)
    if (node.right):
        printNodes(node.right, newVal)
    
    if (not node.left and not node.right):
        string_out = node.symbol + ' ' + newVal + '\n'
        f = open("huffman_compression.txt", "a")
        f.write(string_out)
        f.close()

def encoding(string):
    f = open("huffman_compression.txt", "r")
    lines = f.readlines()
    
    dictionary = {}

    i = 0
    for line in lines:
        if (i == 0):
            i += 1
            continue
        s = line.strip().split(' ')
        dictionary[s[0]] = s[1]
    
    string_out = ''
    for c in string:
        string_out += dictionary[c]
    
    f = open("huffman_compression.txt", "a")
    f.write(string_out)
    f.close()

def decoding():
    f = open("huffman_compression.txt", "r")
    lines = f.readlines()

    dictionary = {}

    i = 0
    for line in lines:
        if (i == 0):
            num = int(line.strip())
            i += 1
            continue
        if (i == num+1):
            encode = line.strip()
            continue
        s = line.strip().split(' ')
        dictionary[s[1]] = s[0]
        i += 1
    
    temp = ''
    string_out = ''
    for c in encode:
        temp += c
        if (temp in dictionary):
            string_out += dictionary[temp]
            temp = ''
    
    f = open("huffman_decompression.txt", "w")
    f.write(string_out)
    f.close()

def main():
    f = open("input.txt", "r")
    string = f.read()

    freq = []
    for i in range(256):
        freq.append(0)
    
    for c in string:
        freq[int(ord(c))] += 1
    
    nodes = []
    s = set(string)

    for c in s:
        heapq.heappush(nodes, node(freq[int(ord(c))], chr(ord(c))))

    while (len(nodes) > 1):
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.code = '0'
        right.code = '1'

        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

        heapq.heappush(nodes, newNode)
    
    f = open("huffman_compression.txt", "w")
    f.write(str(len(s)) + '\n')
    f.close()
    
    printNodes(nodes[0])
    
    encoding(string)

    decoding()

if __name__ == '__main__':
    main()