b=[10,20,[300,400,[5000,6000],500],30,40]

m=[7000]

reformed=[]

x=0

while x != len(b):
	
	if  type(b[x]) == list:
		
		for i in b[x]:
			
			if (type(i) == list) and i[-1]==6000:
				
				i.extend(m)
				
				reformed.extend([b[x]])
				
				
				
				
	else:
		
		reformed.extend([b[x]])
	
	
	x+=1

print(reformed)



