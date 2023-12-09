disk_size_mb = 1.44
pages = 100
strings = 50
symbols = 25
byte = 4

book_byte = pages * strings * symbols * byte
book_mb = book_byte / 1024 ** 2
count_books = int(disk_size_mb // book_mb)

print("Количество книг, помещающихся на дискету:", count_books)
