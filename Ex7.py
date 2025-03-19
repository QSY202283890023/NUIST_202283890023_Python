# Ex7.py
# Author: Qin Siyuan
# Date: 19/3/25
def studList():  
    # Create a list of student names  
    studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]  
    # Use a for loop to print each name followed by the last name "Evans"  
    for name in studentNames:  
        print(name + " Evans")  

def addToList():  
    # Ask the user to add another name  
    new_name = input("Please enter another name to add to the list: ")  
    # Add the new name to the list  
    studentNames.append(new_name)  
    
    # Print the updated list  
    print("Updated list of names:")  
    for name in studentNames:  
        print(name + " Evans")  

# Call the functions  
studList()  
# Initialize the student names list for use in addToList function  
studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]  
addToList()  
