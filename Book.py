from Publication import Publication


class Book(Publication):
    def SetAuthorName(self, name):
        self.Author = name

    def OrderCopy(self, number):
        self.Copies = self.Copies+number    

    def __str__(self):
        return f'Author Name: {self.Author} Book info: {super().__str__()}'