#January 16, 2017#
#Aneesh Patel#
#Text Adventure Game#

#Imports Random#
import random

#Introduction to Game#
print("Welcome to a Dungeon text adventure game! You are starting along the top right corner of the dungeon wall. To exit, you must defeat all the monsters, which requires finding swords, and then you must defeat the Boss Monster, which requires a sword and magic stones. You will start in the top right corner of the dungeon. Good Luck!")

#Starts off with nothing in the pocket#
pocket=[]

#Layout of the dungeon floor#
floor3=[" down stairs ", " a monster ", " nothing ", " a sword ", " start "]
floor2=[" up stairs ", " a sword ", " nothing ", " a monster ", " down stairs "]
floor1=[" up stairs ", " a prize and an exit ", " a boss monster ", " magic stones ", " a sword"]

floor=[floor3, floor2, floor1]

#Current Position Variables#
win=False
gameEnd=False
user_room=4
user_floor=floor[0]
f=0


#Function that lets you run away from boss 40% of the time#
def runBoss():
    global gameEnd
    randrange=random.randint(1,10)
    if randrange<=4:
        print("You barely escaped the monster.")
    elif randrange>4:
        print("You could not run past the monster, and died! Game Over!")
        gameEnd=True

while win!=True and gameEnd!=True:       
    direction=input("Do you want to go left, right, up or down? (You can only go up or down when you see stairs)")
    #If they want to go down#
    if direction == "down":
        #If the user is not in a room with stairs#
        if user_floor[user_room]!=" down stairs ":
            print("You can't go downstairs, because there are no stairs!")
        #If the user is in a room with stairs#
        else:
            #Goes down 1 floor#
            user_floor=floor[f+1]
            f+=1
            print("You see" + user_floor[user_room])
            #After they go downstairs, if they see a sword#
            if user_floor[user_room]==" a sword ":
                pickup=input("Would you like to pick up the sword?")
                if pickup=="yes" or pickup=="Yes":
                    #Pick up sword if they see it and want to pick it up#
                    pocket.append("sword")
                    user_floor[user_room]=" nothing "
                    print("You have picked up the sword.")
                else:
                    print("You have left the sword on the ground.")
            #After they go downstairs, if they see magic stones#
            if user_floor[user_room]==" magic stones ":
                pickup=input("Would you like to pick up the magic stones?")
                if pickup=="yes" or pickup=="Yes":
                    #Pick up magic stones if they see them and want them#
                    pocket.append("magic stones")
                    user_floor[user_room]=" nothing "
                    print("You have picked the magic stones.")
                else:
                    print("You have left the magic stones on the ground")
                #After they go downstairs, if they see a monster#
            if user_floor[user_room]==" a monster ":
                #If they see a monster and they have a sword#
                if "sword" in pocket:
                    print("You have fought and successfully defeated the monster, but unfortunately have lost your sword in the process.")
                    #If they kill the monster, transform the room into having nothing#
                    user_floor[user_room]=" nothing "
                    pocket.remove("sword")
                else:
                    #If they dont have a sword, then they have a 40% chance of running away successfully#
                    print("You do not have a sword, and therefore have a 40% chance of running away successfully from the monster")
                    runBoss()
            if user_floor[user_room]==" a boss monster ":
                #If they see the boss monster and have a sword and magic stones in their pocket#
                if "sword" in pocket and "magic stones" in pocket:
                    print("You have fought and successfully defeated the boss monster, but unfortunately have lost your sword and magic stones in the process.")
                    #After they defeat the boss monster, transform the room into having nothing#
                    user_floor[user_room]=" nothing "
                    pocket.remove("sword")
                    pocket.remove("magic stones")
                else:
                    print("You are missing at least one of the required items to defeat the boss monster (a sword and magic stones), and therefore have a 40% chance of running away successfully.")
                    #If not, they have a 40% chance of running away successfully#
                    runBoss()
    if direction == "left":
        #If they are in the first room, they cannot go left#
        if user_room == 0:
            print("You are at the edge of the dungeon wall.")
        else:
            user_room-=1
            print("You see" + user_floor[user_room])
            #After they go to the left, if they see a sword#
            if user_floor[user_room]==" a sword ":
                pickup=input("Would you like to pick up the sword?")
                if pickup=="yes" or pickup=="Yes":
                    #Pick up sword if they see it and want to pick it up#
                    pocket.append("sword")
                    user_floor[user_room]=" nothing "
                    print("You have picked up the sword.")
                else:
                    print("You have left the sword on the ground.")
            #After they go to the left, if they see magic stones#
            if user_floor[user_room]==" magic stones ":
                pickup=input("Would you like to pick up the magic stones?")
                if pickup=="yes" or pickup=="Yes":
                    #Pick up magic stones if they see them and want them#
                    pocket.append("magic stones")
                    user_floor[user_room]=" nothing "
                    print("You have picked the magic stones.")
                else:
                    print("You have left the magic stones on the ground")
                #After they go to the left, if they see a monster#
            if user_floor[user_room]==" a monster ":
                #If they see a monster and they have a sword#
                if "sword" in pocket:
                    print("You have fought and successfully defeated the monster, but unfortunately have lost your sword in the process.")
                    #If they kill the monster, transform the room into having nothing#
                    user_floor[user_room]=" nothing "
                    pocket.remove("sword")
                else:
                    #If they dont have a sword, then they have a 40% chance of running away successfully#
                    print("You do not have a sword, and therefore have a 40% chance of running away successfully from the monster")
                    runBoss()
            if user_floor[user_room]==" a boss monster ":
                #If they see the boss monster and have a sword and magic stones in their pocket#
                if "sword" in pocket and "magic stones" in pocket:
                    print("You have fought and successfully defeated the boss monster, but unfortunately have lost your sword and magic stones in the process.")
                    #After they defeat the boss monster, transform the room into having nothing#
                    user_floor[user_room]=" nothing "
                    pocket.remove("sword")
                    pocket.remove("magic stones")
                else:
                    print("You are missing at least one of the required items to defeat the boss monster (a sword and magic stones), and therefore have a 40% chance of running away successfully.")
                    #If not, they have a 40% chance of running away successfully#
                    runBoss()
    if direction == "up":
        if user_floor==3:
            print("You are on the top floor of the dungeon, you can't go any higher.")
        elif user_floor[user_room]==" up stairs ":
            user_floor=floor[f-1]
            f-=1
            print("You see" + user_floor[user_room])
            #After they go upstairs, if they see a sword#
            if user_floor[user_room]==" a sword ":
                pickup=input("Would you like to pick up the sword?")
                if pickup=="yes" or pickup=="Yes":
                    #Pick up sword if they see it and want to pick it up#
                    pocket.append("sword")
                    user_floor[user_room]=" nothing "
                    print("You have picked up the sword.")
                else:
                    print("You have left the sword on the ground.")
            #After they go upstairs, if they see magic stones#
            if user_floor[user_room]==" magic stones ":
                pickup=input("Would you like to pick up the magic stones?")
                if pickup=="yes" or pickup=="Yes":
                    #Pick up magic stones if they see them and want them#
                    pocket.append("magic stones")
                    user_floor[user_room]=" nothing "
                    print("You have picked the magic stones.")
                else:
                    print("You have left the magic stones on the ground")
                #After they go upstairs, if they see a monster#
            if user_floor[user_room]==" a monster ":
                #If they see a monster and they have a sword#
                if "sword" in pocket:
                    print("You have fought and successfully defeated the monster, but unfortunately have lost your sword in the process.")
                    #If they kill the monster, transform the room into having nothing#
                    user_floor[user_room]=" nothing "
                    pocket.remove("sword")
                else:
                    #If they dont have a sword, then they have a 40% chance of running away successfully#
                    print("You do not have a sword, and therefore have a 40% chance of running away successfully from the monster")
                    runBoss()
            if user_floor[user_room]==" a boss monster ":
                #If they see the boss monster and have a sword and magic stones in their pocket#
                if "sword" in pocket and "magic stones" in pocket:
                    print("You have fought and successfully defeated the boss monster, but unfortunately have lost your sword and magic stones in the process.")
                    #After they defeat the boss monster, transform the room into having nothing#
                    user_floor[user_room]=" nothing "
                    pocket.remove("sword")
                    pocket.remove("magic stones")
                else:
                    print("You are missing at least one of the required items to defeat the boss monster (a sword and magic stones), and therefore have a 40% chance of running away successfully.")
                    #If not, they have a 40% chance of running away successfully#
                    runBoss()
        else:
            print("You can't go up, because there are no stairs!")
    if direction == "right":
        if user_room == 4:
            print("You are at the edge of the dungeon wall.")
        else:
            user_room+=1
            print("You see" + user_floor[user_room])
            #After they go to the right, if they see a sword#
            if user_floor[user_room]==" a sword ":
                pickup=input("Would you like to pick up the sword?")
                if pickup=="yes" or pickup=="Yes":
                    #Pick up sword if they see it and want to pick it up#
                    pocket.append("sword")
                    user_floor[user_room]=" nothing "
                    print("You have picked up the sword.")
                else:
                    print("You have left the sword on the ground.")
            #After they go to the right, if they see magic stones#
            if user_floor[user_room]==" magic stones ":
                pickup=input("Would you like to pick up the magic stones?")
                if pickup=="yes" or pickup=="Yes":
                    #Pick up magic stones if they see them and want them#
                    pocket.append("magic stones")
                    user_floor[user_room]=" nothing "
                    print("You have picked the magic stones.")
                else:
                    print("You have left the magic stones on the ground")
                #After they go to the right, if they see a monster#
            if user_floor[user_room]==" a monster ":
                #If they see a monster and they have a sword#
                if "sword" in pocket:
                    print("You have fought and successfully defeated the monster, but unfortunately have lost your sword in the process.")
                    #If they kill the monster, transform the room into having nothing#
                    user_floor[user_room]=" nothing "
                    pocket.remove("sword")
                else:
                    #If they dont have a sword, then they have a 40% chance of running away successfully#
                    print("You do not have a sword, and therefore have a 40% chance of running away successfully from the monster")
                    runBoss()
            if user_floor[user_room]==" a boss monster ":
                #If they see the boss monster and have a sword and magic stones in their pocket#
                if "sword" in pocket and "magic stones" in pocket:
                    print("You have fought and successfully defeated the boss monster, but unfortunately have lost your sword and magic stones in the process.")
                    #After they defeat the boss monster, transform the room into having nothing#
                    user_floor[user_room]=" nothing "
                    pocket.remove("sword")
                    pocket.remove("magic stones")
                else:
                    print("You are missing at least one of the required items to defeat the boss monster (a sword and magic stones), and therefore have a 40% chance of running away successfully.")
                    #If not, they have a 40% chance of running away successfully#
                    runBoss()
    if user_floor[user_room]==" a prize and an exit ":
        win=True
    elif direction!="down" and direction!="left" and direction!="up" and direction!="right" and user_floor[user_room-1]!=" a prize and an exit ":
        print("Try Again.")
