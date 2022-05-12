class TooManyItemsSoldError(ValueError):
    pass


class Store:
    def __init__(self, name: str, total_items: int):
        self.name = name
        self.total_items = total_items
        self.items_sold = 0

    def __repr__(self):
        return (
            f"<Store {self.name} has {self.total_items} items. Among them {self.items_sold} items are sold today."
        )

    def sell_item(self, items: int):
        if self.items_sold + items > self.total_items:
            raise TooManyItemsSoldError(
                f"You have tried to sold {self.items_sold + items}, but store has only {self.total_items} items."
            )
        self.items_sold += items
        print(f"Store has sold {self.items_sold} items out of {self.total_items}.")


my_store = Store("Store 1", 100)
try:
    my_store.sell_item(30)
    my_store.sell_item(80)
except:
    pass
