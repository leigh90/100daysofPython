import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint_calc(height,width,cover):
    to_paint = (height * width) / cover
    cans = math.ceil(to_paint)
    print(f'You will need {cans} of paint')

paint_calc(height=test_h, width=test_w, cover=coverage)