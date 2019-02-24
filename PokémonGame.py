import random
attackk=0

class Pokemon(object):
    def __init__(self, name, typea, health, attack_power):
        self.name=name
        self.health=health
        self.typea=typea
        self.attack_power=attack_power

class Water(Pokemon):
    def attack(self,enemy):
        attackk=Pokemon.attack_power
        if enemy.typea=="fire":
            attackk+=10
        if enemy.typea=="grass":
            attackk-=10
        print(attackk)

class Fire(Pokemon):
    def attack(self, enemy):
        attackk=Pokemon.attack_power
        if enemy.typea=="grass":
            attackk+=10
        if enemy.typea=="water":
            attackk-=10
    def growl(self):
        print("Fire Fire")
class Grass(Pokemon):
    def attack(self, enemy):
        attackk=Pokemon.attack_power
        if enemy.typea=="water":
            attackk+=10
        if enemy.typea=="fire":
            attackk-=10
    def growl(self):
        print("CHeep ChheeP")

Bulbasoar=Grass("Bulbasoar","grass",60,40)
Bellsprout=Grass("Belsprout","grass",40,60)
Oddish=Grass("Oddish","grass",50,50)
Charmander=Fire("Charmander","fire",25,70)
Ninetales=Fire("Ninetails","fire",30,50)
Ponyta=Fire("Ponyta","fire",40,60)
Squirtle=Water("Squitle","water",80,20)
Psyduck=Water("Psyduck","water",70,40)
Poliwag=Water("Poliwag","water",50,50)

grasslist=["Bulbasoar","Bellsprout","Oddish"]
firelist=["Charmander","Ninetales","Ponyta"]
waterlist=["Squirtle","Psyduck","Poliwag"]

poke_team=[]
trial=False

def checkInteger(inputt):
    try:
        int(inputt)
        return True
    except ValueError:
        return False

def checkValid(typelist):
    global poke_team
    trial=False
    print(typelist)
    while trial!=True:
        choice=input("\n" + "Which pokemon do you want to pick? Type 1, 2 or 3 (1 for the first one, 2 for the second one, etc.)"+ "\n")
        if checkInteger(choice):
            if int(choice)==1 or int(choice)==2 or int(choice)==3:
                poke_team.append(typelist[int(choice)-1])
                typelist.pop(int(choice)-1)
                trial=True
            else:
                trial=False
                print("Sorry, that is not an acceptable input. Please try again.")
        else:
            trial=False
            print("Sorry, that is not an acceptable input. Please try again.")

checkValid(grasslist)
checkValid(firelist)
checkValid(waterlist)
        
print("Your team is " + str(poke_team))

pokeh=False

while pokeh!=True:
    pokemon_h=input("Which pokemon do you want to start off with?")
    if pokemon_h==poke_team[0] or pokemon_h==poke_team[1] or pokemon_h==poke_team[2]:
        pokeh=True
    else:
        print("\n" + "Sorry, that is not a valid input. Please try again.")

def startPoke(pokemonx):
    global pokemon_hand
    pokelist_team={"Bulbasoar":Bulbasoar,"Bellsprout":Bulbasoar,"Oddish":Oddish,"Charmander":Charmander,"Ninetales":Ninetales,"Ponyta":Ponyta,"Squirtle":Squirtle,"Psyduck":Psyduck,"Poliwag":Poliwag}
    pokemon_hand=pokelist_team[pokemonx]

startPoke(pokemon_h)
rest_of_poketeam=poke_team
rest_of_poketeam.remove(pokemon_h)

comp_poke_team=[]

comp_poke_team.append(grasslist[random.randint(0,1)])
comp_poke_team.append(firelist[random.randint(0,1)])
comp_poke_team.append(waterlist[random.randint(0,1)])
print("\n" + "The computer's team is " + str(comp_poke_team))
comp_poke_hand=random.randint(0,2)
pokelist_team={"Bulbasoar":Bulbasoar,"Bellsprout":Bulbasoar,"Oddish":Oddish,"Charmander":Charmander,"Ninetales":Ninetales,"Ponyta":Ponyta,"Squirtle":Squirtle,"Psyduck":Psyduck,"Poliwag":Poliwag}
pokemon_comp=comp_poke_team[comp_poke_hand]
pokemon_comp_hand=pokelist_team[pokemon_comp]
print("The computer is starting off with " + str(pokemon_comp) + "\n")
comp_pokelist_team={"Bulbasoar":Bulbasoar,"Bellsprout":Bulbasoar,"Oddish":Oddish,"Charmander":Charmander,"Ninetales":Ninetales,"Ponyta":Ponyta,"Squirtle":Squirtle,"Psyduck":Psyduck,"Poliwag":Poliwag}
rest_of_comp_team=comp_poke_team
rest_of_comp_team.remove(pokemon_comp)

def startCompPoke(pokemonx):
    global pokemon_comp_hand, rest_of_comp_team
    rest_of_comp_team=pokelist_team[pokemonx]
    
switchconfirm=False
users_pokemon=3
comps_pokemon=3
end=False
x=0

while end!=True:
    if x%2==0:
        option=input("What do you want to do? You can type 'switch', 'stats', 'heal' or 'attack'")
        if option=="stats":
            print("The name of the pokemon is " + pokemon_hand.name + ". The type of the pokemon is " + pokemon_hand.typea + ". The HP of the pokemon is " + str(pokemon_hand.health) + ". The attack power of the pokemon is " + str(pokemon_hand.attack_power) + ".")
        elif option=="switch": 
            while switchconfirm!=True:
                option2=input("\nWhich pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                if option2==rest_of_poketeam[0] or option2==rest_of_poketeam[1]:
                    rest_of_poketeam.append(pokemon_hand.name)
                    startPoke(option2)
                    rest_of_poketeam=poke_team
                    rest_of_poketeam.remove(option2)
                    switchconfirm=True
                    x+=1
                else:
                    print("Sorry, that is not a valid input. Please try again.")
        elif option=="heal":
            pokemon_hand.health+=5
            print("\n" + pokemon_hand.name + " healed himself by 5 hit points. " + pokemon_hand.name + " now has " + str(pokemon_hand.health) + " HP")
            x+=1
        elif option=="attack":
            checkvalidattack=False
            while checkvalidattack!=True:
                if pokemon_hand.typea=="water":
                    option3=input("Which attack do you want to do? These options include : \n\n Bubble : 40 power, 100% accurate \n Hydro Pump : 185 power, 30% accurate \n Surf : 70 power, 90% accurate \n")
                    if option3=="Bubble":
                        if pokemon_comp_hand.typea=="fire":
                            damagecalc=(1.5*((40+pokemon_hand.attack_power)/10))
                            pokemon_comp_hand.health-=damagecalc
                            print("\n" + pokemon_hand.name + " used Bubble and it did " + str(damagecalc) + " damage")
                            if pokemon_comp_hand.health<=0:
                                print(pokemon_comp_hand.name + " has fainted")
                                x+=1
                                if comps_pokemon>1:
                                    if comps_pokemon==3:
                                        comps_pokemon-=1
                                        randoam=random.randint(0,1)
                                        option2=rest_of_comp_team[randoam]
                                        rest_of_comp_team.append(pokemon_comp_hand)
                                        startCompPoke(option2)
                                        rest_of_comp_team=comp_poke_team
                                    elif comps_pokemon==2:
                                        comps_pokemon-=1
                                        option2=rest_of_comp_team[0]
                                        rest_of_comp_team.append(pokemon_comp_hand)
                                        startCompPoke(option2)
                                        rest_of_comp_team=comp_poke_team
                                else:
                                    print("You defeated the computer! Good Job!")
                                    end=True
                            else:
                                print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")
                        else:
                            damagecalc=((40+pokemon_hand.attack_power)/10)
                            pokemon_comp_hand.health-=damagecalc
                            print("\n" + pokemon_hand.name + " used Bubble and it did " + str(damagecalc) + " damage")
                            if pokemon_comp_hand.health<=0:
                                print(pokemon_comp_hand.name + " has fainted")
                                x+=1
                                if comps_pokemon>1:
                                    if comps_pokemon==3:
                                        comps_pokemon-=1
                                        randoam=random.randint(0,1)
                                        option2=rest_of_comp_team[randoam]
                                        rest_of_comp_team.append(pokemon_comp_hand)
                                        startCompPoke(option2)
                                        rest_of_comp_team=comp_poke_team
                                    elif comps_pokemon==2:
                                        comps_pokemon-=1
                                        option2=rest_of_comp_team[0]
                                        rest_of_comp_team.append(pokemon_comp_hand)
                                        startCompPoke(option2)
                                        rest_of_comp_team=comp_poke_team
                                else:
                                    print("\n You defeated the computer! Good Job!")
                                    end=True
                            else:
                                print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")
                        checkvalidattack=True
                    elif option3=="Hydro Pump":
                        checkvalidattack=True
                        chance=random.randint(1,10)
                        if chance<=3:
                            if pokemon_comp_hand.typea=="fire":
                                damagecalc=(1.5*((185+pokemon_hand.attack)/10))
                                print("\n" + pokemon_hand.name + " used Hydro Pump and it did " + str(damagecalc) + " damage")
                                pokemon_comp_hand.health-=damagecalc
                                if pokemon_comp_hand.health<=0:
                                    print(pokemon_comp_hand.name + " has fainted")
                                    x+=1
                                    if comps_pokemon>1:
                                        if comps_pokemon==3:
                                            comps_pokemon-=1
                                            randoam=random.randint(0,1)
                                            option2=rest_of_comp_team[randoam]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                        elif comps_pokemon==2:
                                            comps_pokemon-=1
                                            option2=rest_of_comp_team[0]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                    else:
                                        print("\n You defeated the computer! Good Job!")
                                        end=True
                                else:
                                    print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")
                            else:
                                damagecalc=((185+pokemon_hand.attack_power)/10)
                                print("\n" + pokemon_hand.name + " used Hydro Pump and it did " + str(damagecalc) + " damage")
                                pokemon_comp_hand.health-=damagecalc
                                if pokemon_comp_hand.health<=0:
                                    print(pokemon_comp_hand.name + " has fainted")
                                    x+=1
                                    if comps_pokemon>1:
                                        if comps_pokemon==3:
                                            comps_pokemon-=1
                                            randoam=random.randint(0,1)
                                            option2=rest_of_comp_team[randoam]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                        elif comps_pokemon==2:
                                            comps_pokemon-=1
                                            option2=rest_of_comp_team[0]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                    else:
                                        print("\n You defeated the computer! Good Job!")
                                        end=True
                                else:
                                    print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")
                        else:
                            print("\n" + pokemon_hand.name + " tried to use Hydro Pump, but it missed")
                        checkvalidattack=True
                    elif option3=="Surf":
                        checkvalidattack=True
                        chance=random.randint(1,10)
                        if chance<=9:
                            if pokemon_comp_hand.typea=="fire":
                                damagecalc=(1.5*((70+pokemon_hand.attack_power)/10))
                                pokemon_comp_hand.health-=damagecalc
                                print("\n" + pokemon_hand.name + " used Surf and it did " + str(damagecalc) + " damage")
                                if pokemon_comp_hand.health<=0:
                                    print(pokemon_comp_hand.name + " has fainted")
                                    x+=1
                                    if comps_pokemon>1:
                                        if comps_pokemon==3:
                                            comps_pokemon-=1
                                            randoam=random.randint(0,1)
                                            option2=rest_of_comp_team[randoam]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                        elif comps_pokemon==2:
                                            comps_pokemon-=1
                                            option2=rest_of_comp_team[0]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                    else:
                                        print("\n You defeated the computer! Good Job!")
                                        end=True
                                else:
                                    print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")
                            else:
                                damagecalc=((70+pokemon_hand.attack_power)/10)
                                pokemon_comp_hand.health-=damagecalc
                                print("\n" + pokemon_hand.name + " used Surf and it did " + str(damagecalc) + " damage")
                                if pokemon_comp_hand.health<=0:
                                    print(pokemon_comp_hand.name + " has fainted")
                                    x+=1
                                    if comps_pokemon>1:
                                        if comps_pokemon==3:
                                            comps_pokemon-=1
                                            randoam=random.randint(0,1)
                                            option2=rest_of_comp_team[randoam]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                        elif comps_pokemon==2:
                                            comps_pokemon-=1
                                            option2=rest_of_comp_team[0]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                    else:
                                        print("\n You defeated the computer! Good Job!")
                                        end=True
                                else:
                                    print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")
                        else:
                            print("\n" + pokemon_hand.name + " tried to use Surf, but it missed")
                        checkvalidattack=True
                    else:
                        print("Sorry, that is not an acceptable input. Please try again")
                        checkvalidattack=False
                elif pokemon_hand.typea=="grass":
                    option3=input("Which attack do you want to do? These options include : \n\n Leaf Storm : 130 power, 90% accurate \n Mega Drain : 50 power, 100% accurate \n Razor Leaf : 55 power, 95% accurate \n")
                    if option3=="Mega Drain":
                        if pokemon_comp_hand.typea=="water":
                            damagecalc=(1.5*((50+pokemon_hand.attack_power)/10))
                            pokemon_comp_hand.health-=damagecalc
                            print("\n" + pokemon_hand.name + " used Mega Drain and it did " + str(damagecalc) + " damage")
                            if pokemon_comp_hand.health<=0:
                                print(pokemon_comp_hand.name + " has fainted")
                                x+=1
                                if comps_pokemon>1:
                                    if comps_pokemon==3:
                                        comps_pokemon-=1
                                        randoam=random.randint(0,1)
                                        option2=rest_of_comp_team[randoam]
                                        rest_of_comp_team.append(pokemon_comp_hand)
                                        startCompPoke(option2)
                                        rest_of_comp_team=comp_poke_team
                                    elif comps_pokemon==2:
                                        comps_pokemon-=1
                                        option2=rest_of_comp_team[0]
                                        rest_of_comp_team.append(pokemon_comp_hand)
                                        startCompPoke(option2)
                                        rest_of_comp_team=comp_poke_team
                                else:
                                    print("\n You defeated the computer! Good Job!")
                                    end=True
                            else:
                                print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")
                        else:
                            damagecalc=((50+pokemon_hand.attack_power)/10)
                            pokemon_comp_hand.health-=damagecalc
                            print("\n" + pokemon_hand.name + " used Mega Drain and it did " + str(damagecalc) + " damage")
                            if pokemon_comp_hand.health<=0:
                                print(pokemon_comp_hand.name + " has fainted")
                                x+=1
                                if comps_pokemon>1:
                                    if comps_pokemon==3:
                                        comps_pokemon-=1
                                        randoam=random.randint(0,1)
                                        option2=rest_of_comp_team[randoam]
                                        rest_of_comp_team.append(pokemon_comp_hand)
                                        startCompPoke(option2)
                                        rest_of_comp_team=comp_poke_team
                                    elif comps_pokemon==2:
                                        comps_pokemon-=1
                                        option2=rest_of_comp_team[0]
                                        rest_of_comp_team.append(pokemon_comp_hand)
                                        startCompPoke(option2)
                                        rest_of_comp_team=comp_poke_team
                                else:
                                    print("\n You defeated the computer! Good Job!")
                                    end=True
                            else:
                                print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")
                        checkvalidattack=True
                    elif option3=="Leaf Storm":
                        chance=random.randint(1,10)
                        if chance<=9:
                            if pokemon_comp_hand.typea=="water":
                                damagecalc=(1.5*((130+pokemon_hand.attack_power)/10))
                                print("\n" + pokemon_hand.name + " used Leaf Storm and it did " + str(damagecalc) + " damage")
                                pokemon_comp_hand.health-=damagecalc
                                if pokemon_comp_hand.health<=0:
                                    print(pokemon_comp_hand.name + " has fainted")
                                    x+=1
                                    if comps_pokemon>1:
                                        if comps_pokemon==3:
                                            comps_pokemon-=1
                                            randoam=random.randint(0,1)
                                            option2=rest_of_comp_team[randoam]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                        elif comps_pokemon==2:
                                            comps_pokemon-=1
                                            option2=rest_of_comp_team[0]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                    else:
                                        print("\n You defeated the computer! Good Job!")
                                        end=True
                                else:
                                    print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")
                            else:
                                damagecalc=((130+pokemon_hand.attack_power)/10)
                                print("\n" + pokemon_hand.name + " used Leaf Storm and it did " + str(damagecalc) + " damage")
                                pokemon_comp_hand.health-=damagecalc
                                if pokemon_comp_hand.health<=0:
                                    print(pokemon_comp_hand.name + " has fainted")
                                    x+=1
                                    if comps_pokemon>1:
                                        if comps_pokemon==3:
                                            comps_pokemon-=1
                                            randoam=random.randint(0,1)
                                            option2=rest_of_comp_team[randoam]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                        elif comps_pokemon==2:
                                            comps_pokemon-=1
                                            option2=rest_of_comp_team[0]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                    else:
                                        print("\n You defeated the computer! Good Job!")
                                        end=True
                                else:
                                    print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")
                        else:
                            print("\n" + pokemon_hand.name + " tried to use Leaf Storm, but it missed")
                        checkvalidattack=True
                    elif option3=="Razor Leaf":
                        chance=random.randint(1, 10)
                        if chance<=9.5:
                            if pokemon_comp_hand.typea=="water":
                                damagecalc=(1.5*((55+pokemon_hand.attack_power)/10))
                                pokemon_comp_hand.health-=damagecalc
                                print("\n" + pokemon_hand.name + " used Razor Leaf and it did " + str(damagecalc) + " damage")
                                if pokemon_comp_hand.health<=0:
                                    print(pokemon_comp_hand.name + " has fainted")
                                    x+=1
                                    if comps_pokemon>1:
                                        if comps_pokemon==3:
                                            comps_pokemon-=1
                                            randoam=random.randint(0,1)
                                            option2=rest_of_comp_team[randoam]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                        elif comps_pokemon==2:
                                            comps_pokemon-=1
                                            option2=rest_of_comp_team[0]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                    else:
                                        print("\n You defeated the computer! Good Job!")
                                        end=True
                                else:
                                   print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")
                            else:
                                damagecalc=((55+pokemon_hand.attack_power)/10)
                                pokemon_comp_hand.health-=damagecalc
                                print("\n" + pokemon_hand.name + " used Razor Leaf and it did " + str(damagecalc) + " damage")
                                if pokemon_comp_hand.health<=0:
                                    print(pokemon_comp_hand.name + " has fainted")
                                    x+=1
                                    if comps_pokemon>1:
                                        if comps_pokemon==3:
                                            comps_pokemon-=1
                                            randoam=random.randint(0,1)
                                            option2=rest_of_comp_team[randoam]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                        elif comps_pokemon==2:
                                            comps_pokemon-=1
                                            option2=rest_of_comp_team[0]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                    else:
                                        print("\n You defeated the computer! Good Job!")
                                        end=True
                                else:
                                    print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")            
                        else:
                            print(pokemon_hand.name + " tried to use Razor Leaf, but it missed")
                        checkvalidattack=True
                    else:
                        print("Sorry, that is not an acceptable input. Please try again.")
                        checkvalidattack=False
                elif pokemon_hand.typea=="fire":
                    option3=input("Which attack do you want to do? These options include : \n\n Ember : 60 power, 100% accurate \n Fire Punch : 85 power, 80% accurate \n Flame Wheel : 70 power, 90% accurate \n")
                    if option3=="Ember":
                        if pokemon_comp_hand.typea=="grass":
                            damagecalc=(1.5*((60+pokemon_hand.attack_power)/10))
                            pokemon_comp_hand.health-=damagecalc
                            print("\n" + pokemon_hand.name + " used Ember and it did " + str(damagecalc) + " damage")
                            if pokemon_comp_hand.health<=0:
                                print(pokemon_comp_hand.name + " has fainted")
                                x+=1
                                if comps_pokemon>1:
                                    if comps_pokemon==3:
                                        comps_pokemon-=1
                                        randoam=random.randint(0,1)
                                        option2=rest_of_comp_team[randoam]
                                        rest_of_comp_team.append(pokemon_comp_hand)
                                        startCompPoke(option2)
                                        rest_of_comp_team=comp_poke_team
                                    elif comps_pokemon==2:
                                        comps_pokemon-=1
                                        option2=rest_of_comp_team[0]
                                        rest_of_comp_team.append(pokemon_comp_hand)
                                        startCompPoke(option2)
                                else:
                                    print("\n You defeated the computer! Good Job!")
                                    end=True
                            else:
                                print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")   
                        else:
                            damagecalc=((60+pokemon_hand.attack_power)/10)
                            pokemon_comp_hand.health-=damagecalc
                            print("\n" + pokemon_hand.name + " used Ember and it did " + str(damagecalc) + " damage")
                            if pokemon_comp_hand.health<=0:
                                print(pokemon_comp_hand.name + " has fainted")
                                x+=1
                                if comps_pokemon>1:
                                    if comps_pokemon==3:
                                        comps_pokemon-=1
                                        randoam=random.randint(0,1)
                                        option2=rest_of_comp_team[randoam]
                                        rest_of_comp_team.append(pokemon_comp_hand)
                                        startCompPoke(option2)
                                        rest_of_comp_team=comp_poke_team
                                    elif comps_pokemon==2:
                                        comps_pokemon-=1
                                        option2=rest_of_comp_team[0]
                                        rest_of_comp_team.append(pokemon_comp_hand)
                                        startCompPoke(option2)
                                        rest_of_comp_team=comp_poke_team
                                else:
                                    print("\n You defeated the computer! Good Job!")
                                    end=True
                            else:
                                print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")
                        checkvalidattack=True
                    elif option3=="Fire Punch":
                        checkvalidattack=True
                        chance=random.randint(1,10)
                        if chance<=8:
                            if pokemon_comp_hand.typea=="grass":
                                damagecalc=(1.5*((85+pokemon_hand.attack_power)/10))
                                print("\n" + pokemon_hand.name + " used Fire Punch and it did " + str(damagecalc) + " damage")
                                pokemon_comp_hand.health-=damagecalc
                                if pokemon_comp_hand.health<=0:
                                    print(pokemon_comp_hand.name + " has fainted")
                                    x+=1
                                    if comps_pokemon>1:
                                        if comps_pokemon==3:
                                            comps_pokemon-=1
                                            randoam=random.randint(0,1)
                                            option2=rest_of_comp_team[randoam]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                        elif comps_pokemon==2:
                                            comps_pokemon-=1
                                            option2=rest_of_comp_team[0]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                    else:
                                        print("\n You defeated the computer! Good Job!")
                                        end=True
                                else:
                                    print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")
                            else:
                                damagecalc=((85+pokemon_hand.attack_power)/10)
                                print("\n" + pokemon_hand.name + " used Fire Punch and it did " + str(damagecalc) + " damage")
                                pokemon_comp_hand.health-=damagecalc
                                if pokemon_comp_hand.health<=0:
                                    print(pokemon_comp_hand.name + " has fainted")
                                    x+=1
                                    if comps_pokemon>1:
                                        if comps_pokemon==3:
                                            comps_pokemon-=1
                                            randoam=random.randint(0,1)
                                            option2=rest_of_comp_team[randoam]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                        elif comps_pokemon==2:
                                            comps_pokemon-=1
                                            option2=rest_of_comp_team[0]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                    else:
                                        print("\n You defeated the computer! Good Job!")
                                        end=True
                                else:
                                    print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")
                        else:
                            print("\n" + pokemon_hand.name + " tried to use Fire Punch, but it missed")
                        checkvalidattack=True
                    elif option3=="Flame Wheel":
                        chance=random.randint(1,10)
                        if chance<=9:
                            if pokemon_comp_hand.typea=="grass":
                                damagecalc=((70+pokemon_hand.attack_power)/10)
                                pokemon_comp_hand.health-=damagecalc
                                print("\n" + pokemon_hand.name + " used Flame Wheel and it did " + str(damagecalc) + " damage")
                                if pokemon_comp_hand.health<=0:
                                    print(pokemon_comp_hand.name + " has fainted")
                                    x+=1
                                    if comps_pokemon>1:
                                        if comps_pokemon==3:
                                            comps_pokemon-=1
                                            randoam=random.randint(0,1)
                                            option2=rest_of_comp_team[randoam]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                        elif comps_pokemon==2:
                                            comps_pokemon-=1
                                            option2=rest_of_comp_team[0]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                    else:
                                        print("\n You defeated the computer! Good Job!")
                                        end=True
                                else:
                                    print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")
                            else:
                                damagecalc=((70+pokemon_hand.attack_power)/10)
                                pokemon_comp_hand.health-=damagecalc
                                print("\n" + pokemon_hand.name + " used Flame Wheel and it did " + str(damagecalc) + " damage")
                                if pokemon_comp_hand.health<=0:
                                    print(pokemon_comp_hand.name + " has fainted")
                                    x+=1
                                    if comps_pokemon>1:
                                        if comps_pokemon==3:
                                            comps_pokemon-=1
                                            randoam=random.randint(0,1)
                                            option2=rest_of_comp_team[randoam]
                                            rest_of_comp_team.append(pokemon_comp_handd)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                        elif comps_pokemon==2:
                                            comps_pokemon-=1
                                            option2=rest_of_comp_team[0]
                                            rest_of_comp_team.append(pokemon_comp_hand)
                                            startCompPoke(option2)
                                            rest_of_comp_team=comp_poke_team
                                    else:
                                        print("\n You defeated the computer! Good Job!")
                                        end=True
                                else:
                                    print(pokemon_comp_hand.name + " has " + str(pokemon_comp_hand.health) + " left")
                        else:
                            print("\n" + pokemon_hand.name + " tried to use Flame Wheel, but it missed")
                        checkvalidattack=True
                else:
                    print("Sorry, that is not an acceptable input. Please try again.")
                    checkvalidattack=False
            x+=1
        else:
            print("Sorry, that is not a valid input. Please try again" + "\n")
            
    else:
        randominteger=random.randint(1,6)
        randm=random.randint(1,3)
        if randominteger<=4:
            if pokemon_comp_hand.typea=="water":
                if randm==1:
                    if pokemon_hand.typea=="fire":
                        damagecalc=(1.5*((40+pokemon_comp_hand.attack_power)/10))
                        pokemon_hand.health-=damagecalc
                        print("\n" + pokemon_comp_hand.name + " used Bubble and it did " + str(damagecalc) + " damage\n")
                        if pokemon_hand.health<=0:
                            print(pokemon_hand.name + " has fainted")
                            if users_pokemon>1:
                                users_pokemon-=1
                                option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                startPoke(option2)
                                rest_of_poketeam=poke_team
                                rest_of_poketeam.remove(option2)
                            else:
                                print("You were defeated. Too bad!")
                        else:
                            print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")
                    else:
                        damagecalc=((40+pokemon_hand.attack_power)/10)
                        pokemon_hand.health-=damagecalc
                        print("\n" + pokemon_comp_hand.name + " used Bubble and it did " + str(damagecalc) + " damage\n")
                        if pokemon_hand.health<=0:
                            print(pokemon_hand.name + " has fainted")
                            if users_pokemon>1:
                                users_pokemon-=1
                                option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                startPoke(option2)
                                rest_of_poketeam=poke_team
                                rest_of_poketeam.remove(option2)
                            else:
                                print("\n You were defeated. Too bad!")
                        else:
                            print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")
                elif randm==2:
                    chance=random.randint(1,10)
                    if chance<=3:
                        if pokemon_hand.typea=="fire":
                            damagecalc=(1.5*((185+pokemon_comp_hand.attack_power)/10))
                            print("\n" + pokemon_comp_hand.name + " used Hydro Pump and it did " + str(damagecalc) + " damage\n")
                            pokemon_hand.health-=damagecalc
                            if pokemon_hand.health<=0:
                                print(pokemon_hand.name + " has fainted")
                                if users_pokemon>1:
                                    users_pokemon-=1
                                    option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                    startPoke(option2)
                                    rest_of_poketeam=poke_team
                                    rest_of_poketeam.remove(option2)
                                else:
                                    print("\n You were defeated. Too bad!")
                            else:
                                print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")
                        else:
                            damagecalc=((185+pokemon_comp_hand.attack_power)/10)
                            print("\n" + pokemon_comp_hand.name + " used Hydro Pump and it did " + str(damagecalc) + " damage\n")
                            pokemon_hand.health-=damagecalc
                            if pokemon_hand.health<=0:
                                print(pokemon_hand.name + " has fainted")
                                if users_pokemon>1:
                                    users_pokemon-=1
                                    option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                    startPoke(option2)
                                    rest_of_poketeam=poke_team
                                    rest_of_poketeam.remove(option2)
                                else:
                                    print("\n You were defeated. Too bad!")
                            else:
                                print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")
                    else:
                        print("\n" + pokemon_comp_hand.name + " tried to use Hydro Pump, but it missed\n")
                elif randm==3:
                    chance=random.randint(1,10)
                    if chance<=9:
                        if pokemon_hand.typea=="fire":
                            damagecalc=(1.5*((70+pokemon_comp_hand.attack_power)/10))
                            pokemon_hand.health-=damagecalc
                            print("\n" + pokemon_comp_hand.name + " used Surf and it did " + str(damagecalc) + " damage\n")
                            if pokemon_hand.health<=0:
                                print(pokemon_hand.name + " has fainted")
                                if users_pokemon>1:
                                    users_pokemon-=1
                                    option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                    startPoke(option2)
                                    rest_of_poketeam=poke_team
                                    rest_of_poketeam.remove(option2)
                                else:
                                    print("\n You were defeated. Too bad!")
                            else:
                                print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")
                        else:
                            damagecalc=((70+pokemon_comp_hand.attack_power)/10)
                            pokemon_hand.health-=damagecalc
                            print("\n" + pokemon_comp_hand.name + " used Surf and it did " + str(damagecalc) + " damage\n")
                            if pokemon_hand.health<=0:
                                print(pokemon_hand.name + " has fainted")
                                if users_pokemon>1:
                                    users_pokemon-=1
                                    option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                    startPoke(option2)
                                    rest_of_poketeam=poke_team
                                    rest_of_poketeam.remove(option2)
                                else:
                                    print("\n You were defeated. Too bad!")
                            else:
                                print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")
                    else:
                        print("\n" + pokemon_hand.name + " tried to use Surf, but it missed\n")
            elif pokemon_comp_hand.typea=="grass":
                if randm==1:
                    if pokemon_hand.typea=="water":
                        damagecalc=(1.5*((50+pokemon_comp_hand.attack_power)/10))
                        pokemon_hand.health-=damagecalc
                        print("\n" + pokemon_comp_hand.name + " used Mega Drain and it did " + str(damagecalc) + " damage\n")
                        if pokemon_hand.health<=0:
                            print(pokemon_hand.name + " has fainted")
                            if users_pokemon>1:
                                users_pokemon-=1
                                option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                startPoke(option2)
                                rest_of_poketeam=poke_team
                                rest_of_poketeam.remove(option2)
                            else:
                                print("\n You were defeated. Too bad!")
                        else:
                            print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")
                    else:
                        damagecalc=((50+pokemon_comp_hand.attack_power)/10)
                        pokemon_hand.health-=damagecalc
                        print("\n" + pokemon_comp_hand.name + " used Mega Drain and it did " + str(damagecalc) + " damage\n")
                        if pokemon_hand.health<=0:
                            print(pokemon_hand.name + " has fainted")
                            if users_pokemon>1:
                                users_pokemon-=1
                                option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                startPoke(option2)
                                rest_of_poketeam=poke_team
                                rest_of_poketeam.remove(option2)
                            else:
                                print("\n You were defeated. Too bad!")
                        else:
                            print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")                    
                elif randm==2:
                    chance=random.randint(1,10)
                    if chance<=9:
                        if pokemon_hand.typea=="water":
                            damagecalc=(1.5*((130+pokemon_comp_hand.attack_power)/10))
                            print("\n" + pokemon_comp_hand.name + " used Leaf Storm and it did " + str(damagecalc) + " damage\n")
                            pokemon_hand.health-=damagecalc
                            if pokemon_hand.health<=0:
                                print(pokemon_hand.name + " has fainted")
                                if users_pokemon>1:
                                    users_pokemon-=1
                                    option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                    startPoke(option2)
                                    rest_of_poketeam=poke_team
                                    rest_of_poketeam.remove(option2)
                                else:
                                    print("\n You were defeated. Too bad!")
                            else:
                                print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")
                        else:
                            damagecalc=((130+pokemon_comp_hand.attack_power)/10)
                            print("\n" + pokemon_comp_hand.name + " used Leaf Storm and it did " + str(damagecalc) + " damage\n")
                            pokemon_hand.health-=damagecalc
                            if pokemon_hand.health<=0:
                                print(pokemon_hand.name + " has fainted")
                                if users_pokemon>1:
                                    users_pokemon-=1
                                    option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                    startPoke(option2)
                                    rest_of_poketeam=poke_team
                                    rest_of_poketeam.remove(option2)
                                else:
                                    print("\n You were defeated. Too bad!")
                            else:
                                print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")
                    else:
                        print("\n" + pokemon_comp_hand.name + " tried to use Leaf Storm, but it missed\n")
                elif randm==3:
                    chance=random.randint(1, 10)
                    if chance<=9.5:
                        if pokemon_comp_hand.typea=="water":
                            damagecalc=(1.5*((55+pokemon_comp_hand.attack_power)/10))
                            pokemon_hand.health-=damagecalc
                            print("\n" + pokemon_comp_hand.name + " used Razor Leaf and it did " + str(damagecalc) + " damage\n")
                            if pokemon_hand.health<=0:
                                print(pokemon_hand.name + " has fainted")
                                if users_pokemon>1:
                                    users_pokemon-=1
                                    option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                    startPoke(option2)
                                    rest_of_poketeam=poke_team
                                    rest_of_poketeam.remove(option2)
                                else:
                                    print("\n You were defeated. Too bad!")
                            else:
                               print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")
                        else:
                            damagecalc=((55+pokemon_comp_hand.attack_power)/10)
                            pokemon_hand.health-=damagecalc
                            print("\n" + pokemon_comp_hand.name + " used Razor Leaf and it did " + str(damagecalc) + " damage\n")
                            if pokemon_hand.health<=0:
                                print(pokemon_hand.name + " has fainted")
                                if users_pokemon>1:
                                    users_pokemon-=1
                                    option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                    startPoke(option2)
                                    rest_of_poketeam=poke_team
                                    rest_of_poketeam.remove(option2)
                                else:
                                    print("\n You were defeated. Too bad!")
                            else:
                                print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")            
                    else:
                        print("\n" + pokemon_comp_hand.name + " tried to use Razor Leaf, but it missed\n")
            elif pokemon_comp_hand.typea=="fire":
                if randm==1:
                    if pokemon_comp_hand.typea=="grass":
                        damagecalc=(1.5*((60+pokemon_comp_hand.attack_power)/10))
                        pokemon_hand.health-=damagecalc
                        print("\n" + pokemon_comp_hand.name + " used Ember and it did " + str(damagecalc) + " damage\n")
                        if pokemon_hand.health<=0:
                            print(pokemon_hand.name + " has fainted")
                            if users_pokemon>1:
                                users_pokemon-=1
                                option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                startPoke(option2)
                                rest_of_poketeam=poke_team
                                rest_of_poketeam.remove(option2)
                            else:
                                print("\n You were defeated. Too bad!")
                        else:
                            print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")   
                    else:
                        damagecalc=((60+pokemon_comp_hand.attack_power)/10)
                        pokemon_hand.health-=damagecalc
                        print("\n" + pokemon_comp_hand.name + " used Ember and it did " + str(damagecalc) + " damage\n")
                        if pokemon_hand.health<=0:
                            print(pokemon_hand.name + " has fainted")
                            if users_pokemon>1:
                                users_pokemon-=1
                                option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                startPoke(option2)
                                rest_of_poketeam=poke_team
                                rest_of_poketeam.remove(option2)
                            else:
                                print("\nYou were defeated. Too bad!")
                        else:
                            print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")
                elif randm==2:
                    chance=random.randint(1,10)
                    if chance<=8:
                        if pokemon_hand.typea=="grass":
                            damagecalc=(1.5*((85+pokemon_comp_hand.attack_power)/10))
                            print("\n" + pokemon_comp_hand.name + " used Fire Punch and it did " + str(damagecalc) + " damage\n")
                            pokemon_hand.health-=damagecalc
                            if pokemon_hand.health<=0:
                                print(pokemon_hand.name + " has fainted")
                                x+=1
                                if users_pokemon>1:
                                    users_pokemon-=1
                                    option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                    startPoke(option2)
                                    rest_of_poketeam=poke_team
                                    rest_of_poketeam.remove(option2)
                                else:
                                    print("\n You were defeated. Too bad!")
                            else:
                                print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")
                        else:
                            damagecalc=((85+pokemon_comp_hand.attack_power)/10)
                            print("\n" + pokemon_comp_hand.name + " used Fire Punch and it did " + str(damagecalc) + " damage\n")
                            pokemon_hand.health-=damagecalc
                            if pokemon_hand.health<=0:
                                print(pokemon_hand.name + " has fainted")
                                x+=1
                                if users_pokemon>1:
                                    users_pokemon-=1
                                    option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                    startPoke(option2)
                                    rest_of_poketeam=poke_team
                                    rest_of_poketeam.remove(option2)
                                else:
                                    print("\n You were defeated. Too bad!")
                            else:
                                print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")
                    else:
                        print("\n" + pokemon_comp_hand.name + " tried to use Fire Punch, but it missed\n")
                elif option3=="Flame Wheel":
                    chance=random.randint(1,10)
                    if chance<=9:
                        if pokemon_hand.typea=="grass":
                            damagecalc=((70+pokemon_comp_hand.attack_power)/10)
                            pokemon_hand.health-=damagecalc
                            print("\n" + pokemon_comp_hand.name + " used Flame Wheel and it did " + str(damagecalc) + " damage\n")
                            if pokemon_hand.health<=0:
                                print(pokemon_hand.name + " has fainted")
                                x+=1
                                if users_pokemon>1:
                                    users_pokemon-=1
                                    option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                    startPoke(option2)
                                    rest_of_poketeam=poke_team
                                    rest_of_poketeam.remove(option2)
                                else:
                                    print("\n You were defeated. Too bad!")
                            else:
                                print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")
                        else:
                            damagecalc=((70+pokemon_comp_hand.attack_power)/10)
                            pokemon_hand.health-=damagecalc
                            print("\n" + pokemon_comp_hand.name + " used Flame Wheel and it did " + str(damagecalc) + " damage\n")
                            if pokemon_hand.health<=0:
                                print(pokemon_hand.name + " has fainted")
                                x+=1
                                if users_pokemon>1:
                                    users_pokemon-=1
                                    option2=input("Which pokemon would you like to switch to? You can choose to switch to either " + str(rest_of_poketeam))
                                    startPoke(option2)
                                    rest_of_poketeam=poke_team
                                    rest_of_poketeam.remove(option2)
                                else:
                                    print("\n You were defeated. Too bad!")
                            else:
                                print(pokemon_hand.name + " has " + str(pokemon_hand.health) + " left")
                    else:
                        print("\n" + pokemon_comp_hand.name + " tried to use Flame Wheel, but it missed\n")
        elif randominteger==5:
            pokemon_comp_hand.health+=5
            print("\n" + pokemon_comp_hand.name + " healed himself by 5 hit points. " + pokemon_comp_hand.name + " now has " + str(pokemon_comp_hand.health) + " HP\n")
        if comps_pokemon>1:
            if randominteger==6:
                if comps_pokemon==3:
                    randoam=random.randint(0,1)
                    option2=rest_of_comp_team[randoam]
                    rest_of_comp_team.append(pokemon_comp_hand)
                    startCompPoke(option2)
                    rest_of_comp_team=comp_poke_team
                elif comps_pokemon==2:
                    option2=rest_of_comp_team[0]
                    rest_of_comp_team.append(pokemon_comp_hand)
                    startCompPoke(option2)
                    rest_of_comp_team=comp_poke_team
        x+=1
