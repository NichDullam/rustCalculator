class Calc:
    items = {
      "rockets" : {
        "explosives" : 10,
        "gunpowder" : 150,
        "metal pipe" : 2
      },
      "explosives" : {
        "gunpowder" : 50,
        "sulfur" : 10,
        "metal fragments" : 10,
        "low-grade" : 3
      },
      "gunpowder" : {
        "quantity" : 10,
        "charcoal" : 30,
        "sulfur" : 20
      },
      "c4" : {
        "explosives" : 20,
        "tech trash" : 2,
        "cloth" : 5
      }
    }

    def inputMain(self, total = {}):
        cont = True
        while cont:
            contQuantity = True
            name = input("--- Item Name --- \n").lower()
            if self.interpretRequest(name):
                instance = self.items[name]
                base = self.setBase(instance)
                while contQuantity:
                    quantity = int(input("--- Item Quantity --- \n"))
                    if type(quantity) != bool:
                        contQuantity = False
                        total = self.traceback(base, quantity)
                        for i in total:
                            print("Material: {}, Quantity: {}".format(i, total[i]))



    def interpretRequest(self, name):
        if name in self.items:
            print("Item Found")
            return True

        elif name not in self.items:
            print("Item not found")
            return False
#MAJOR CHANGES NEEDED
    def traceback(self, base, quantity, total = {}):
        for broad in base:
            if broad != "quantity" :
                try:
                    units = base[broad] / base["quantity"]
                except KeyError:
                    units = base[broad]

                try:
                    spread = self.items[broad]
                    newQuantity = quantity * units
                    self.traceback(spread, newQuantity, total)

                except KeyError:
                    if broad in total:
                        total[broad] = total[broad] + units * quantity
                    else:
                        total[broad] = units * quantity

        return total

    def adjustTotal(self, total, quantity):
        for material in total:
            total[material] = total[material] * quantity
        return total

    def setBase(self, instance):
        base = {}
        for i in instance:
            base[i] = instance[i]
        return base

    def main():
        self.inputMain()

calc1 = Calc()

testing = calc1.inputMain()
for i in testing:
    print("Material: {}, Quantity: {}".format(i, testing[i]))
