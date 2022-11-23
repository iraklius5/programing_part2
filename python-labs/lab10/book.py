class Book:
    def __init__(self, name, author, year_of_publish, publication, price):
        self.name = name
        self.author = author
        self.year_of_publish = year_of_publish
        self.publication = publication
        self.price = price

    def __str__(self):
        return f'The book {self.name}, author {self.author}, was published ' \
               f'in {self.year_of_publish}, publication {self.publication}, for ${self.price}'
