def function1(lst1,x,y): #that function takes one list and two parameters
    length1=len(lst1) # I take the length of list and put to the length1 variable
    if length1%2==0: # I checked the lists length is it even number or odd number and if it is even, do statements
        size=length1//2 # to slice list from middle
        firstpart=lst1[0:size] # I upload  between beginning and middle elements of list to firstpart
        lastpart=lst1[size:] # I upload between middle and last elements of list to lastpart
        middlepart=[x]*y #created new middle part
        newlst1=firstpart+middlepart # I added firstpart and newmiddlepart together
        lst1=newlst1+lastpart # I added lastpart to the newlist
        return(lst1)
    else: #if lists number of elements is odd , do the statements
        lst1.extend(y*[x]) 
        return(lst1)

def function2(lst2,num):
    length2=len(lst2) #take the length of list
    if length2==0: # if there is no element return zero
        return 0
    else: # if there is elements in the list do statements
        element1=lst2[0] #take the first element of list and assign element1
        lst2.remove(element1) #delete first element of list
        return (element1*(10**num)**(length2-1)+function2(lst2,num)) #do first elements power of 10 then do it for other elements same operation with using recursion and calling function again
       
lst1=[2,3,4,5]   #create a list
lst1=function1(lst1,9,2) #send to the first function
print(lst1) #print the new list
lst2=function2(lst1,1) #send new list to the second function
print(lst2) # print the new list 
        
