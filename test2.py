import sys;
args=sys.argv[-1]
fp=open("ip2.txt","r")
i=fp.read();
ip=i.split(" ")
ip[-1]=ip[-1].split("\n")[0]
count=0
for a in ip:
	if(a==args):
		count=count+1
if count==0:
	print("ip not found")
else:
	print(args,"ip found",count,"times")

fp.close()