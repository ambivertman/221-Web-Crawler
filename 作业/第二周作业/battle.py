import random


# 定义player类
class Player:
    def __init__(self, name, HP, attack):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.score = 0


# 开始游戏进程
while True:
    is_continue = input("是否开始游戏(点击Q退出,点击任意键继续):")
    if is_continue in "qQ":
        print("游戏退出!")
    else:
        print("游戏开始!")
        for i in range(3):
            # 为对战双方赋予属性
            player1 = Player("奥特曼", 150, 30)
            player2 = Player("小怪兽", 120, 40)
            print(f"Round {i + 1}")
            while player1.HP > 0 and player2.HP > 0:
                attack1 = int(player2.attack * random.uniform(0.8, 1.2))
                attack2 = int(player1.attack * random.uniform(0.8, 1.2))
                player1.HP -= attack1
                player2.HP -= attack2
                print(f"{player1.name}受到了{attack1}点伤害.")
                print(f"{player2.name}受到了{attack2}点伤害.")

            if player1.HP > 0 and player2.HP <= 0:
                print(f"{player2.name}被击败了")
                player1.score += 1
            elif player1.HP <= 0 and player2.HP > 0:
                print(f"{player1.name}被击败了")
                player2.score += 1
            else:
                print("平局")
        print("大比分:", end='')
        if player1.score > player2.score:
            print(f"{player1.name}赢啦")
        elif player1.score < player2.score:
            print(f"{player2.name}赢啦")
        else:
            print("平局")
