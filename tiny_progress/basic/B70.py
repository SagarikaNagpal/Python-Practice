import math

for i in range(10,100):
    print(i)
    num = str(i)
    revNum = int(num[::-1])
    sq_num = int(math.pow(i,2))
    rev_sq_num = int(math.pow(revNum,2))

    if sq_num == rev_sq_num:
        print(f'They match, the sq of {i} = {sq_num} and the {revNum} is {rev_sq_num} !!')

    else:
        print('It doesnot!!')

