#string

#str1="my name is somya yaduvanshi.\n my collage id is 22cs077"
#print(str1)

#str1="my name is somya yaduvanshi.\t my collage id is 22cs077"
#print(str1) 
 
#str1="somya"
#str2="yaduvanshi"
#print("my name is",str1+str2)

#str1="somya"
#len1=len(str1)
#print(len1)
#str2="yaduvanshi"
#len2=len(str2)
#print(len2)
#print("total length=",len1+len2)

#str="somya yaduvanshi"
#ch=str[12]
#print(ch)

#str="somya yaduvanshi"
#print(str[3:9])

#str="my name is somya yaduvanshi"
#print(str.endswith("anshi"))
                  
#str="my name is somya yaduvanshi"
#str=str.capitalize()
#print(str)

#str="my name is somya yaduvanshi"
#print(str.replace("somya","honey"))

#str="my name is somya yaduvanshi"
#print(str.find("s"))

#str="my name is somya yaduvanshi"
#print(str.count("s"))

#a=input("enter your name:")
#print(a)
#len=len(a)
#print(len)

#str=" hii my name is $ and i love $"
#print(str.count("$"))

                                            #coditional statement
                                            #if,elif,else(syntax)

                                            #trafic light signal

#signal="yellow"
#if(signal=="green"):
 #   print("go")
#elif(signal=="yellow"):
 #   print("slow")
#elif(signal=="red"):
 #   print("stop")
#else:
 # print("the signal have some problem you will go slowly")

                                               #marks sheet of school 

#marks=input("enter the marks:")
#print("total marks=",marks)
#if(marks>="90"):
 #   print("grade A")
#elif((marks>="80") and (marks<="90")):
 #   print("grade B")
#elif((marks>="70") and (marks<="80")):
 #   print("grade C")
#elif((marks>="60" and (marks<="70"))):
 #   print("grade D")
#else:
 #   print("The Student Are Fail")

                                              # even odd number

#num=24
#rem= num % 2
#if(rem == 0):
 #    print(" even")
#else:
 #   print(" odd")    

                                            #greaterthen lessthen

#a=input("enter the value of a:")
#b=input("enter the value of b:")
#c=input("enter the value of c:")
#print("value of =",a,b,c)
#if((a>b) and (a>c)):
 #   print("a is greater")
#elif((b>a) and (b>c)):
 #   print("b is greater")
#elif((c>a) and (c>b)):
  #  print("c is greater")
#else:
  #  print("the all value are same or equal")     

                                             #multiple of 5

#x=int(input("enter the number:"))

#if(x % 5 == 0):
 #   print("it is multiple of 5")    
#else:
 #   print("it is not a multiple of 5")     
 
                                # list method      
#list=[3,2,4]
#list.append(5)
#print(list)  
 
#list=[3,2,4]
#list.sort()
#print(list)                          

#list=[3,2,4]
#list.sort(reverse=True)
#print(list)                            

#list=[3,2,4]
#list.reverse()
#print(list)  

#list=[3,2,4]
#list.insert(1,6)
#print(list)

#list=[3,2,4]
#list.remove(2)
#print(list)

#list=[3,2,4]
#list.pop(0)
#print(list)

                    # tuples 

#tup=(3,8,9,6,5)
#print(tup[4])
#print(tup[2])

#tup=(3,8,9,6,5)
#print(tup.index(1))


#movie=[]
#mov1=input("enter the first movie name=")
#mov2=input("enter the second movie name=")
#mov3=input("enter the third movie name=")
 
#movie.append(mov1)
#movie.append(mov2)
#movie.append(mov3)
#print(movie)

#list=[1,2,3,2,1]
#list.copy()
#print(list)
#list.reverse()
#print(list)
#if(list.copy=list.reverse):
#    print(match)
#else:
#    print(not match)

#tup=(1,2,3,4,3,2,1,1,1)
#print(tup.count(1))

#list=["b","h","a","c","b"]
#list.sort()
#print(list)

                                   #dictiona

#info={
 #     "name" : "somya" ,
  #    "age":"20",
   #   "id":"22cs077",
    #    }
#print(info)
                            
                            # set

#collection={1,2,3,4,5,6}
#print(collection)
 
#set={1,2,3,4,5,6}
#set.add(7)
#print(set)
 
#set={1,2,3,4,5,6}
#set.remove(4)
#print(set)

#set={1,2,3,4,5,6}
#set.clear()
#print(set)

#set={1,2,3,4,5,6}
#set.pop()
#print(set)

#set1={1,2,3,4}
#set2={3,4,5,6}
#print(set1.union(set2))

#set1={1,2,3,4}
#set2={3,4,5,6}
#print(set1.intersection(set2))

#collection={
#"table":"a peice of furniture","list of facts and figurs"
#"cat":"a small animal",
#}
#print(collection)

#set={"python","jawa","c","c","python","c","c"}
#print(set)
#print(len(set))

                                        #loop (while/for loop)

#count=1
#while count<=5:
#  print("hellow world")
#  count+=1

#i=1
#while i<=100:
#  print(i)
 # i+=1

#i=100
#while i>=1:
 # print(i)
  #i-=1

#n=int(input("enter the no="))
#i=1
#while i<=10:
# print(n*i)
#i+=1

#nums=[1,2,34,56,78,89,54,34,65,74,85,69]
#idx=0
#while idx<len(nums):
#  print(nums[idx])
# idx+=1

#nums=(1,2,34,56,78,89,54,34,65,74,85,69)##
#x=5
#i=0
#while i<len(nums):
#if(nums[i]==x):
 #    print("found at index",i)
 # i+=1

#i=1
#while i<=5:
# print(i)
# if(i ==3):
#   break
# i+=1

#i=1
#while i<=5:
#  if(i==3):
#   i+=1
#   continue
# print(i)
# i+=1

#nums=[1,2,3,4,5,6,7]
#for val in nums:
# print(val)
  

#nums=[1,2,3,4,5,6,7]
#for val in nums:
#print(val)
#else:
# print("end")
  
#nums=[1,23,43,54,6,24,35,7,68,28,64]
#for val in nums:
# print(val)

#nums=[1,23,43,54,6,24,35,7,68,28,64,23]
#X=23
#idx=0
#for val in nums:
#  if(val==X ):
#   print("found the no on idx",idx)
#    idx+=1
  #print(val)

#seq=range(20)
#for i in seq :
# print(i)

#for i in range(10):#(stop)
#  print(i)

#for i in range(2,10):#(start,stop)
#  print(i)

#for i in range(2,10,2):#(start,stop,step)
# print(i)

#for i in range(1,101):#(stop)
# print(i)

#for i in range(100,0,-1):#(stop)
#  print(i)

#n=int(input("enter the number="))
#for i in range (1,11):
# print(n*i)

#for i in range(10):
#  pass 
#print("some useful work")

#n=5
#sum=0
#or i in range(1,n+1):
# sum+=i
# print("total no of sum=",sum)

#n=5
#fact=1
#for i in range(1,n+1):
# fact*=i
# print("total no of fact=",fact)

#def calc_sum(a,b):
#   sum= a+b 
#   print(sum)
#    return sum
#calc_sum(3,4)
#calc_sum(5,6)
#calc_sum(1,2)

#def calc_avg(a,b,c):
 #sum=a+b+c
 #avg=sum/3
 #print(avg)
#calc_avg(1,2,3)

#cities=["jaipur","delhi","goa","manali","punjab"]
#heroes=["saktiman","srk","ssr"]
#def print_len(list):
#    print (len(list))
#print_len(heroes)
#print_len(cities)  

#cities=["jaipur","delhi","goa","manali","punjab"]
#heroes=["saktiman","srk","ssr"]
#def print_len(list):
#    print (len(list))
#print_len(heroes)
#print_len(cities) 
#def print_list(list):
#   for item in list:
#    print(item,end=" ")
#print_list(heroes)
#print_list(cities)

#def cal_fact(n):
# fact=1
# for i in range(1,n+1): 
#     fact*=i
# print(fact)
#cal_fact(5)

#def converter(usd_val):
#  inr_val=usd_val*83
#  print(usd_val,"USD=",inr_val,"INR")
#converter(100)

#def show(n):
#  if (n==0):
#   return 
#  print(n)
#  show(n-1)
#show(5)

