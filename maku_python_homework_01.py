class FizzBuzz():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def play(self):
        for i in range(self.start, self.end + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

    def play_stage_2(self):
        for i in range(self.start, self.end + 1):
            if (i % 3 == 0 or '3' in str(i)) and (i % 5 == 0 or '5' in str(i)):
                print("FizzBuzz")
            elif i % 3 == 0 or '3' in str(i):
                print("Fizz")
            elif i % 5 == 0 or '5' in str(i):
                print("Buzz")
            else:
                print(i)

def main():
    game = FizzBuzz(1, 100)
    game.play()

    print("--------------------------------")

    game.play_stage_2()

if __name__ == "__main__":
    main()