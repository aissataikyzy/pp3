def ooo():
    str="";
    for row in range(0, 7):
        for col in range(0, 7):
            if (((col==1 or col==5) and row!=0 and row!=6) or ((row==0 or row==6) and col>1 and col<5)):
                str=str+"*"
            else:
                str=str+" "
        str=str+"\n"
    print(str);