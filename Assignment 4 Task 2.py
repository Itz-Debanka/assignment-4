#Task 2
file=open("output.txt","r+")

a=str(input("enter text to write to the file:  "))
file.write(a+"\n")
print('data successfully written to output.txt')


c=str(input("enter additional text to append: "))
file.write(c+"\n")
print("data successfully appended")
file.seek(0)
n=int(input('number of characters to read: '))
print('final content of output.txt')
b=file.read(n)
print(b)
file.close()