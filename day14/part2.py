from collections import defaultdict
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


def pair_insertion(polymer,rules,steps):
    count_letters = Counter(polymer)
    
    if steps == 0:
        print(count_letters)
    if steps > 0:
        pairs = []
        for i in range(len(polymer)-1):
            pairs.append('{}{}'.format(polymer[i],polymer[i+1]))
        count_pairs = Counter(pairs)
        for i in range(steps): 
            new_template =defaultdict(int) 
            # print('step: {}'.format(i+1))
            for pair in count_pairs.keys():
                count_letters[rules[pair]] += count_pairs[pair]
                child_left = '{}{}'.format(pair[0],rules[pair])
                child_right = '{}{}'.format(rules[pair],pair[1])
                # print("Pair:{}, Rule:{}, Left: {}, Right: {}, Merge:{}".format(pair,
                    # rules[pair],child_left,child_right,pair[0]+rules[pair]+pair[1]))
                new_template[child_left]+=count_pairs[pair]
                new_template[child_right]+=count_pairs[pair]
            count_pairs = new_template

    find_max = max(count_letters.values())
    find_min =min(count_letters.values())

    print('Steps:{}, Max:{}, Min:{}, Dif:{}'.format(steps,find_max,find_min,find_max-find_min))


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

    rules, template  = parse_input(example)
    print('Template:     {}'.format(template))
    pair_insertion(template,rules,10)
    pair_insertion(template,rules,40)


    with open("input.txt") as infile:
        input = [line.strip() for line in infile]
    rules, template  = parse_input(input)
    print('Template:     {}'.format(template))
    pair_insertion(template,rules,10)
    pair_insertion(template,rules,40)



if __name__ == '__main__':
    main()