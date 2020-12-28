import shelve


helloFile = open('./hello.txt')
helloFile.read()
helloFile.close()

helloFile = open('./hello.txt')
# returns a single string
content = helloFile.read()
print(content)

helloFile.close()

helloFile = open('./hello.txt')
# return all of the lines as strings of a list
helloFile.readlines()
helloFile.close()

# write mode - create new file if one doesnt exist
helloFile = open('./hello2.txt', 'w')
helloFile.write('Hello!!!!!!!')
helloFile.write('Hello!!!!!!!')
# does not add new line - have to add yourself
helloFile.write('Hello!!!!!!!\n')
helloFile.write('Hello!!!!!!!')
helloFile.close()

# when you need to store lists and dictionaries shelve allows you do to that
# you can make changes to it as it if were a dictionary
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['hector', 'heathcliff', 'mongo', 'rifraff']
shelfFile.close()

# you can call .keys() and .values() on  the file like a dictionary
shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()