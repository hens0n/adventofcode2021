class Lanternfish:
    def __init__(self, days=9):
        self.days = days

    def reset(self):
        self.days = 6

    def cycle(self):
        self.days -= 1
        if self.days < 0:
            self.reset()


def main():
    test_input = "3,4,3,1,2"
    live_input = "1,2,1,1,1,1,1,1,2,1,3,1,1,1,1,3,1,1,1,5,1,1,1,4,5,1,1,1,3,4,1,1,1,1,1,1,1,5,1,4,1,1,1,1,1,1,1,5,1,3,1,3,1,1,1,5,1,1,1,1,1,5,4,1,2,4,4,1,1,1,1,1,5,1,1,1,1,1,5,4,3,1,1,1,1,1,1,1,5,1,3,1,4,1,1,3,1,1,1,1,1,1,2,1,4,1,3,1,1,1,1,1,5,1,1,1,2,1,1,1,1,2,1,1,1,1,4,1,3,1,1,1,1,1,1,1,1,5,1,1,4,1,1,1,1,1,3,1,3,3,1,1,1,2,1,1,1,1,1,1,1,1,1,5,1,1,1,1,5,1,1,1,1,2,1,1,1,4,1,1,1,2,3,1,1,1,1,1,1,1,1,2,1,1,1,2,3,1,2,1,1,5,4,1,1,2,1,1,1,3,1,4,1,1,1,1,3,1,2,5,1,1,1,5,1,1,1,1,1,4,1,1,4,1,1,1,2,2,2,2,4,3,1,1,3,1,1,1,1,1,1,2,2,1,1,4,2,1,4,1,1,1,1,1,5,1,1,4,2,1,1,2,5,4,2,1,1,1,1,4,2,3,5,2,1,5,1,3,1,1,5,1,1,4,5,1,1,1,1,4"
    lanternfishes = [Lanternfish(int(l)) for l in test_input.split(',')]

    for i in range(1, 257):
        if i%50 == 0 :
            print(i)
        for lanternfish in lanternfishes:
            if lanternfish.days == 0:
                lanternfishes.append(Lanternfish())
            lanternfish.cycle()
        #output = ""
        # for lanternfish in lanternfishes:
        #     output += '{},'.format(lanternfish.days)
        #print('After  {} day:'.format(str(i).rjust(2)), output[:-1])


    print('Total of {} fish'.format(len(lanternfishes)) )


if __name__ == '__main__':
    main()
