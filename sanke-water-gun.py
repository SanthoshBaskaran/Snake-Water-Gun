import random
print("Snake Water Gun")
print('Snake->press 1 :: Water->press 2 :: Gun->press 3')
def swg():
    list1=[]
    dict1={1:'Snake',2:'Water',3:'Gun'}
    user=int(input("You:"))
    while(user!=None):
        if(user>3):
            print("Invalid option")
            break
        print("   ",dict1[user])
        cpu=random.randint(1,3)
        print("Cpu:",cpu)
        print("   ",dict1[cpu])
        list1.append(dict1[user])
        list1.append(dict1[cpu])
        if(list1[0]==list1[1]):
            print("play again- Game Draw")
            swg()
        elif(list1[0]=='Snake' and list1[1]=='Water' or list1[0]=='Water' and list1[1]=='Snake'):
            print("Snake drinks water")
            if(user==1 and cpu==2):
                print("You won")
            elif(cpu==1 and user==2):
                print("cpu won")
        elif(list1[0]=='Snake' and list1[1]=='Gun' or list1[0]=='Gun' and list1[1]=='Snake'):
            print("Gun shots snake")
            if(user==1 and cpu==3):
                print("cpu won")
            elif(cpu==1 and user==3):
                print("you won")
        elif(list1[0]=='Water' and list1[1]=='Gun' or list1[0]=='Gun' and list1[1]=='Water'):
            print("Water falls upon Gun")
            if(user==2 and cpu==3):
                print("you won")
            elif(cpu==2 and user==3):
                print("cpu won")
        swg()
swg()
    
