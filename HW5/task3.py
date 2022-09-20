def rle_compress(string):
    result = ''
    prev_symbol = ''
    count = 1
    for i in string:
        if i != prev_symbol:
            if prev_symbol:
                result += str(count) + prev_symbol
            count = 1
            prev_symbol = i
        else:
            count += 1
    result += str(count) + prev_symbol 
    return result

def rle_decompress(string):
    result = ''
    count = ''
    for i in string:
        if i.isdigit():
            count += i
        else: 
            result += i * int(count)
            count = '' 
    return result

path_decompressed = 'F:/GB/Courses/Python1/Homeworks/HW5/task3_decompressed.txt'
path_compressed = 'F:/GB/Courses/Python1/Homeworks/HW5/task3_compressed.txt'

with open(path_decompressed) as file1:
    str1 = file1.read()

with open(path_compressed, 'w') as file2:
    file2.write(rle_compress(str1))

# with open(path_compressed) as file2:
#     str2 = file2.read()

# with open(path_decompressed, 'w') as file1:
#     file1.write(rle_decompress(str2))

