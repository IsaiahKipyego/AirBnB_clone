Contents
Description
Environment
Further Information
Requirements
Repo Contents
Installation
Usage
Built with
Acknowledgements
Description 
This is the first of four phases of an attempt to make a copy of the AirBnB web app. To control the objects of the entire project in this initial phase, a simple console was built using the Cmd Python module, allowing the implementation of the methods create, show, update, all, and destroy to the existing classes and subclasses.

Environment 
The console was developed in Ubuntu 20.04LTS using python3 (version 3.8.5).

Further information 
For further information on python version, and documentation visit python.org.

Requirements 
Knowledge in python3
How to use a command line interpreter
A computer with Ubuntu 20.04
Python3 and pep8 style corrector.
Repo Contents 
This repository constains the following files:

File	Description
AUTHORS	Contains info about authors of the project
base_model.py	Defines BaseModel class (parent class), and methods
user.py	Defines subclass User
amenity.py	Defines subclass Amenity
city.py	Defines subclass City
place.py	Defines subclass Place
review.py	Defines subclass Review
state.py	Defines subclass State
file_storage.py	Creates new instance of class, serializes and deserializes data
console.py	creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object
test_base_model.py	unittests for base_model
test_user.py	unittests for user
test_amenity.py	unittests for amenity
test_city.py	unittests for city
test_place.py	unittests for place
test_review.py	unittests for review
test_state.py	unittests for state
test_file_storage.py	unittests for file_storage
test_console.py	unittests for console
Installation 
Clone the repository and run the console.py

$ git clone https://github.com/IsaiahKipyego/AirBnB_clone
Usage 
Method	Description
create	Creates object of given class
show	Prints the string representation of an instance based on the class name and id
all	Prints all string representation of all instances based or not on the class name
update	Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)
destroy	Deletes an instance based on the class name and id (save the change into the JSON file)
count	Retrieve the number of instances of a class
help	Prints information about specific command
quit/ EOF	Exit the program
Example No.1
(hbnb) create User
4bfe50ff-747c-4062-8c98-2da9405b84c1
(hbnb) show User 4bfe50ff-747c-4062-8c98-2da9405b84c1
[User] (4bfe50ff-747c-4062-8c98-2da9405b84c1) {'id': '4bfe50ff-747c-4062-8c98-2da9405b84c1', 'created_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 99815), 'updated_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 101018)}
(hbnb) all User
["[User] (597beedb-5d39-4546-a4d5-f3ddf2ae7d82) {'id': '597beedb-5d39-4546-a4d5-f3ddf2ae7d82', 'created_at': datetime.datetime(2023, 7, 16, 11, 10, 55, 757687), 'updated_at': datetime.datetime(2023, 7, 16, 11, 10, 55, 759466), 'first_name': 'John', 'age': '69'}", "[User] (4bfe50ff-747c-4062-8c98-2da9405b84c1) {'id': '4bfe50ff-747c-4062-8c98-2da9405b84c1', 'created_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 99815), 'updated_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 101018)}"]
(hbnb) update User update 4bfe50ff-747c-4062-8c98-2da9405b84c1 name Betty
** no instance found **
(hbnb) update User update 4bfe50ff-747c-4062-8c98-2da9405b84c1 name Betty
** no instance found **
(hbnb) update User 4bfe50ff-747c-4062-8c98-2da9405b84c1 name Betty
(hbnb) all User
["[User] (597beedb-5d39-4546-a4d5-f3ddf2ae7d82) {'id': '597beedb-5d39-4546-a4d5-f3ddf2ae7d82', 'created_at': datetime.datetime(2023, 7, 16, 11, 10, 55, 757687), 'updated_at': datetime.datetime(2023, 7, 16, 11, 10, 55, 759466), 'first_name': 'John', 'age': '69'}", "[User] (4bfe50ff-747c-4062-8c98-2da9405b84c1) {'id': '4bfe50ff-747c-4062-8c98-2da9405b84c1', 'created_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 99815), 'updated_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 101018), 'name': 'Betty'}"]
(hbnb) destroy User 597beedb-5d39-4546-a4d5-f3ddf2ae7d82
(hbnb) all
["[User] (4bfe50ff-747c-4062-8c98-2da9405b84c1) {'id': '4bfe50ff-747c-4062-8c98-2da9405b84c1', 'created_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 99815), 'updated_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 101018), 'name': 'Betty'}"]
(hbnb) show User 597beedb-5d39-4546-a4d5-f3ddf2ae7d82
** no instance found **
Example No.2
(hbnb)
(hbnb) User.create()
a7bb7ba5-711f-4490-a6df-972516441237
(hbnb) User.create
*** Unknown syntax: User.create
(hbnb) User.show()
** instance id missing **
(hbnb) User.update()
instance id missing 
(hbnb) User.show(a7bb7ba5-711f-4490-a6df-972516441237)
[User] (a7bb7ba5-711f-4490-a6df-972516441237) {'id': 'a7bb7ba5-711f-4490-a6df-972516441237', 'created_at': datetime.datetime(2023, 7, 16, 16, 54, 57, 176780), 'updated_at': datetime.datetime(2023, 7, 16, 16, 54, 57, 177214)}
(hbnb) User.all()
["[User] (4bfe50ff-747c-4062-8c98-2da9405b84c1) {'id': '4bfe50ff-747c-4062-8c98-2da9405b84c1', 'created_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 99815), 'updated_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 101018), 'name': 'Betty'}", "[User] (a7bb7ba5-711f-4490-a6df-972516441237) {'id': 'a7bb7ba5-711f-4490-a6df-972516441237', 'created_at': datetime.datetime(2023, 7, 16, 16, 54, 57, 176780), 'updated_at': datetime.datetime(2023, 7, 16, 16, 54, 57, 177214)}"]
(hbnb) User.destroy(a7bb7ba5-711f-4490-a6df-972516441237)
(hbnb) User.all()
["[User] (4bfe50ff-747c-4062-8c98-2da9405b84c1) {'id': '4bfe50ff-747c-4062-8c98-2da9405b84c1', 'created_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 99815), 'updated_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 101018), 'name': 'Betty'}"]
(hbnb) quit
Built with 
python3 (3.8.5)

Version
HBnB - version 5.5

Acknowledgements 
To all the peers that contribuited with their knowledge

Authors 
Isaiah Kipyego - @isaiahKipyego
