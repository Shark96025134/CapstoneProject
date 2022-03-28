import datetime


#print("TO - DO List")
print("My List")
k = 0
arr = {
}   
a = str(input("::"))
class A:
    
#B
    
         def B():
                  a = str(input("::"))

#additem            

         if a == "/additem":
             b = input("Enter the item you would like to add :: ") 
             k = str(k+1)
             n = "item {}"
             u = n.format(k)
             arr[u] = b
             print (arr) 
             c = input("would you like to add any other item?")
             while c == "yes":
                 b = input("Enter the item you would like to add :: ") 
                 k = str(input("Enter name :"))
                 n = "item {}"
                 u = n.format(k)
                 arr[u] = b
                 print (arr) 
                 c = input("would you like to add any other item?")
                 if c == "no":
                      u1 = datetime.datetime.now()
                      print(u1)
                      x = arr.items()
                      print(x)
                      a = str(input("::"))
                 
#deleteitem            

         if a == "/deleteitem":
             print(arr)
             e = input("Enter which Item you would like to delete :")
             f = input("Are you sure?")
             if f == "yes":
                 arr.pop(e)
                 print(arr)
                 a = str(input("::"))
             if f == "no":
                 a = str(input("::"))

#update

         if a == "/update":
             print (arr.items())
             j = input("Enter the keyname here: ")
             p = input("Enter the new item: ")
             arr.update({j: p})
             print(arr)
             a = str(input("::"))

#getitem         

         if a == "/getitem":
             print (arr.items())
             q = input("Enter the keyname: ")
             _ = arr.get(q)
             print(_)
             a = str(input("::"))

#display

         if a == "/display":
             print (arr.items())
             a = str(input("::"))

#clearlist

         if a == "/clearlist":
             d = input("are you sure you want to clear the list? ::")
             if d == "yes":
                arr.clear()
                B()
                a = str(input("::"))
             if d == "no":
                 B()
                 a = str(input("::"))
                 
#exit

         if a == "/exit":
             a = str(input("::")) 
