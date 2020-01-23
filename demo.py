req=int(input("Enter the number of candies required by the user:"))
avl=int(input("Enter the number of candies available in the vending machine:"))
i=0
while i<req:
  if i>avl:
      print("Stock Out!!!")
      print("Have a nice Day!!!")
      break
  else:
    print("Candy!!!")
  i+=1
print("Bye Pythonists..!!Nice meeting You!!!") 
