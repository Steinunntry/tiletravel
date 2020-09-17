

# Hér munum við gera forritið Tile traveller sem er ferðalag frá reit 1.1 til 3.1


directions = input("Direction:")
#föll : 
def where_to_next():
    # með þessu falli tökum við inn núverandi staðsetningu og sláum inn hvert við viljum fara næst.
    #
    # reitur 1.1 ------ N
    #reitur 1.2 ------- S / A / N       Skrifa hér hvaða ferða möguleikar eru í hverjum reit
    #reitur 1.3 ------- S / A           
    #reitur 2.1 ------- N
    #reitur 2.2 ------- V / S
    #reitur 2.3 ------- V / A
    #reitur 3.1 ------- Victory
    #reitur 3.2 ------- S / N
    #reitur 3.3 ------- V / N

 functions for moves
    #n/N for north (up) = y +1
    #e/E for east (right) = x + 1
    #s/S for south (down) = y -1
    #w/W for west (left) = x - 1

def move_n(x,y):
    if direction == "n" or direction == "N":
        y+=1
        x=x
    return x,y

def move_s(x,y):
    if direction == "s" or direction == "S":
        y-=1
        x=x
    return x,y

def move_e(x,y):
    if direction == "e" or direction == "E":
        y=y
        x+=1
    return x,y


def move_w(x,y):
    if direction == "w" or direction == "W":
        y=y
        x-=1
    return x,y

# fomulas for possible moves

def go_north():
    if y == 1 or (y==2 and x!=2):
        n = "(N)orth"
    else:
        n = "Not a valid direction"
    return n

def go_south():
	if y == 2 or (y==3 and x!=2)):
		s = "(S)outh"
	else:
		s = "Not a valid direction"
	return s

def go_east():
	if (x==1 and y ==3) or(y==2 and x==3)or(x==1 and y==2)
		e = "(E)ast"
	else:
		e = "Not a valid direction"
	return e

def go_west():
	if (x ==2 and y ==3) or (x==3 and y==3)
		W = "(W)est"
	else:
		W = "Not a valid direction"
	return e


# tiles
x,y = 1,1
x,y = 1,2
x,y = 1,3
x,y = 2,1
x,y = 2,2
x,y = 2,3
x,y = 3,1
x,y = 3,2
x,y = 3,3


#start game

x,y=1,1
direction ="N(orth)"

print("You can Travel: ", direction )

direction                                                  

