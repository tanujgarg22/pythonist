
# add all element in list 
"""
def sum_list():
    list1=[1,2,3,4,5,-6]
    total=sum(list1)
    return total

total1=sum_list()
print(total1)

#add numbers in mixed list fast way
def sum_mixedlist():
    list1=[1,2,3,"apple",4,"cat",60]
    total=sum([element for element in list1 if isinstance(element,int) ])
    print(total)
    return total

total1=sum_mixedlist()
print(total1)
"""
"""
def find_largest():
    list1=[4555,678,45677,24526,64,6]
    max_num=max(list1)
    return max_num

def find_largest():
    list1=[4555,"Tanuj",678,45677,"hello",24526,"hi",64,6]
    max_num=max(element for element in list1 if isinstance(element,int))
    return max_num

print(find_largest())
"""

# remove duplicate in the list 
"""
def remove_dups():
    list1=[1,22,22,33,44,33,5,6,9,9]
    unique_list=[]
    for item in list1:
        if item not in unique_list:
            unique_list.append(item)
            # if I give append([item]) item in sq bracket ,
            #  that will reurn nested list 
            # other ways inbuilt function like list(set(mu_list))
            #dict.fromkeys(list(my_list))

    return unique_list
print(remove_dups())
"""
#check for duplicate in ist and return true or false 
"""
def check_dup():
    list1=[1,2,3,4]
   # return len(list1)>len(list(set(list1)))
   #the shortest way , above one
    
    list2=[]
    for item in list1:
        if item not in list2:
            list2.append(item)
    if len(list2)<len(list1):
        print("duplicate in original list ")
        return True
    else:
        print("no dups")
        return False

    #if not list2:
    #   means list is empty
     #   return True
    #else:
     #   return False
     
print(check_dup())
"""
"""
def check_dup_fast_exit():
    list1=[1,2,2,3,4,5,6]
    list2=[]
    #use set for speed - it keeps in memory , hashable values
    for k in list1:
        if k in list2:
            return True
        list2.append(k)
    return False

print(check_dup_fast_exit())
"""

"""
def reverse_list():
    list1=[1,2,3,4,5,6,7]
    list2=list1.copy()
    length=len(list1)
    for i,k in enumerate(list1):
        #for i in rane(length):
        index=(length-1)-i
        print(f" index is {index} list2[{index}] is {list2[index]} and list1[{i}] is {list1[i]}")
        list2[index]=list1[i]

    return list2

print(reverse_list())
"""
"""
def count_evenodd():
    list1=[2,4,6,8,3,5,7,9,22,44,55]
    set1=()
    #set1=[]
    counteven=0
    countodd=0
    for k in list1:
        if (k%2):
            counteven += 1
        else:
            countodd += 1
    set1 = set1 + (counteven,)
    set1 = set1 + (countodd,)
    #set1.append(counteven)
    #set1.append(countodd)
    #my_tuple=tuple(set1)
    #return my_tuple
    return set1

print(count_evenodd())

"""

# brute force- max diff between 2 consecutive elment in list 
"""
def bruteforce():
    list1=[10,20,40,50000,90,100,450,890,1,4]
    diff=0
    for k in range(len(list1)-1):
        value_z=abs(list1[k] - list1[k+1])
       ## for j in range(1,(len(list1))):
          #  value_y=list1[j]
          #  valuez=abs(value_x-value_y)
        print(f"value_x is list1[{k}] and value_y  list1[{k+1}]")
        if value_z>diff:
            diff=value_z

    return diff

print(bruteforce())
"""
"""
def sorted_list():
    list1=[4,3,7,3,7,28,2,89]
    list2=[1,2,3,4,5,43,21]

    list1.sort()
    merge_list=sorted(list1+list2)
    #merge_list=list1+list2
    #merge_list.sort()
    #for k in range(len(list1)):
      #  list2.append(list1[k])
   # list2.sort()
    return merge_list

print(sorted_list())
"""

def circular_list():
    list1=[1,2,3,4,5]
    key=3
    #5,4,3,2,1
    #3,4,5,1,2,
#[3,4,5,1,2]
    def reverselist(listx,start,end):
        while start<end:
            listx[start],listx[end]=listx[end],listx[start]
            start += 1
            end -= 1
        return listx
    result=reverselist(list1,0,len(list1)-1)
    resultx=result.copy()
    partAlist=reverselist(result,0,key-1)
    #print(f"result {result} length {len(list1)}")
    partBlist=reverselist(result,key,len(list1)-1)
    #print (f"part a list {partAlist} part B {len(list1)-1}list {partBlist}")
    #result=partAlist+partBlist
    return partBlist
    #return result

print(circular_list())






