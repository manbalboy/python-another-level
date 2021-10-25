class Item:
    def __init__(self, name, price, weight, isDropAble):
        self.name = name
        self.price = price
        self.weight = weight
        self.isDropAble = isDropAble

    def sale(self):
        print(f"{self.name} 판매 가격은 {self.price}")

    def discard(self):
        if self.isDropAble:
            print("버렸습니다.")
        else:
            print("버릴수 없습니다.")


class WearableItem(Item):
    def __init__(self, name, price, weight, isDropAble, effect):
        super().__init__(name, price, weight, isDropAble)
        self.effect = effect

    def wear(self):
        print(f"{self.name} 장착 {self.effect}")


class UsableItem(Item):
    def __init__(self, name, price, weight, isDropAble, effect):
        super().__init__(name, price, weight, isDropAble)
        self.effect = effect

    def use(self):
        print(f"{self.name} 소모 {self.effect}")


wearableItem = WearableItem("옷", 10000, 10, True, "반짝")
useAbleItem = UsableItem("약", 10000, 10, False, "반짝")
wearableItem.discard()
wearableItem.sale()
wearableItem.wear()
useAbleItem.discard()
useAbleItem.sale()
useAbleItem.use()
