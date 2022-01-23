import csv


try:
    input_number_rows = int(input("Enter number of new books\n"))
except ValueError:
    print("Invalid input")


class Book:
    def __init__(self, book_name, author, year):
        self.book_name = book_name,
        self.author = author,
        self.year = year

    def __str__(self):
        return self.book_name, self.author, self.year


book_list = []

while input_number_rows != 0:
    book_name = str(input("Enter the title: "))
    author = str(input("Enter the author: "))
    year = int(input("Enter the year: "))
    book_list.append(Book(book_name, author, year))
    input_number_rows -= 1

print(book_list)


with open("Book.csv", "a") as f:
    writer = csv.writer(f)
    for b in book_list:
        writer.writerow([b.book_name, b.author, b.year])




with open('Book.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in csvreader:
           print(', '.join(row))
