from collections import defaultdict


def parse_input(input):
    target_area = defaultdict(lambda: False)

    input = input.replace('target area: ','')
    input = input.split(', ')

    xs = input[0].split('..')
    ys = input[1].split('..')

    x = int(xs[0].replace('x=',''))
    x2 = int(xs[1])
    
    y = int(ys[0].replace('y=',''))
    y2 = int(ys[1])

    x_list = [x,x2]
    y_list = [y,y2]

    for i in range(min(x_list),max(x_list)+1):
        for j in range(min(y_list),max(y_list)+1):
            target_area[i, j] = True

    return target_area, min(y_list)

def calc_velocity(x,y):


    if x > 0 :
        x += -1
    elif x < 0:
        x += 1
    else:
        x=0


    y += -1

    return x,y


def fire_probe(target_area,max_depth,vx,vy):
    x,y=0,0
    max_y = 0 


    while not y < max_depth and not target_area[x,y]:
    # for _ in range(8):
        x +=vx
        y +=vy
        if y > max_y:
            max_y = y
        vx,vy = calc_velocity(vx,vy)
        # print('x:{},y:{}'.format(x,y))        
        # print('vx:{},vy:{}'.format(vx,vy))
        # print(y < max_depth)
        if target_area[x,y]:
            # print('Max Y:{}, Hit Target:{},{}'.format(max_y,x,y))
            return True, max_y
    return False, 0





def main():


    example = "target area: x=20..30, y=-10..-5"
    input = "target area: x=70..96, y=-179..-124"
    max_y = 0
    target_area,max_depth = parse_input(example)
    hit_count =0
    # print(target_area)
    for x in range(40):
        for y in range(-20,20):
            hit,ma_y = fire_probe(target_area,max_depth,x,y)
            if hit:
                hit_count += 1
                if ma_y > max_y:
                    max_y = ma_y

    print('max_y',max_y)
    print('hit_count',hit_count)
    

    # 
    # if hit: 


    target_area,max_depth = parse_input(input)
    # print(target_area)
    max_y = 0
    hit_count =0
    for x in range(100):
        for y in range(-200,200):
            hit,ma_y = fire_probe(target_area,max_depth,x,y)
            if hit:
                hit_count += 1
                if ma_y > max_y:
                    max_y = ma_y

    print('max_y',max_y)
    print('hit_count',hit_count)
    










if __name__ == '__main__':
    main()