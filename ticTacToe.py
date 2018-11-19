m=[["","",""],["","",""],["","",""]]


def checkandplace(m,a,b,x):
    if m[a][b]=="x" or m[a][b]=="o":
        return 4
    else:
        m[a][b]=x
    
def board(m):
    for i in m:
        print(i)

def winner(m,a,b,x):
    if m[0][0]==m[0][1]==m[0][2]==x or m[1][0]==m[1][1]==m[1][2]==x or m[2][0]==m[2][1]==m[2][2]==x or m[0][0]==m[1][0]==m[2][0]==x\
    or m[o][1]==m[1][1]==m[2][1]==x or m[0][2]==m[1][2]==m[2][2]==x or m[0][0]==m[1][1]==m[2][2]==x or m[0][2]==m[1][1]==m[2][0]==x:
        return True

while True:
    print("Player A turn")
    a=int(input("X="))
    b=int(input("Y="))
    w=checkandplace(m,a,b,"x")
    if w==4:
        print (" overlap is not allowed ")
    board(m)

    winner(m,a,b,"x")
    print ("A IS THE WINNER")


    print("Player B turn")
    a=int(input("X="))
    b=int(input("Y="))
    w=checkandplace(m,a,b,"o")
    if w==4:
        print(" overlap is not allowed ")

    board(m)

    winner(m,a,b,"o")
    
  
    
        
