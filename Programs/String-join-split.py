# Python program to split a string and 
# join it using different delimiter 

def split_string(string): 

	# Split the string based on space delimiter 
	list_string = string.split(' ') 
	
	return list_string 

def join_string(list_string): 

	# Join the string based on '-' delimiter 
	string = '-'.join(list_string) 
	
	return string 

# Driver Function 
if __name__ == '__main__': 
	string = 'Rahul Goyal'
	
	# Splitting a string 
	list_string = split_string(string) 
	print(list_string) 

	# Join list of strings into one 
	new_string = join_string(list_string) 
	print(new_string) 

