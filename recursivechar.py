pattern="ABACCD"
f_rec={}
rec_char=[]
for st in pattern:
    if st in f_rec:
        rec_char.append(st)
    else:
        f_rec[st]=1
print("first_recursive character",rec_char[0])
print("second recursive character",rec_char[1])
# most recursive?