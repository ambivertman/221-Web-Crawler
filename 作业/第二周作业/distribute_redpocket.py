import random


def distribute(num, result):
    if num == 1:
        result.append(amount - sum(result))
        return result

    maximum = (amount - sum(result))
    result.append(random.uniform(0.1, maximum))
    return distribute(num - 1, result)


number = 10  # eval(input("请输入红包的个数:"))
amount = 200  # eval(input("请输入红包的总金额:"))
distribution = []
distribute(number, distribution)
print(distribution)
