#Problem 1
def find_lol(text_name):
    '''Opens the file text_name.txt and prints all lines in it that contain
    lol (not case sensitive).
    '''
    f = open(text_name+".txt")
    text = f.read()
    text = text.split("\n")

    for line in text:
        if "lol" in line.lower():
            print(line)

#Problem 2
def dict_to_str(d):
    '''Return a str containing each key and value in dict d. Keys and values
    are separated by a comma. Key-value pairs are separated by a newline
    character from each other.
    '''
    for items in d.items():
        print(f"{items[0]}, {items[1]}")

#Problem 3
def dict_to_str_sorted(d):
    '''Return a str containing each key and value in dict d. Keys and values
    are separated by a comma. Key-value pairs are separated by a newline
    character from each other, and are sorted in ascending order by key
    '''
    dict_list = []
    for keys, values in d.items():
        dict_list.append([keys, values])

    dict_list.sort()
    for i in range(len(dict_list)):
        print(dict_list[i][0], ",", dict_list[i][1])

#Problem 4
'''Creates a dictionary whose keys are words and whose values are lists of
phones
'''
f = open("dict.txt")
text = f.read()
text = text.split("\n")
dict = {}

count = 0

for lines in text:
    if not ";;;" in lines:
        cur_line = lines.split("  ")
        if len(cur_line) == 2:
            key = cur_line[0]
            value = cur_line[1]
            print(key, value)
            dict[key] = value
            # count +=1
            # if count == 3:
            #     break

print(dict)

# if __name__ == "__main__":
#     d = {1:2,5:6,0:4}
#     dict_to_str_sorted(d)

