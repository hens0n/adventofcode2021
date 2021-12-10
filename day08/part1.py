from collections import Counter


def find_number_by_length(length, patterns) -> str:
    for item in patterns:
        if len(item) == length:
            return item


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        # print(line.strip())
        pattern, digits = line.split("|")
        pattern_list = ["".join(sorted(p.strip())) for p in pattern.split(' ') if len(p) > 0]
        digits_list = ["".join(sorted(p.strip())) for p in digits.split(' ') if len(p) > 0]

        counter = Counter(digits_list)

        one = find_number_by_length(2, pattern_list)
        four = find_number_by_length(4, pattern_list)
        seven = find_number_by_length(3, pattern_list)
        eight = find_number_by_length(7, pattern_list)
        total += (counter[one] + counter[four] + counter[seven] + counter[eight])

    print('Totals(1,4,7,8): {}'.format(total))


if __name__ == '__main__':
    main()
