class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self, file_name='products.txt'):
        self.__file_name = file_name
        prod_db = open(self.__file_name, 'a')
        prod_db.close()

    def get_products(self):
        prod_db = open(self.__file_name, 'r')
        prod_all = prod_db.read()
        prod_db.close()
        return prod_all

    def add(self, *products):
        prod_all = self.get_products()
        for product in products:
            if product.name in prod_all:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as prod_db:
                    prod_db.write(str(product) + '\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
