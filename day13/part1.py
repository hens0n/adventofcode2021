from collections import defaultdict

def fold_paper(paper, direction, along):
    folded_paper =defaultdict(lambda: False)
    # print('direction:{}, along:{}'.format(direction,along))
    for coordinate in paper.keys():
        if direction == "x":
            if coordinate[0] > along:                
                if paper[coordinate]:
                    new_x = (along*2)-coordinate[0]
                    folded_paper[new_x,coordinate[1]] = True
            elif coordinate[0] == along:
                pass
            else:
                if paper[coordinate]:
                    folded_paper[coordinate] = True
                

        if direction == "y": 
            if coordinate[1] > along: 
                if paper[coordinate]:
                    new_y = (along*2)-coordinate[1]
                    folded_paper[coordinate[0],new_y] = True
            elif coordinate[1] == along:
                pass
            else:
                if paper[coordinate]:
                    folded_paper[coordinate] = True


    return folded_paper


def print_paper(paper):
    max_x = 0
    max_y = 0
    for coordinate in paper.keys():
        if max_x < coordinate[0]:
            max_x = coordinate[0]
        if max_y < coordinate[1]:
            max_y = coordinate[1]

    for y in range(max_y+1):
        row = ""
        for x in range(max_x+1):
            if paper[x,y]:
                row += '#'
            else:
                row += '.'
        print(row)

def parse_input(input):
    paper =  defaultdict(lambda: False)
    folds = []

    for line in input:
        if ',' in line:

            x,y = [int(i.strip()) for i in line.split(",")]
            paper[x, y] = True
        elif "fold along " in line:
            folds.append(line.replace("fold along ",''))
    return paper, folds

def do_folds(paper, folds):
    i = 0
    for fold in folds:
        direction,along = fold.split('=')
        along = int(along)
        paper = fold_paper(paper,direction,along) 
        
        if i == 0:
            print('Dot counter after first fold:{}'.format(len(paper.values())))


        i+=1
    return paper

def main():
    
    example = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".splitlines()
# 

    paper,folds = parse_input(example)
    paper = do_folds(paper,folds)    
    print_paper(paper)

    with open("input.txt") as infile:
        input = [line.strip() for line in infile]


    paper,folds = parse_input(input)
    paper = do_folds(paper,folds)    
    print_paper(paper)



if __name__ == '__main__':
    main()