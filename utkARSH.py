import json
import time

x=5     #to change x value
sec=5   #to change seconds


current_y=x
f=open('sample_data.json','r')
json_list=json.load(f)
print(list(json_list.values()))
input()
for i in list(json_list.values()):

    time.sleep(sec)
    y=i
    if( (y>=( x+(x* 0.15) ))  or (y<= (x- (x*0.05)  ))   ):
        x=y
        current_y=y
        print('into if',x,y,current_y)
    else:
        current_y=y
        print('into else',x,y,current_y)

        continue
#elif(condition):
    #break