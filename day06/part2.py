from collections import Counter
from collections import defaultdict


def breed(lanternfishes, days) -> int:
    fishcounter = defaultdict(int)
    counter = Counter(lanternfishes)
    fishcounter.update(counter)
    for _ in range(days):
        eight = fishcounter.get(0, 0)
        for i in range(9):
            if i == 8:
                fishcounter[i] = eight
            elif i == 6:
                fishcounter[i] = fishcounter.get(7, 0) + eight
            else:
                fishcounter[i] = fishcounter.get(i + 1, 0)
    return sum(fishcounter.values())


def example():
    print('input_example-----------')
    with open('input_example.txt') as f:
        input = f.read()
    lanternfishes = [int(l) for l in input.split(',')]
    assert breed(lanternfishes, 18) == 26
    print('after {} days, there are a total of {} fish'.format(18, breed(lanternfishes, 18)))
    assert breed(lanternfishes, 80) == 5934
    print('after {} days, there are a total of {} fish'.format(80, breed(lanternfishes, 80)))
    assert breed(lanternfishes, 256) == 26984457539
    print('after {} days, there are a total of {} fish'.format(256, breed(lanternfishes, 256)))


def main():
    example()
    print('input.txt-----------')
    with open('input.txt') as f:
        input = f.read()
    lanternfishes = [int(l) for l in input.split(',')]
    print('after {} days, there are a total of {} fish'.format(80, breed(lanternfishes, 80)))
    print('after {} days, there are a total of {} fish'.format(256, breed(lanternfishes, 256)))


if __name__ == '__main__':
    main()