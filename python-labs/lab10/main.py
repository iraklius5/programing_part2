from book import Book
from node import Node


first_book = Book("The Picture of Dorian Gray", "Oscar Wilde", 1890, "A-ba-ba-ha-la-ma-ha", 120)
second_book = Book("Harry Potter and the Chamber of Secrets", "Joanne Rowling", 2017, "A-ba-ba-ha-la-ma-ha", 190)
third_book = Book("Marusya Churai", "Lina Kostenko", 2017, "A-ba-ba-ha-la-ma-ha", 220)
fourth_book = Book("Charlie and the chocolate factory", "Roald Dahl", 1997, "A-ba-ba-ha-la-ma-ha", 199)

root = Node(first_book)
root.insert(second_book)
root.insert(third_book)
root.insert(fourth_book)
root.print_tree()
print()
print(root.find("A-ba-ba-ha-la-ma-ha"))
print()
root.delete("Joanne Rowling")
root.print_tree()