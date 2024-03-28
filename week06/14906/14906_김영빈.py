def check_slump(text):
    if text[0] != 'D' and text[0] != 'E':
       
        return False
    else :
       
        if text[1] ==  'F':
            for i in range(2,len(text[2:])+2):
                if text[i]=='F':
                    continue
                elif text[i] =='G':
                    return True

                elif text[i] =='D' or text[i] =='E':
                     check_slump(text[i:])
                
                else :
        
                    return False

        else:
            return False


def check_slimp(text):
    if len(text) == 2 :
        if text == 'AH':
            return True
        else :
            return False
    elif len(text) > 2:

        if text[0] != 'A':
            return False
        else :
            pass
    else : 
        return False



N = int(input())
texts = [input() for _ in range(N)]

for text in texts:
    is_slump = check_slump(text)
    is_slimp = check_slimp(text)
    print(is_slump)
print('SLURPYS OUTPUT')








print('END OF OUTPUT')