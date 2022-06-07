for row in range(1,7):
    str=""
    for space in range(1,(7-row)):
        str+=" "
    for _ in range(1,(row+1)):
        str+="* "
    print(str)

