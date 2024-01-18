#Imported Ctypes to get a static array (referential array tho)
#Refrential array is basically independent of the type of elements stored in array it stores the reference of the variable
import ctypes

#Mylist class to make our own created Dynamic array
class mylist:

    #Constructor to create empty array
    def __init__(self):
        self.size = 1
        self.n = 0
        #special function to get static array of size 
        self.A = self.__make__array(self.size)

    #Ctype library helped us here
    def __make__array(self,size):
        return (size*ctypes.py_object)()

    #To tell how many elements in the list yet
    def __len__(self):
        return self.n
    
    #To print our object it converts our whole object into a string format to later put it on our stream
    def __str__(self):
        s = ""
        for i in range(self.n):
            s += str(self.A[i])
            s += ","
        
        s = "[" + s[0:-1] + "]"
        return s
    
    #To delete item from an index
    def __delitem__(self,index):

        for i in range(0,self.n-1):
            if(i >= index):
                a = i+1
            else:
                a = i

            self.A[i] = self.A[a]
        
        self.n -= 1

            
    #This is to subscript our array and have index function working (it is called when you try "A[10]" or anything likewise)
    def __getitem__(self,index):
        if( self.n <= index or index <= -(self.n)):
            return "IndexError - Index is out of range :( "
        return self.A[index]
    
    #To add another element in the end of the array
    def append(self,ele):
        if(self.size == self.n):
            self.A = self.__resize(self.size)
        
        self.A[self.n] = ele
        self.n += 1

    #To add another element in between of list you need the index and val for it
    def insert(self,index,val):
        if(index > self.n):
            index = self.n
        
        B = self.__make__array(self.n+1)
        b = -1
        for i in range(self.n+1):
            if(i == index):
                B[i] = val
            else:
                b+=1
                B[i] = self.A[b]
        
        self.A = B
        self.size += 1
        self.n += 1
        return None

    #To pop the last element or element at the index if provided
    def pop(self,index = 0):
        if (self.n == 0):
            print("EmptyListError : No item in list to pop ")
            return 
        else:
            if (index != 0):
                for i in range(0,self.n-1):
                    if(i >= index):
                        a = i+1
                    else:
                        a = i

                    self.A[i] = self.A[a]
            else:
                pass

        self.n -= 1

    #To find where the value is stored in array returns the index point
    def index(self,val):
        for i in range(0,self.n):
            if(self.A[i] == val):
                return i
        return f"ValueError : No value in the list matching \"{val}\""

    #to remove the array using value
    def remove(self,val):
        for i in range(self.n):
            if(self.A[i] == val):
                self.__delitem__(i)
                return
            
        return None
    
    #Our special function that makes the static array dynamic that resizes the whole array and copies it to new one with new size and returns it to orginal array
    def __resize(self,size):
    
        B = self.__make__array(size+2)
        self.size = size+2
        for i in range(self.n):
            B[i] = self.A[i]
        
        return B
            
        
l = mylist()
l.append(1)
l.append(2)
l.append(3)
l.insert(2,100)
print(l)
l.append(4)
l.insert(2,"HEy")
del l[5]
print(l)









#Dynamic Array is nothing but a static array with no fixed memory size and how we do it is a basic concept
#We just copy the old array let's a[4] which wants to add a 5th element so we will create a new static array
#like b[8] and then copy all the items from "a" array and then return the list with 5 elements and continuing 
#to do so as much as required.

#Dynamic Array is what List is in Python 