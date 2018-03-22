import csv
import os
from data_types import Purchase
import statistics

def main():
    print_header()
    filename = get_data_file()
    purchase_data = load_file(filename)
    query_data(purchase_data)

def print_header():
    print('----------------------------------------')
    print('         REAL ESTATE ANALYZER APP')
    print('----------------------------------------')
    print()

def get_data_file():
    base_folder =  os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')

def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)
        return purchases


def query_data(data):
    data.sort(key=lambda p: p.price)
    high_purchase = data[-1]
    print("The most expensive house is ${:,}.".format(high_purchase.price))

    low_purchase = data[0]
    print("The least expensive house is ${:,}.".format(low_purchase.price))

    prices = [
        p.price
        for p in data
    ]


    print("The average priced house is ${:,}.".format(round(statistics.mean(prices))))

    bed_prices = [
        p.price
        for p in data
        if p.beds == 2
    ]

    print("The average price of a 2 bedroom house is ${:,}.".format(round(statistics.mean(bed_prices))))

if __name__ == '__main__':
    main()