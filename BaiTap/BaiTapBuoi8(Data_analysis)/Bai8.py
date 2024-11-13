import numpy as np 

def solve():
    arr1 = np.random.randint(-50, 50, size = 7)
    arr2 = np.random.randint(-50, 50, size = 7)
    print(arr1)
    print(arr2)
    # noi 2 ma tran 1 chieu 
    arr3 = np.concatenate((arr1, arr2), axis = 0)
    # gop thanh ma tran 2x7 
    arr4 = arr3.reshape(2, 7)
    print(arr4)
    # xu li
    result = []
    for i in range(7):
        found = False
        for j in range(2):
            if arr4[j][i] > 0:
                    result.append(int(arr4[j][i]))
                    found = True
                    break
            else:
                if arr4[j][i] > 0 and j == 1:
                    result.append(int(arr4[j][i]))
                    found = True
                    break
        if found == False:
            result.append("None")
    print(result)

if __name__ == "__main__":
    solve()

