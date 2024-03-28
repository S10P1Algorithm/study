import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def pattern_match(code):
    pw = [0]*26
    ptn = []
    temp = 1
    for char in code:
        chr_num = ord(char)-ord('a')
        if not pw[chr_num]:
            pw[chr_num] = temp
            temp+=1
        ptn.append(pw[chr_num])
    return ptn

def decode_func(code, decode, encrypted):
    pw = ['?']*26
    possible_ans = []
    for i in range(len(code)):
        chr_num = ord(code[i])-ord('a')
        pw[chr_num] = decode[i]

    if (pw.count('?') == 1):
        last_chr = pw.index('?')
        bit = (1<<26) -1
        for i in range(26):
            if i != last_chr:
                bit ^= 1<<(ord(pw[i]) - ord('a'))
        pw[last_chr] = chr(len(bin(bit))-3 + ord('a'))
        

    for char in encrypted:
        chr_num = ord(char)-ord('a')
        possible_ans.append(pw[chr_num])
    return possible_ans


for _ in range(T):
    N = int(input())
    code = []
    for _ in range(N):
        code.append(input())
    decode = input()
    encrypted_ans = input()


    possible_idx = []
    ans_ptn = pattern_match(decode)
    for i in range(N):
        if pattern_match(code[i]) == ans_ptn:
            possible_idx.append(i)

    if possible_idx:
        ans_list = []
        for i in possible_idx:
            ans_list.append(decode_func(code[i], decode, encrypted_ans))
        
        ans = ans_list[0]

        for i in range(len(ans_list)):
            for idx in range(len(ans)):
                if ans[idx] != ans_list[i][idx]:
                    ans[idx] = '?'
        print(''.join(ans))
    else:
        print('IMPOSSIBLE')