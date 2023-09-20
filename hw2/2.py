def rrr():
    str=""
    for row in range(0, 7):
        for col in range(0, 7):
            if (col==1 or ((row==0 or row==3) and col>1 and col<5) or (col==5 and row!=0 and row<3) or (col==row-1 and row>2)):
                str=str+"*"
            else:
                str=str+" "
        str=str+"\n"
    print(str)