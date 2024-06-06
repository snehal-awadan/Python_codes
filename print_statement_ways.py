a=20
b=30
c=90

print("A:",a ,"B:",b ,"C:",c)

# Here we are printing A B C as string and its value are in the form of int, so we need to convert into str to concatenate it; 
print("A:"+str(a)+"B:"+str(b)+"C:"+str(c))

#formatting printing statement:
print(f"A:{a} B:{b} C:{c}")

#using format syntax:
print("A:{0} B:{1} C:{2}".format(a,b,c))

#using c programming syntax:
print("A:%d B:%d C:%d" %(a,b,c))
