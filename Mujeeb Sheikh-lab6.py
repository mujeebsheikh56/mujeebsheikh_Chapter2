# Question NO 1 part(a)
import time
print("The Formatted Date and time is : ",time.strftime('%A %B %d %Y'))
# (part b)
print(time.strftime('%T  %p %Z on %x'))
# (part c)
print("I will meet you on ",time.strftime('%a %B %d at %x %p'))
print()

# Question No 2: (part a,)
forecast= "It will be a sunny day today"
print ("The number of occurences of string day is: ",forecast.count('day'))
print ("The index where substring sunny starts is:",forecast.index('sunny'))
print (forecast.replace('sunny','cloudy'))
print()
# Question No 3:
def even(n):
    global lst
    lst =[]
    for i in range(2,n):
       if i%2 or i%3:
           lst.append(i)
even(17)
print("The Number divisible by 2 & 3 is:",lst)
print()

# Question No 4:
def mailaddress(first,last,street,city,state,zipcode):
    f=first
    l=last
    st=street
    c=city
    s=state
    zip=zipcode
    print('{}\n{}\n{}\n{}\n{}\n{}\n'.format(f,l,st,c,s,zip))
mailaddress('Mujeeb','Sheikh','Nipa','Karachi','Pakistan','3150')









