master_word="abbcceddffggt"
chk_word="fat"
mw_dic={}
flag=0
for char in master_word:
    if char in mw_dic:
        mw_dic[char]+=1
    else:
        mw_dic[char]=1
print(mw_dic)
for char in chk_word:
    if char in mw_dic:
        cur_char_count=mw_dic.get(char)
        if cur_char_count>0:
            mw_dic[char]-=1
        elif cur_char_count==0:
            flag=1
            break
    else:
        flag=1
        break
if flag==1:
    print(False)
else:
    print(True)