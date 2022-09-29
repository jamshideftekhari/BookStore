class Publication():
    def __init__(self, title, price, copies):
        self.Title=title
        self.Price=price
        self.Copies=copies

    def SellCopy(self,number):
        self.Copies=self.Copies-number

    def __str__(self):
        return f'Title: {self.Title} Price: {self.Price} numbers in store: {self.Copies}'      