import sys

container = [""] * 100

def main():
    tc = int(input())

    for t in range(tc):
        global container
        container = [""] * 100
        a_to_z = ['?'] * 26
        a_to_z_bottom = ['?'] * 26

        N = int(input())
        for i in range(N):
            container[i] = input().strip()

        hint, target = input().strip().split()

        is_no_match = True
        for i in range(N):
            temp = ['?'] * 26
            temp_a_to_z_bottom = ['?'] * 26

            if len(container[i]) != len(hint):
                continue

            for j in range(len(hint)):
                a = container[i][j]
                b = hint[j]

                if (temp[ord(a) - ord('a')] != '?' and temp[ord(a) - ord('a')] != b) or \
                        (temp_a_to_z_bottom[ord(b) - ord('a')] != '?' and temp_a_to_z_bottom[ord(b) - ord('a')] != a):
                    break
                else:
                    temp[ord(a) - ord('a')] = b
                    temp_a_to_z_bottom[ord(b) - ord('a')] = a

                if j == len(hint) - 1:
                    if is_no_match:
                        a_to_z = temp[:]
                        a_to_z_bottom = temp_a_to_z_bottom[:]
                        is_no_match = False
                    else:
                        for l in range(26):
                            if a_to_z[l] != temp[l]:
                                a_to_z[l] = '?'

        if is_no_match:
            print("IMPOSSIBLE")
            continue

        for_a_to_z = [0] * 26
        count_for_a_to_z = 0
        for i in range(26):
            if a_to_z[i] != '?' and a_to_z[i] != '0':
                for_a_to_z[ord(a_to_z[i]) - ord('a')] += 1
                count_for_a_to_z += 1

        if count_for_a_to_z == 25:
            unselected = ' '
            for i in range(26):
                if not for_a_to_z[i]:
                    unselected = chr(97 + i)
                    break
            for i in range(26):
                if a_to_z[i] == '?' or a_to_z[i] == '0':
                    a_to_z[i] = unselected

        ans = ""
        for p in target:
            ans += a_to_z[ord(p) - ord('a')]

        print(ans)

if __name__ == "__main__":
    main()
