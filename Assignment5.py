'''
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''
studentdictionary={'Kirti':95,'Vayu':100,'Lakshit':95,
            'Shaurya':96,'Kunj':98,'Advit':33,'Pranil':75}
name = input("Enter the student's name: ")
try:
    marks = studentdictionary.get(name)
    if marks is None:
        raise TypeError
except TypeError:
    print("Student not found.")
finally:
    if marks is not None:
        print(name, "'s marks: ", marks)

'''
Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''
numbers=[1,2,3,4,5,6,7,8,9,10]
print("Original list:",numbers)
extractednumbers=numbers[0:5] #list slicing
print("Extracted first five elements: ",extractednumbers)
reversednumbers=[]
for x in range(5):
    num= extractednumbers[4-x]
    reversednumbers.append(num)
print('Reversed extracted elements: ',reversednumbers)
