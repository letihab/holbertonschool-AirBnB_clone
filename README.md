
# console for project AirBnb clone

This project is a command-line interpreter (CLI) designed to manage and interact with different objects using a JSON-based data storage system. It allows users to create, retrieve, update, and delete instances of various classes, such as User, Place, State, City, Amenity, Review, and more.

The interpreter offers a user-friendly and text-based interface, making it easy to manipulate and query data for various use cases.

## How to Use

The command interpreter provides a set of commands to interact with the data storage. Here are some of the available commands:

* create: Create a new instance of a class and save it to the JSON file.

* show: Show the details of an instance based on its class and ID.

* destroy: Delete an instance based on its class and ID.

* all: List all instances or instances of a specific class.

* update: Update an instance's attributes.

The interpreter supports multiple classes like  User, Place, State, City, Amenity, and Review.

Examples

* Create a new place instance:

(hbnb) create Place

* Show details of a Place instance with a specific ID:

(hbnb) show Place 12345

* List all instances of the User class:

(hbnb) all User

* Update an instance's attribute:

(hbnb) update User 54321 email "new_email@example.com"

## Authors

Leticia Habib - leticia.habib@holbertonstudents.com

Gaël Deschamps - gael.deschamps@holbertonstudents.com

 #C21 -Holberton School Laval
