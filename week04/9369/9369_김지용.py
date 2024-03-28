import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def check_encrypt(enc, unc):
    check_dict = dict()
    rev_dict = dict()
    len_enc = len(enc)
    if len_enc != len(unc):
        return False
    for i in range(len_enc):
        curr_enc = enc[i]
        curr_unc = unc[i]
        if check_dict.get(curr_enc) and check_dict.get(curr_enc) != curr_unc:
            return False
        if rev_dict.get(curr_unc) and curr_enc != rev_dict.get(curr_unc):
            return False
        check_dict[curr_enc] = curr_unc
        rev_dict[curr_unc] = curr_enc
    return check_dict


for test_case in range(1, T+1):

    N = int(input())

    encrypted = []

    for i in range(N):
       encrypted.append(input().strip())

    uncrypted = input().strip()

    target = input().strip()

    result = [''] * len(target)

    for k in encrypted:
        decode = check_encrypt(k, uncrypted)
        if decode:
            for j in range(len(target)):
                if decode.get(target[j]):
                    if result[j] == '':
                        result[j] = decode.get(target[j])
                    elif decode.get(target[j]) != result[j]:
                        result[j] = '?'
                else:
                    result[j] = '?'

    if ''.join(result):
        print(target, ''.join(result))
    else:
        print(target, 'IMPOSSIBLE')