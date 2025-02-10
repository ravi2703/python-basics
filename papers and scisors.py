'''a = 2
print(type(a))

a = "hello"
print(type(a))

a = 1.9
print(type(a))
a = 1
while a < 6:
    print(a)
    a += 1'''

'''def motor(name, color):
  bike_name = name
  color_bike = color
  print(f"the bike name is {bike_name} and color is {color_bike}")
  if bike_name == "yamaha":
    print(f"{bike_name} price is 90 ")
  elif bike_name == "kawasaki":
    print(f"{bike_name} price is 100 ")
  else:
      print(f"you have choosen wrong option")
motor("yamaha", "blue")      
motor("kawasaki", "yellow")'''

'''n = float(input("enter a number: "))
if n % 2 ==0:
  print("weird and even")
elif n % 2 !=0:
  print("wierd and odd")
elif n in range(6,21):
  print("not weird")
else:
  print("none")'''
  
rock = '''
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

scisors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

paper = '''
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''
import random  
game_images = [rock, paper, scisors]

user_input = int(input("choose a number: 0 for rock, 1 for paper, 2 scisors"))
if user_input >= 0 and user_input <=2:
  print(game_images[user_input])

computer_choice = random.randint(0, 2)
print(f"comouter choice id {computer_choice}")
print(game_images[computer_choice])

if user_input >= 3 or user_input < 0:
  print("invalid number")
elif user_input == 0 and computer_choice == 2:
  print("you won")
elif user_input > computer_choice:
  print("you won")
elif user_input < computer_choice:
  print("you lose")
elif user_input == computer_choice:
  print("print draw")
