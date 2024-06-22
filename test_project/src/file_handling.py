# Open a file

file = open('newFile.txt', 'w')
file.write("This is a new File!!!\n")
file.close()

#Open a file in read mode
file_read = open('newFile.txt', 'r')
content = file_read.read()

print(content)
file_read.close()

# Open a file in append mode
file_append = open('newFile.txt', 'a')
file_append.write("This is a new line in the File!!!\n")
file_append.close()

file_read = open('newFile.txt', 'r')
content = file_read.read()

print(content)
file_read.close()