import sys
args=sys.argv[1]
count=0
with open("ip1.txt") as fileobj:
    for line in fileobj:  
       if args in line:
         count=count+1;
         
if(count==0):
	  print ("no ip found ")
else:
	print("ip found times",count)