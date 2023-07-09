f1=open("/content/sample_data/student.csv","r") 
f2=open("/content/sample_data/placement.csv","r") 
f3=open("/content/sample_data/stud_placement.csv","w")
contents1=f1.read()
contents2=f2.read()
print(contents1) 
print(contents2) 
nm=[]
package=[] 
lines1=contents1.split("\n") 
lines2=contents2.split("\n") 
lines1.pop()
lines2.pop()
for l1 in lines1: 
    words1=l1.split(",") 
for l2 in lines2:
  words2=l2.split(",") 
if(words1[0] == words2[0]):
 l1 = l1 + "," + words2[1] + "," + words2[2] + "\n"
f3.write(l1)
nm.append(words1[1]) 
package.append(int(words2[2]))
print(l1)
f1.close() 
f2.close() 
f3.close()
 #Code2
f=open("/content/sample_data/stud_placement.csv","r") 
contents=f.read()
lines=contents.split("\n")
lines.pop()
sid=[]; nm=[]; company=[]; package=[];
for l in lines: words=l.split(",") 
print(words) 
sid.append(int(words[0])) 
nm.append(words[1]) 
company.append(words[2]) 
package.append(int(words[3]))
print("\nStudent IDs",sid) 
print("Student Names",nm) 
print("Student Company",company) 
print("Student Package",package)
#Max Package
print("\nMaximum Package :",max(package)) #Min Package
print("Minimum Package :",min(package)) #Average Package
print("Average Package :",sum(package)/len(package)) #Total Package
print("Total Package :",sum(package))
#Student whose package is max
print("\nStudent name whose package is maximum : ",nm[package.index(max(package))])
#Student whose company is Google
print("Student name whose company is Google : ",end=",") 
for i in range(len(company)):
 if company[i]=="Google": print(nm[i],end=" ")
#Student whose package is 2400000
print("\nStudent name whose package is 2400000 : ",nm[package.index(2400000)])
#Student whose package is min
print("Student name whose package is minimum : ",nm[package.index(min(package))])

 #Student whose company is Microsoft
print("Student name whose company is Microsoft : ",end=",")
for i in range(len(company)):
 if company[i]=="Microsoft": print(nm[i],end=" ")
f=0
#Student whose package is 2000000 for i in range(len(package)):
if package[i]==2000000:
 print("\nStudent name whose package is 2000000 : ",nm[i]) 
f=1
if(f==0):
 print("No any Student present whose package is 2000000")

 