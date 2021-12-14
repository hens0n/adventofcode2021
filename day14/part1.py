
from collections import Counter

def parse_input(input):
    rules =  {}
    template = ""
    i = 0
    for line in input:
        if i == 0:
            template = line.strip()
        i+=1
        if ' -> ' in line:
            temp = line.split(' -> ')
            rules[temp[0]] = temp[1]
    return rules, template


def apply_rules(rules,template):
    pairs = []
    new_pairs = []
    for i in range(len(template)-1):
        pairs.append('{}{}'.format(template[i],template[i+1]))

    for pair in pairs:
        new_pairs.append('{}{}'.format(pair[0],rules[pair]))
    new_pairs.append(template[len(template)-1])
    return ''.join(new_pairs)


def grow(template,rules, steps):
    for i in range(steps):
        template = apply_rules(rules,template)
        print('After step {}: Len {}'.format(i+1,len(template)))
        counts = Counter(template)
        # print(counts)
        find_max = max(counts.values())
        find_min =min(counts.values())
    print('Max:{}, Min:{}, Dif:{}'.format(find_max,find_min,find_max-find_min))



def main():

    example = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".splitlines()

    with open("input.txt") as infile:
            input = [line.strip() for line in infile]

    rules, template  = parse_input(example)
    print('Template:     {}'.format(template))
    # print(rules) 
    grow(template,rules,10)


    rules, template  = parse_input(input)
    print('Template:     {}'.format(template))
    # print(rules) 
    grow(template,rules,10)

    




if __name__ == '__main__':
    main()