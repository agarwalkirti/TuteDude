'''
#Task 1: Read a File and Handle Errors
#Problem Statement:  Write a Python program that:
#1.   Opens and reads a text file named sample.txt.
#2.   Prints its content line by line.
#3.   Handles errors gracefully if the file does not exist.
'''
#modes can be read r, write w, append a,r+ read and write, x creation, rb read in binary etc
try:
    file1=open('sample.txt','r') # with open('sample.txt','r') as file1:
    statement=file1.read()
    print(statement)
except:
    print("sample.txt does not exist")
finally:
    file1.close()
    print("Sample File closed properly")
'''
#Task 2: Write and Append Data to a File

#Problem Statement: Write a Python program that:
#1.   Takes user input and writes it to a file named output.txt.
#2.   Appends additional data to the same file.
#3.   Reads and displays the final content of the file.
'''
try:
    file2=open('output.txt','w+')
    file2.write("Hello! This is output file. ")
    file2.seek(0)
    write_statement = file2.read()
    print(write_statement)
    file2=open('output.txt', 'a+')
    content = input("Enter content to be written in file: ")
    file2.write(content) # Add this user input to output file
    file2.seek(0)
    append_statement=file2.read()
    print(append_statement)
except:
    print("output.txt does not exist")
finally:
    file2.close()
    print("Output File closed properly")
