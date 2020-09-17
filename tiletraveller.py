

# Hér munum við gera forritið Tile traveller sem er ferðalag frá reit 1.1 til 3.1

print("You can travel (N)orth.")
direction = str(input("Direction:"))
x=1
y = 1   

 #functions for moves
    #n/N for north (up) = y +1
    #e/E for east (right) = x + 1
    #s/S for south (down) = y -1
    #w/W for west (left) = x - 1

#Föll fyrir mögulegar færslur:

def can_go_north(x,y):
    if (y==1 or (y==2 and x!=2)):   #Skila True ef þú getur farið norður annars false
        return True
    else:
        return False


def can_go_south(x,y):
    if (y==2 or (y==3 and x!=2)):
        return True
    else:
        return False

def can_go_west(x,y):
    if ((x==2 and y==3) or (x==2 and y==2) or (x==3 and y==3)):
        return True
    else:
        return False


def can_go_east(x,y):
    if ((x==1 and y==3) or (x==2 and y==3) or (x==1 and y==2)):
        return True
    else:
        return False



# Föll til að finna hvaða leiðir eru mögulegar

def where_to(x,y):
    all_dir = ""
    if can_go_north(x,y):
        all_dir=all_dir+"(N)orth"
    if can_go_south(x,y):
        if can_go_north(x,y):
            all_dir=all_dir+" or "
        all_dir=all_dir+"(S)outh"
    if can_go_east(x,y):
        if can_go_north(x,y) or can_go_south(x,y):
            all_dir=all_dir+" or "
        all_dir=all_dir+ "(E)ast"
    if can_go_west(x,y):
        if can_go_north(x,y) or can_go_south(x,y) or can_go_east(x,y):
            all_dir=all_dir+" or "
        all_dir=all_dir+ "(W)est"
    all_dir=all_dir+"."
    return all_dir

while direction:
    direction=direction.lower()
    if direction == "n" and can_go_north(x,y):
        y= y+1
    elif direction == "s" and can_go_south(x,y):
        y = y-1
    elif direction == "e" and can_go_east(x,y):
        x= x+1
    elif direction == "w" and can_go_west(x,y):
        x=x-1
    else:
        print("Not a valid direction!")
    if x==3 and y==1:
        print("Victory!")
        break
    possible_dir = where_to(x,y)
    print("You can travel:", possible_dir)
    direction = str(input("Direction: "))
    

# # tiles
# x,y = 1,1
# x,y = 1,2
# x,y = 1,3
# x,y = 2,1
# x,y = 2,2
# x,y = 2,3
# x,y = 3,1
# x,y = 3,2
# x,y = 3,3