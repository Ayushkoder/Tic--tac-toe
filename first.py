# Tic -tac -toe
def printboard(x_state,z_state):
    
    zero= 'X' if x_state[0]else('0' if z_state[0] else 0)
    one=  'X' if x_state[1]else('0' if z_state[1] else 1)
    two ='X' if x_state[2] else ('0' if z_state[2] else 2)
    three ='X' if x_state[3] else ('0' if z_state[3] else 3)
    four ='X' if x_state[4] else ('0' if z_state[4] else 4)
    five ='X' if x_state[5] else ('0' if z_state[5] else 5)
    six='X' if x_state[6] else ('0' if z_state[6] else 6 )
    seven='X' if x_state[7] else ('0' if z_state[7] else 7)
    eight='X' if x_state[8] else ('0' if z_state[8] else 8)
    
    print(f"{zero} |{one} |{two} ")     # print gives automatically new line 
    print(f"--|---|--")
    print(f"{three} |{four} |{five} ")
    print(f"--|---|--")
    print(f"{six} |{seven} |{eight} ")
    pass
def checkwin(x_state,z_state):
    wins=[[0,1,2],[0,3,6],[0,4,8],[2,5,8],[2,4,6],[6,7,8],[3,4,5],[1,4,7]]
    for win in wins:
        if (sum(x_state[wins[0]],x_state[wins[2]],x_state[wins[3]])== 3) :
            print('X' won the matach)
            return 1
        if (sum(z_state[wins[0]],z_state[wins[2]],z_state[wins[3]])== 3):
            print('0' won the matach)
            return 0
    return -1     
if __name__ == "__main__" :  
    x_state = [0, 0, 0, 0, 0, 0, 0, 0,0]  # xstate represent the position of X in the board then after putting X in board the position in xstate is also change 
    z_state = [0, 0, 0, 0, 0, 0, 0, 0,0]  #it is just the representation of place of 0 in the board 
    
    turn=1          #1 for x and 0 for o
    
    print("Welcome to Tic-Tac-Toe")
    while(True):
        printboard(x_state,z_state)
        if(turn==1):
         print("X chanches")
         value=int(input("Enter the value "))
         x_state[value]=1
        else:
            print(" 0 chanches")
            value=int(input("enter the value"))
            z_state[value]=1
        cwin=checkwin(x_state,z_state)
        if(cwin !=-1):
            break
        
        turn =1 -turn