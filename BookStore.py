from Book import Book
from Magazine import Magazine

b1 = Book("python for beginers", 200, 15)
b1.SetAuthorName("Mr. G")
print(b1)
b1.SellCopy(2)
print(b1)
b1.OrderCopy(5)
print(b1)

m1 = Magazine("computer word", 60, 100, 0, 77)
print(m1)