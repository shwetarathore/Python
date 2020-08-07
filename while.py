# i = 1
# while i <= 5:
#     print(' *' * i)
#     i = i + 1
#     # print("Done")
# print("All Done")    


# Guess Game

# secret = 9
# guess_count = 0
# attempts = 3
# while guess_count < attempts:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret:
#         print("You WON!")
#         break
# else:
#     print("You Lost!")    

# Game 2

key = ""
started = False
while True:
   key = input("> ").lower()
   if key == "help":
     print(""" 
start - to start the car
stop - to stop the car
quit - to exit
      """)
   elif key == "start":
       if started:
           print("Already started!")
       else:
           started = True   
           print("Car started...Ready to go!")
   elif key == "stop":
       if not started:
           print("Already stopped!")
       else:
           started = False   
           print("Car stopped...!")
   elif key == "quit":
       break
   else:
       print("Sorry, Didn't get you!")
    # break



