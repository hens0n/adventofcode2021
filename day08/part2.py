from collections import Counter


class Sevensegment:
    def __init__(self):
        self.top = '*'
        self.top_right = '*'
        self.bottom_right = '*'
        self.bottom = '*'
        self.bottom_left = '*'
        self.top_left = '*'
        self.center = '*'

    def __str__(self):
        rtn = " {}\n".format(self.top * 4)
        rtn += "{}    {}\n".format(self.top_left, self.top_right)
        rtn += "{}    {}\n".format(self.top_left, self.top_right)
        rtn += " {}\n".format(self.center * 4)
        rtn += "{}    {}\n".format(self.bottom_left, self.bottom_right)
        rtn += "{}    {}\n".format(self.bottom_left, self.bottom_right)
        rtn += " {}\n".format(self.bottom * 4)
        return rtn

    def __repr__(self):
        return "Test a:% s b:% s"


def find_number_by_length(length, patterns) -> str:
    for item in patterns:
        if len(item) == length:
            return item


def letters_in_string(letters, string):
    rtn = True
    for l in letters:
        if l not in string:
            rtn = False
    return rtn


def find_number(length, segments, patterns):
    for item in patterns:
        if len(item) == length:
            if letters_in_string(segments, item):
                return item


def substract_strings(string1, string2):
    rtn = ""
    for i in string1:
        if i not in string2:
            rtn += i
    return rtn


def main():
    answer = 0
    with open('input.txt') as f:
        lines = f.readlines()
    # lines = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    total = 0
    for line in lines:
        display = Sevensegment()
        # print(line.strip())
        pattern, digits = line.split("|")
        pattern_list = ["".join(sorted(p.strip())) for p in pattern.split(' ') if len(p) > 0]
        digits_list = ["".join(sorted(p.strip())) for p in digits.split(' ') if len(p) > 0]

        one = find_number_by_length(2, pattern_list)
        four = find_number_by_length(4, pattern_list)
        seven = find_number_by_length(3, pattern_list)
        eight = find_number_by_length(7, pattern_list)
        three = find_number(5, one, pattern_list)

        display.top = substract_strings(seven, one)
        display.top_left = substract_strings(four, three)
        display.bottom = substract_strings(substract_strings(three, four), seven)
        display.center = substract_strings(substract_strings(three, seven), display.bottom)
        zero = substract_strings(eight, display.center)
        display.bottom_left = substract_strings(substract_strings(eight, three), display.top_left)
        nine = substract_strings(eight, display.bottom_left)
        six = "".join(sorted([display.top, display.top_left, display.center, display.bottom_left, display.bottom]))
        six = find_number(6, six, pattern_list)
        display.top_right = substract_strings(eight, six)
        display.bottom_right = substract_strings(one, display.top_right)
        five = substract_strings(six, display.bottom_left)
        two = substract_strings(substract_strings(eight, display.top_left), display.bottom_right)
        # print(display)

        lookup = {
            "".join(sorted(zero)): '0',
            "".join(sorted(one)): '1',
            "".join(sorted(two)): '2',
            "".join(sorted(three)): '3',
            "".join(sorted(four)): '4',
            "".join(sorted(five)): '5',
            "".join(sorted(six)): '6',
            "".join(sorted(seven)): '7',
            "".join(sorted(eight)): '8',
            "".join(sorted(nine)): '9'
        }
        output = ""

        for d in digits_list:
            output += lookup[d]
        answer += int(output)
        # print(output)
        print(answer)


if __name__ == '__main__':
    main()
