class Bill:
    def __init__(self, amount):
        if amount < 0:
            raise ValueError('Negative Value')
        elif not isinstance(amount, int):
            raise TypeError('Amount not an integer')
        else:
            self.amount = amount

    def __int__(self):
        return self.amount

    def __str__(self):
        return 'A {}$ bill'.format(self.amount)

    def __repr__(self):
        return 'A {}$ bill'.format(self.amount)

    def __lt__(self,other):
        return self.amount < other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)


class BillBatch:
    def __init__(self, lst):
        for i in lst:
            if not isinstance(i, Bill):
                raise TypeError('Element not a type of Bill')
        self.batch = lst

    def __len__(self):
        return len(self.batch)

    def total(self):
        total = 0
        for bill in self.batch:
            total += bill.amount

        return total

    def __getitem__(self, index):
        if index > len(self.batch) - 1 or index < -len(self.batch):
            raise IndexError('Index out of range')
        else:
            return self.batch[index]

    def __str__(self):
        return str(self.batch)

    def __repr__(self):
        return str(self.batch)


class CashDesk:
    def __init__(self):
        self.money = []

    def take_money(self, money):
            if not isinstance(money, Bill) and not isinstance(money, BillBatch):
                raise TypeError('Invalid argument')
            else:
                self.money.append(money)

    def total(self):
        total = 0
        for bill in self.money:
            if isinstance(bill, Bill):
                total += bill.amount
            else:
                total += bill.total()

        return 'We have a total of {}$ in the desk'.format(total)

    def __to_list(self, money):
        lst = []
        for mns in self.money:
            if isinstance(mns, Bill):
                lst.append(mns)
            else:
                for i in mns:
                    lst.append(i)
        return lst
        

    def __sort_lst(self, money):
        return sorted(money)

    def __to_dictionary(self,money):
        sorted_lst = self.__sort_lst(self.__to_list(money))
        return {x: sorted_lst.count(x) for x in sorted_lst}

    def inspect(self):
        print('We have the following count of bills, sorted in ascending order')
        dictionary = self.__to_dictionary(self.money)
        for key in dictionary:
            print(f'{key} - {dictionary[key]}')



def main():
    values=[100, 10, 50, 20, 100, 100, 100]
    bills=[Bill(value) for value in values]

    batch=BillBatch(bills)
    desk=CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))   

    print(desk.total())  # 390
    desk.inspect()


if __name__ == '__main__':
    main()
