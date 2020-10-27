import math

def sum_cubes(k):
    count = 0

    for i in range (k):
        count += (i+1) ** 3

    return count

def sum_cubes_num_terms(n):
    previous_number = 0
    total = 0

    while ((previous_number + 1)**3 + total) < n:
        total += ((previous_number + 1) ** 3)
        previous_number += 1

    return (previous_number + 1)

def moving_average(measurements):
    average = []

    for i in range (1,len(measurements)-1,1):
       average.append((measurements[i-1] + measurements[i] + measurements[i + 1])/3)

    return average

def match(pattern,text):
    # if len(pattern)>len(text):
    #     return False
    #
    # if pattern in text:
    #     return True
    #
    # substring = ""
    # counter = 0
    #
    # while (substring in text):
    #     if substring + pattern[len(substring)] in text:
    #         substring += pattern[len(substring)]
    #     else:
    #         break
    #
    # if substring[-1] == text[-1]:
    #     for i in range (len(pattern) - len(substring)):
    #         if text[i] != pattern[len(substring)+i]:
    #             return False
    #     return True
    # return False

    test_text = text * 2

    return pattern in test_text

def share_n1(M1,M2):
    if M1 == M2:
        return True

    M1_trans = []
    M2_trans = []
    columns = []

    for i in range (len(M1[0])):
        for e in range(len(M1)):
            columns.append(M1[e][i])
        M1_trans.append(columns)
        columns.clear()

    for i in range (len(M2[0])):
        for e in range(len(M2)):
            columns.append(M2[e][i])
        M2_trans.append(columns)
        columns.clear()

    print(M1_trans)
    print(M2_trans)
    pass
    # M1_column = [[0]*len(M1)] * len(M1[0])
    # M2_column = [[0]*len(M1)] * len(M1[0])
    #
    # print(M1_column)
    #
    # counter = 0

    # for i in range(len(M1[0])):
    #     for e in range(len(M1)):
    #         M1_column[i][e] = M1[e][i]
    #         M2_column[i][e] = M2[e][i]
    #print(M1_column)

    #print (M1_column)
    #print (M2_column)

    # counter = 0
    #
    # test_1 = True
    # test_2 = True
    #
    # for i in range (len(M1[0])):
    #     for d in range(len(M1[0])):
    #         if M1[0][i] == M2[0][d]:
    #             for s in range(len(M1[0])):
    #                 if M1[i][s] != M2[i][s]:
    #                     counter -= 1
    #                     break
    #             counter += 1
    # return counter

    # counter = 0
    #
    # M1_column = [[M1[j][i] for j in range(len(M1))] for i in range(len(M1[0]))]
    #
    # M2_column = [[M2[j][i] for j in range(len(M2))] for i in range(len(M2[0]))]
    #
    # for i in range (len(M2_column)):
    #     for e in range(len(M1_column)):
    #         if M2_column[i] == M1_column[e]:
    #             counter += 1


if __name__ == "__main__":
    print(sum_cubes_num_terms(8))