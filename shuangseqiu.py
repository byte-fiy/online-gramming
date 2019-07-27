import random

def redball():
    redball = []
    n = 1
    while n < 7:
        a = random.randint(1,33)
        redball.append(a)
        n += 1
    print('红球：%s'%redball)


def blueball():
    blueball = random.randint(1,16)
    print('蓝球：%s'%blueball)


if __name__ == '__main__':
    print('---------------------------本期双色球开奖结果---------------------------')
    redball()
    blueball()
    print('---------------------------祝君好运，恭喜发财---------------------------')
