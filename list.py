lst=[10,-1,-25,30]
#div_by_five =[]
#for itr in range(len(lst)):
    #if (lst[itr])<0:
        #div_by_five.append(lst[itr])
#print(div_by_five)

div_by_five=[itr for  itr in lst if itr<0]
print(div_by_five)
