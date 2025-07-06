## 为了表示这个Bowling游戏，我们做如下约定，该约定与 “维基百科-保龄球-记分方式-传统方式” 的约定一致
## https://zh.wikipedia.org/wiki/%E4%BF%9D%E9%BD%A1%E7%90%83
## 1. 一局游戏由10轮组成，每轮有2次投球机会，每轮游戏之间使用空格分割；
## 2. 如果第一次投球击倒10个瓶子，记为X，该轮结束；
## 3. 如果第一次投球没有击倒10个瓶子，第二次击倒所有剩余的瓶子，则记为第一次的击倒瓶子数量和/；如 7/
## 4. 如果第一次投球没有击倒10个瓶子，第二次击倒部分剩余的瓶子，则记为第一次的击倒瓶子数量和第二次击倒瓶子数量；如42
## 5. 如果一次击球没有击倒瓶子，则记为-；如1-

## Reference
## https://www.topendsports.com/sport/tenpin/scoring.htm
## https://en.wikipedia.org/wiki/Tenpin_bowling
## https://www.activesgcircle.gov.sg/learn/bowling/how-are-points-determined-in-bowling
## Use this calculator to verify: https://www.bowlinggenius.com/
##

## Frame      1   2   3   4   5   6   7   8   9   10       Score
##            X   X   X   X   X   X   X   X   X   XXX      300
##            1-  1-  1-  1-  1-  1-  1-  1-  1-  1-       10
##            X   9/  5/  72  X   X   X   9-  8/  9/X      187
##            5/  5/  5/  5/  5/  5/  5/  5/  5/  5/5      150

import re

def get_rolls(game):
    frames = re.split(r'\s+', game.strip())
    rolls = []

    for i, frame in enumerate(frames):
        if i < 9:
            if frame == 'X':
                rolls.append(10)
            else:
                first, second = frame[0], frame[1]
                if first == '-':
                    roll_first = 0
                else:
                    roll_first = int(first)

                if second == '/':
                    roll_second = 10 - roll_first
                elif second == '-':
                    roll_second = 0
                else:
                    roll_second = int(second)

                rolls.append([roll_first, roll_second])
        else:
            roll_last = []
            for roll in frame:
                if roll.isdigit():
                    roll_last.append(int(roll))
                    already = int(roll)
                elif roll == 'X':
                    roll_last.append(10)
                    already = 10
                elif roll == '-':
                    roll_last.append(0)
                    already = 0
                elif roll == '/':
                    roll_last.append(10 - already)
            rolls.append(roll_last)

    return rolls

def sum_score(rolls):
    score = 0

def main():
    game1 = "X   X   X   X   X   X   X   X   X   XXX"
    rolls1 = get_rolls(game1)
    print("rolls1:", rolls1)

    game2 = "1-  1-  1-  1-  1-  1-  1-  1-  1-  1-"
    rolls2 = get_rolls(game2)
    print("rolls2:", rolls2)

    game3 = "X   9/  5/  72  X   X   X   9-  8/  9/X"
    rolls3 = get_rolls(game3)
    print("rolls3:", rolls3)
    
    game4 = "5/  5/  5/  5/  5/  5/  5/  5/  5/  5/5"
    rolls4 = get_rolls(game4)
    print("rolls4:", rolls4)


if __name__ == "__main__":
    main()