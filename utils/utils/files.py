def createFile(name):
 assert len(name)!=0

 file=open(name+".txt","w")
 file.write("Hi "+name)
 file.close()


def myfunc():

    assert 5==5,'SomethingWrongWithEntries'

    myfile=open("matlab.txt",'r')
    vo=myfile.read()
    print(vo)

    myfile.close()





def decor(fu):
    def test():
        print("HHHHHHHHHHHHHHHHHHHHHHHHHH")
        fu()
        print("__________________________")
    return test

def funct():
        print("htg")

y=decor(funct)
y()     


def fib(x):
      if x == 0 or x == 1:
               return 1
      else: 
               return fib(x-1) + fib(x-2)
print(fib(4))
