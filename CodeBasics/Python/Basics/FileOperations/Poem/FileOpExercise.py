fr=open("D:\\Documents and Settings\\Kaushik Dayabar\\Documents\\datascience\\FileOperations\\poem.txt","r")

l=fr.read().replace("\n"," ").split(" ")
fr.close()

res,max1={},0
for i in l:
    if i in res:
        res[i]+=1
        if max1<res[i]:
            max1=res[i]
    else:
        res[i]=1


for k in res.keys():
    if res[k]==max1:
        print(k,res[k])
print(res) 




