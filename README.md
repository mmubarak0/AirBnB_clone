# Project: 0x00. AirBnB clone - The console
# AirBnB Clone Project

This project is a simplified version of the AirBnB website, where users can browse, book and review places to stay. The project consists of four parts:

- A command interpreter that allows you to create, manipulate and store objects of various classes, such as User, State, City and Place.
- A file storage engine that serializes and deserializes objects to and from JSON files.
- A web static part that contains HTML/CSS templates for the web pages of the project.
- A web dynamic part that uses Flask to create a RESTful API for the objects and integrates the web static part with the database.

## Command Interpreter

The command interpreter is a program that runs in a terminal and allows you to perform actions on the objects of the project. You can use it to create new objects, show existing objects, update attributes of objects, delete objects and perform other operations.

To start the command interpreter, run the file `console.py` in your terminal. You will see a prompt `(hbnb)` where you can type commands. To exit the program, type `quit` or press Ctrl-D.

The command interpreter supports the following commands:

- `create <class>`: Creates a new instance of `<class>` and prints its id.
- `show <class> <id>`: Prints the string representation of an instance based on its `<class>` and `<id>`.
- `destroy <class> <id>`: Deletes an instance based on its `<class>` and `<id>`.
- `all [<class>]`: Prints all string representations of instances of a given `<class>` or of all classes if no argument is given.
- `update <class> <id> <attribute name> "<attribute value>"`: Updates an instance based on its `<class>` and `<id>` by adding or updating an attribute. The attribute name and value must be in double quotes.
- `<class>.count()`: Prints the number of instances of a given `<class>`.
- `<class>.all()`: Prints all string representations of instances of a given `<class>`.
- `<class>.show(<id>)`: Prints the string representation of an instance based on its `<class>` and `<id>`.
- `<class>.destroy(<id>)`: Deletes an instance based on its `<class>` and `<id>`.
- `<class>.update(<id>, <attribute name>, <attribute value>)`: Updates an instance based on its `<class>` and `<id>` by adding or updating an attribute. The attribute name and value do not need to be in double quotes.

## File Storage

The file storage engine is a module that handles the serialization and deserialization of objects to and from JSON files. It uses a class called `FileStorage` that has two attributes:

- `__file_path`: A string that represents the path to the JSON file (ex: file.json).
- `__objects`: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212).

## Usage

### Interactive mode:
```fish
$ ./console.py
(hbnb) all
["[BaseModel] (9f660537-5c81-4a2b-a67b-6b23013aec96) {'id': '9f660537-5c81-4a2b-a67b-6b23013aec96', 'created_at': datetime.datetime(2023, 10, 14, 8, 18, 22, 480586), 'updated_at': datetime.datetime(2023, 10, 14, 8, 18, 22, 480586)}", "[User] (3060b403-c913-47a6-807b-e1b6b17a37b1) {'id': '3060b403-c913-47a6-807b-e1b6b17a37b1', 'created_at': datetime.datetime(2023, 10, 14, 8, 19, 52, 814957), 'updated_at': datetime.datetime(2023, 10, 14, 8, 19, 52, 814981), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (076113e5-ba8e-4c5e-b90f-a97a6827427e) {'id': '076113e5-ba8e-4c5e-b90f-a97a6827427e', 'created_at': datetime.datetime(2023, 10, 14, 8, 19, 52, 815243), 'updated_at': datetime.datetime(2023, 10, 14, 8, 19, 52, 815278), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[User] (1b54475d-abf9-4179-9637-6a57c6356961) {'id': '1b54475d-abf9-4179-9637-6a57c6356961', 'created_at': datetime.datetime(2023, 10, 14, 8, 21, 42, 747117), 'updated_at': datetime.datetime(2023, 10, 14, 8, 21, 42, 747154), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (7a755a08-dd02-4814-bf95-0e95fc751fd1) {'id': '7a755a08-dd02-4814-bf95-0e95fc751fd1', 'created_at': datetime.datetime(2023, 10, 14, 8, 21, 42, 747840), 'updated_at': datetime.datetime(2023, 10, 14, 8, 21, 42, 747970), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}"]
(hbnb) all BaseModel
["[BaseModel] (9f660537-5c81-4a2b-a67b-6b23013aec96) {'id': '9f660537-5c81-4a2b-a67b-6b23013aec96', 'created_at': datetime.datetime(2023, 10, 14, 8, 18, 22, 480586), 'updated_at': datetime.datetime(2023, 10, 14, 8, 18, 22, 480586)}"]
(hbnb) all User
["[User] (3060b403-c913-47a6-807b-e1b6b17a37b1) {'id': '3060b403-c913-47a6-807b-e1b6b17a37b1', 'created_at': datetime.datetime(2023, 10, 14, 8, 19, 52, 814957), 'updated_at': datetime.datetime(2023, 10, 14, 8, 19, 52, 814981), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (076113e5-ba8e-4c5e-b90f-a97a6827427e) {'id': '076113e5-ba8e-4c5e-b90f-a97a6827427e', 'created_at': datetime.datetime(2023, 10, 14, 8, 19, 52, 815243), 'updated_at': datetime.datetime(2023, 10, 14, 8, 19, 52, 815278), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[User] (1b54475d-abf9-4179-9637-6a57c6356961) {'id': '1b54475d-abf9-4179-9637-6a57c6356961', 'created_at': datetime.datetime(2023, 10, 14, 8, 21, 42, 747117), 'updated_at': datetime.datetime(2023, 10, 14, 8, 21, 42, 747154), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (7a755a08-dd02-4814-bf95-0e95fc751fd1) {'id': '7a755a08-dd02-4814-bf95-0e95fc751fd1', 'created_at': datetime.datetime(2023, 10, 14, 8, 21, 42, 747840), 'updated_at': datetime.datetime(2023, 10, 14, 8, 21, 42, 747970), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}"]
```
```fish
(hbnb) show User 3060b403-c913-47a6-807b-e1b6b17a37b1
[User] (3060b403-c913-47a6-807b-e1b6b17a37b1) {'id': '3060b403-c913-47a6-807b-e1b6b17a37b1', 'created_at': datetime.datetime(2023, 10, 14, 8, 19, 52, 814957), 'updated_at': datetime.datetime(2023, 10, 14, 8, 19, 52, 814981), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}
```
```fish
(hbnb) update User 3060b403-c913-47a6-807b-e1b6b17a37b1 first_name ki2kid
(hbnb) show User 3060b403-c913-47a6-807b-e1b6b17a37b1
[User] (3060b403-c913-47a6-807b-e1b6b17a37b1) {'id': '3060b403-c913-47a6-807b-e1b6b17a37b1', 'created_at': datetime.datetime(2023, 10, 14, 8, 19, 52, 814957), 'updated_at': datetime.datetime(2023, 10, 14, 13, 3, 54, 113573), 'first_name': 'ki2kid', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}
```
```fish
(hbnb) destroy User 3060b403-c913-47a6-807b-e1b6b17a37b1
(hbnb) show User 3060b403-c913-47a6-807b-e1b6b17a37b1
** no instance found **
```
```fish
(hbnb) BaseModel.all()
["[BaseModel] (9f660537-5c81-4a2b-a67b-6b23013aec96) {'id': '9f660537-5c81-4a2b-a67b-6b23013aec96', 'created_at': datetime.datetime(2023, 10, 14, 8, 18, 22, 480586), 'updated_at': datetime.datetime(2023, 10, 14, 8, 18, 22, 480586)}"]
(hbnb) User.count()
3
(hbnb) BaseModel.count()
1
(hbnb) quit
```
## Resources

#### Read or watch:

* [AirBnB clone concept page](https://intranet.alxswe.com/concepts/263)
* [packages concept page](https://intranet.alxswe.com/concepts/66)
* [cmd module](https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A)
* [cmd module in depth](https://intranet.alxswe.com/rltoken/uEy4RftSdKypoig9NFTvCg)
* [uuid module](https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ)
* [datetime](https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA)
* [unittest module](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA)
* [args/kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng)
* [Python test cheatsheet](https://intranet.alxswe.com/rltoken/tgNVrKKzlWgS4dfl3mQklw)
* [cmd module wiki page](https://intranet.alxswe.com/rltoken/EvcaH9uTLlauxuw03WnkOQ)
* [python unittest](https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA)
## Learning Objectives

### General

* How to create a Python package
* How to create a command interpreter in Python using the <code>cmd</code> module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage <code>datetime</code>
* What is an <code>UUID</code>
* What is <code>*args</code> and how to use it
* What is <code>**kwargs</code> and how to use it
* How to handle named arguments in a function
## Tasks

| Task | File |
| ---- | ---- |
| 3. BaseModel | [base_model.py](./models/base_model.py) |
| 4. Create BaseModel from dictionary | [base_model.py](./models/base_model.py) |
| 5. Store first object | [file_storage.py](./models/engine/file_storage.py) |
| 6. Console 0.0.1 | [console.py](./console.py) |
| 7. Console 0.1 | [console.py](./console.py) |
| 8. First User | [user.py](./models/user.py) |
| 9. More classes! | [state.py](./models/state.py), [city.py](./models/city.py), [amenity.py](./models/amenity.py), [place.py](./models/place.py), [review.py](./models/review.py) |
| 10. Console 1.0 | [console.py](./console.py) |
