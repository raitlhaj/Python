
import  random



def RemoveDuplicateInAList(liste):
    liste2=[]
    for item in liste:
        if(item not in liste2):
            liste2.append(item)
  
    return liste2   
    
def IsPrime(n):
    for i in range(2,n-1,1):
        if(n%i==0):
            return False
        return True
    
def LargestNumebr(liste):
    max=0
    for item in liste:
        if(max<item):
            max=item
    return max

def SumListe(liste):
    s=0
    for i in liste:
        s=s+i
        
    return s

def ShowMatrix(matrix):
    for row in matrix:
        for s in row:
            print(s)
            
def SortTbl(liste):
    for s in liste:
        s
        
def ConvertPhoneNumber(phoneNumber):
    
    dictPhone ={ # dictionnnary 
        1:"One",
        2:"Two",
        3:"Tree",
        4:"Four",
        5:"Five"
    }

    for num in phoneNumber:
       print(dictPhone[int(num)])  # print(dictPhone.get(int(num),"!")) 
       
def AgeToInt(number):
    try:
       age=int(input("Age : ? "))
       return age
    except ValueError:
        print("Exception !")
    except ZeroDivisionError:
        print("Dividing by zero !")


def SortmyTbl(liste,low,high):
    
    if(low<high):
        pi=partitionner(liste, low, high)
        SortmyTbl(liste,low, pi-1)
        SortmyTbl(liste, pi+1,high)
        
def partitionner(liste,low,high):
    pivot=liste[high]
    i=low-1
    
    for j in range(low,high):
        if(liste[j]<pivot):
            i=i+1
            tmp=liste[i]
            liste[i]=liste[j]
            liste[j]=tmp
    
    tmp=liste[i+1]
    liste[i+1]=liste[high]
    liste[high]=tmp 
    
    return i+1


def sortto(liste):
    
    for i in range(len(liste)-1):
        if(liste[i]>liste[i+1]):
            tmp=liste[i]
            liste[i]=liste[i+1]
            liste[i+1]=tmp
            i=0
            
    return liste

        
        

        
#init
matrix=[
    [1,2,4],
    [3,3,4],
    [3,3,4]]
liste=[10,2,3,4,4,3,34,5,89,22] # Append, sort, reverse, remove, insert
numberTpl=(1,2,4,3)  # Only Count and Index
x,y,z,y=numberTpl

dict ={ # dictionnnary 
    "name":"John",
   "Email":"ait@gmail.com",
    "Age":26,
    'isM':True
}



message="Hello world!, everything is ok."

print(message.split(' ')) # donne une liste des mots splités par espace

#Calls
print(ShowMatrix(matrix))
print(IsPrime(6))
print('Max '+str(LargestNumebr([10,34,5,89,22])))
print('Sum:'+str(SumListe([10,34,5,89,22])))
print('RemoveDuplicate in a list:'+str(RemoveDuplicateInAList(liste)))

print(dict['Age'])
print(dict.get('Birthday','01-01-2022'))

phone="34432"#input("Your phone ?:")
ConvertPhoneNumber(phone)

print("my liste: ")
liste=[3,4,1,5,2]
for item in liste:
    print(item)
    
print("QuickSorte result: ")
SortmyTbl(liste,0,4)

for item in liste:
    print(item)
liste=[3,4,1,5,2]    
print("Sortto result: ")
sortto(liste)

for item in liste:
    print(item)
