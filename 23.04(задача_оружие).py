# file1 = open('test.txt','a')
# file1.write('\n'+'test append')
# file1.close()




data = {
    'glock.20':2000,
    'usp':2500,
    'fs':3467,
    'deagle':5000,
    'p92':4000,
    'colt':90000,
    'magnum':6000,
    'p90':10000,
    'mp7':11000,
    'uzi':12000,
    'mp5':14000,
    'm16':20000,
    'ak-47':19000,
    'm416':24000,
    'famas':21000,
    'AWM':30000,
    'Dragunov':31000,
    'Barett':50000,
    'RPG':100000,
    'Topol-M':2000000
}


"""
ТЗ:
По данным введенным пользователем вычислить, сможет он купить выбранный им товар или нет.
Если товар в списке отсутствует - NOT OK
__________
Входные данные: название товара,кол-во товара, наличные
Реализовать 2+ функциями
Выходные данные: словарь состящий из: 
{названия товара как ключ:кол-во, следующий элемент - потраченная сумма - ключ, значение сумма}
"""

dict1 = {}

def count_money(price,quantity,cash):
    return cash - price * quantity

count_money(2500,1,5000)



def order(product,quantity,cash):

    if product in data:
        print(data[product])
        payback = count_money(data[product],quantity,cash)
        print(payback)
        dict1[product].append(data[product])
        print(dict1)
        if payback < 0:
            print("У вас не хватает денег!")
    else:
        print("Такого товара нет")

order("mp5",1,5000)



