# file handling
file=open('myfile.txt','w')
#text="This is my first file handling project"
mytext=input("Enter the file text to write and read ")
file.write(mytext)
file.close()
file=open('myflile.txt','r')
text1=file.read()

print(text1)





