a=input("請輸入數學考試成績")
s=input("請輸入英文考試成績")
s=int(s)
a=int(a)
if a>100  or a<0:
    print("輸入100以下,0以上的數字")
elif a >= 90 and s >= 90:
    print("有獎品")    
elif a >=60 or s >= 60:
    print("再加油")
else:
    print("要處罰") 

