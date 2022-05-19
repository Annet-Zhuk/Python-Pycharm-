def deposit(arg):
    name, money = arg
    bank[name] = bank.setdefault(name, 0) + int(money)


def withdraw(arg):
    name, money = arg
    bank[name] = bank.setdefault(name, 0) - int(money)


def balance(arg):
    name = arg[0]
    if name in bank:
        print(bank[name])
    else:
        print('ERROR')


def transfer(arg):
    name_1, name_2, money = arg
    withdraw((name_1, money))
    deposit((name_2, money))


def income(arg):
    percent = int(arg[0])
    for name, balanse in bank.items():
        if balanse > 0:
            bank[name] = bank.get(name) + balanse * percent // 100
bank = {}
bank_fun = {'DEPOSIT': deposit, 'WITHDRAW' : withdraw, 'BALANCE' : balance,
            'TRANSFER' : transfer, 'INCOME' : income}
for _ in range(int(input())):
    data = input().split()
    fun_name = data[0]
    arg = data[1:]
    bank_fun[fun_name](arg)
