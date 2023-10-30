import math 
def distance (x1,y1,x2,y2) :
 dis = math.sqrt(((x2-x1)**2) +((y2-y1)**2))
print('distance entre u{},{})  , v({},{})')
print('entre point1 :')
x1 = int(input(" x1 = "))
y1 = int(input(" y1 = "))
print('entre point2:')
x2 = int(input(" x2 = "))
y2 = int(input(" y2 = "))
distance (x1,y1,x2,y2)
print(distance)