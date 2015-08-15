print "Welcome to 'A Simple Life', Created by Jai Yarlagadda Sat Aug 15 2015" 

print "You wake up and find yourself relaxed \nfrom a good sleep last night. You get a text message."
print "Type 1 to check your phone"
print "Type 2 to not check your phone" 

phone = raw_input('>')

if phone == '1':
	print "It is from your ex wife. It says, 'Hey, you left some stuff at my house, can you come and get them?'" 
	print "Type 1 to go pick up your stuff" 
	print "Type 2 to ignore the message" 
	
	stuff = raw_input('>')
	if stuff == '1':
		print "You drive to the house but get into a car accident. You die." 
		
	else:
		print "You go back to sleep. Good night."
	

elif phone == '2':
	print "You go back to sleep. Good night." 
	
else: 
	print "You get a heart attack. You die." 
	
