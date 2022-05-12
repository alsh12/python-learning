class Store:
    def __init__(self,name):
        self.name = name
        self.items = []

    def AddItems(self,name,price):
        self.item = dict({'name':name,'price':price})
        self.items.append(self.item)
        

    def StockPrice(self):
        return sum(item['price'] for item in self.items)


store = Store("Brian")
store.AddItems("Sugar",34)
store.AddItems("Ghee",500)
store.AddItems("Oil",1000)
print(f'Total Stock Price: {store.StockPrice()}')