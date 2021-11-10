import os

times = input('Enter a number of file you want to create: ')
filename = input('Enter a name of file: ')

# Creates a new file
for i in range(3):
    fileCreate = filename + str(i) + '.txt'
    with open(fileCreate, 'w') as fp:
        pass
        # To write data to new file uncomment
        # this fp.write("New file created")
