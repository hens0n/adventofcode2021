import sys


def position_cost(crabs, position):
    cost = 0
    for c in crabs:
        # print('position:{}, start:{}, cost:{}'.format(position,c, abs(position-c)))
        cost += abs(position - c)
    # print('Total Cost:{}'.format(cost))
    return cost


def main():
    with open('input.txt') as f:
        input = f.read()
    crab_positions = [int(i) for i in input.split(',')]
    # print(crab_positions)
    cheapest_cost = sys.maxsize
    cheapest_position = 0
    max_position = max(crab_positions)
    min_position = min(crab_positions)
    for i in range(min_position, max_position + 1):
        cost = position_cost(crab_positions, i)
        if cost < cheapest_cost:
            cheapest_cost = cost
            cheapest_position = i

    print('Cheapest position:{}, Cheapest Cost:{}'.format(cheapest_position, cheapest_cost))


if __name__ == '__main__':
    main()
