class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
#    def __init__(self):
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r+')
        return file.read()
        file.close()

    def add(self, *products):
        for product in products:
            if self.get_products().find(f'{product.name},') == -1:
                file = open(self.__file_name, 'a')
                file.write(f'{product.name}, {product.weight}, {product.category}\n')
                file.close()
            else:
                for line in self.get_products():
                    if line.startswith(product.name):
                        existing_weight = float(line.split(',')[1].strip())
                        new_weight = existing_weight + product.weight
#                print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {product.weight}')
                        print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {new_weight}')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())