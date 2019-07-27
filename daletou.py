import random

def redball():
    redball = []
    n = 1
    while n < 6:
        a = random.randint(1,35)
        redball.append(a)
        n += 1
    print('红球：%s'%redball)


def blueball():
    blueball = []
    m = 1
    while m < 3:
        b = random.randint(1,12)
        blueball.append(b)
        m += 1
    print('蓝球：%s'%blueball)


if __name__ == '__main__':
    print('---------------------------本期大乐透开奖结果---------------------------')
    redball()
    blueball()
    print('---------------------------祝君好运，恭喜发财---------------------------')
