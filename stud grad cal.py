total=0
for i in range(1,6):
 mark=int(input("enter your marks"+str(i)+":"))
 total=total+mark
 
totl=print("totalmarks=",total) 
per=print("persentage is:",(total/5))
 
if mark>=90:
    print("grade = A")
elif mark>=70 :
        print("grade = C")
elif mark>=60 :
        print("grade = D")
else:
    print("fail")   
    