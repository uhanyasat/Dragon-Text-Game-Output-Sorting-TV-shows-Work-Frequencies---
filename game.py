
#Created instructions for Player
def show_instructions():  
   #print a main menu and the commands
   print("*********Dragon Text Adventure Game*************")
   print("---->Collect 4 items to win the game, or be eaten by the dragon.")
   print("Move commands: South, North, East, West")
   print("Add to Inventory: type get ")

show_instructions()

#Created Blueprint for Game Area and Rewards
rooms = {
   'Great Hall' : { 'South' : 'Bedroom', 'North': 'Dungeon', 'East' : 'Kitchen', 'West' : 'Library' },
   'Bedroom' : { 'North' : 'Great Hall', 'East' : 'Cellar'},
   'Cellar' : { 'West' : 'Bedroom', 'item' : 'Helmet' },
   'Kitchen' :{'North' :'Dining Room' ,'West' :'Great Hall','item' : 'Knife'},
   'Library' :{'East' : 'Great Hall','item' : 'Gun'},
   'Dungeon': {'South':'Great Hall','item':'Sword'},
   'Dining Room' : { 'South' : 'Kitchen', 'item' : 'Dragon' } #villain
}

#Created Random Player Position
import random
position=random.randint(1,6)

if position==1:
    Player='Great Hall'
elif position==2:
    Player='Bedroom'
elif position==3:
    Player='Cellar'
elif position==4:
    Player='Library'
elif position==5:
    Player='Dungeon'
elif position==6:
    Player='Kitchen'

#initialising Inventory
Inventory=[]
i=0
#Game will run untill win or loose
while i<=1000:
    print('You are in the {0}'.format(Player))
    print(Inventory)
    
    Room_details=rooms[Player]#Details about room,In which Player has been Entered
    if 'item' in Room_details:
        print('You see a {0}'.format(Room_details['item']))
        if Room_details['item']=='Dragon':#check Dragon
            print('''   NOM NOM...GAME OVER!''')
            print('''Thanks for playing the game. Hope you enjoyed it. ''')
            break
        if Room_details['item'] not in Inventory:#Check for Inventory
            print('Enter your action:')
            Action=input()#Action about Inventory 
            if Action=='get':
                Inventory.append(Room_details['item'])
            else:
                Inventory=Inventory
    if len(Inventory)==4:#Check Maximum Invertory is completed
        print('''Congratulations! You have collected all items and defeated the dragon!''')
        print('''Thanks for playing the game. Hope you enjoyed it''')
        break
    print('Enter your Move:')
    Move=input()
    if Move in Room_details:# Check valid Move
        Player=Room_details[Move]
    else:
        print('Try another Move')
    i=i+1

            