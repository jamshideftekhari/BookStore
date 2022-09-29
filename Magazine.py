from Publication import Publication


class Magazine(Publication):
    def __init__(self, title, price, copies, orderQty, currentIssue):
        super().__init__(title, price, copies)
        self.OrderQty=orderQty
        self.CurrentIssue = currentIssue

    def AdjustQty(self, number):
        self.OrderQty = self.OrderQty+number
    
    def ReciveNewIssue(self):
        self.CurrentIssue+=1

    def __str__(self):
        return f'{super().__str__()} Order Quantity: {self.OrderQty} Issue Number: {self.CurrentIssue}'     
