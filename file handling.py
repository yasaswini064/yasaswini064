#to create a file
file = open("yashu.txt", mode='w')  
write_data = file.write("\n hi iam yasaswini")
file.close()

#to append text to the existing file
file = open("yashu.txt", mode='a')  
write_data = file.write("\n iam a graduate")
file.close()

#to read already existing file
file = open("yashu.txt", mode='r')  
read_data = file.read()
print(read_data)
file.close()

#trucate
file = open("yashu.txt", mode='w+')  
write_data = file.write("\n you are so cute")
file.close()

file = open("yashu.txt", mode='r+')  
read_data = file.read()
print(read_data)
file.close()

file = open("yashu.txt", mode='a+')  
write_data = file.write("\n you can do it")
file.close()

#using readlines
file = open("yashu.txt", mode='r+')  
read_data = file.readlines()
print(read_data)
file.close()

#write lines
list_1 = ["\nswaroop","\nramya","\npandu","\nbhavana","\nnithin","\nyashu"]
file = open("cousins.txt",mode = 'w+')
write_data= file.writelines(list_1)
file.close()

#to create file in desktop
file = open("C:\\Users\\SWAROOP\\Desktop\\angrybird.txt",mode = 'w')



