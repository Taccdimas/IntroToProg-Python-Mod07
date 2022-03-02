"""
Title:  Assignment 07
Description:    Script demonstrates work with binary files & Exception Handling
ChangeLog:  DP - 02.27.2022 - created
"""
# sample DATA
file_name = "data_file.dat"
user1 = [1, "Bob"]
user2 = [2, "John"]
user3 = [3,"Sam"]
lst_users = [user1, user2, user3]
# Functions for reading and writing:
def read_file(file):  # Function to read binary file, Read mode
    with open(file, "rb") as obj_file:
        data_from_file = pickle.load(obj_file)
    print("\nCurrent data saved in file:\n", data_from_file)
def write_file(list, file):  # Function to write into binary file. Overwrite
    try:  # Handling exception if file is "Read-only"
        with open(file, "wb") as obj_file:
            pickle.dump(list, obj_file)
    except IOError:
        print("\nNo access to file. Program is terminated")
        exit()
# Main body of script:
import pickle
write_file(list=lst_users, file=file_name)  # Writing current list data into file
read_file(file=file_name)  # Reading current data from file
#  Ask new data from user and add it to list
while(True):
    try:
        new_id = int(input("\nInput ID for new user: "))
        if new_id > 3:
            break
        else:
            print("ID already exists")
            continue
    except ValueError:  # raised when value for ID is not integer
        print("\nID should be an integer")
new_user = input("Input NAME for new user: ")
new_item = [new_id, new_user]
lst_users.append(new_item)
# Re-write data into binary file
write_file(list=lst_users, file=file_name)
print("\nData re-saved into file")
# Read data from file
read_file(file=file_name)