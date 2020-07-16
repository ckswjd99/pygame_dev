from setting import *
from util import *
import poly

#---------- USE MANY ABSOLUTELY FAR POINTS, PREVENTING ERROR ----------#
points_absolutely_far = [(-2147483648, -2147483648), (2147483648, -2147483648), (-2147483648, 2147483648), (2147483648, 2147483648)]
points_absolutely_far_ext = [(-2147483648, -2147483648), (2147483648, -2147483648), (-2147483648, 2147483648), (2147483648, 2147483648), (2147483648, 0), (-2147483648, 0), (0, 2147483648), (0, -2147483648)]



#---------- TOPOLOGY CHECKER ----------#

def point_inside_poly(point, poly):
    result = []
    for PAF in points_absolutely_far_ext:
        num_crossing_line = 0
        for line in poly.lines:
            c_point = crossing_point(PAF, point, line.pos0, line.pos1)
            if c_point != False and points_in_line(PAF, c_point, point) and points_in_line(line.pos0, c_point, line.pos1):
                num_crossing_line += 1
        result.append(num_crossing_line%2)
    if result.count(0) < result.count(1):
        return True
    else:
        return False


def poly_collide(poly0, poly1):
    result = False
    for point in poly0.pos:
        if point_inside_poly(point, poly1):
            result = True
    for point in poly1.pos:
        if point_inside_poly(point, poly0):
            result = True
    return result;



#---------- TEST BENCH ----------#
if __name__ == "__main__":
    temp_poly = poly.poly( [(300,300), (600,300), (500,600), (300,600)], WHITE )
    check_point = (400,400)
    print("is Point Inside?")
    print(point_inside_poly(check_point, temp_poly))

    offset = (100,150)
    temp_poly2 = poly.poly( [(300+offset[0],300+offset[1]), (600+offset[0],300+offset[1]), (500+offset[0],600+offset[1]), (300+offset[0],600+offset[1])], WHITE )
    print("does Polys Collide?")
    print(poly_collide(temp_poly, temp_poly2))

    temp_poly.render()
    temp_poly2.render()
    pygame.gfxdraw.pixel(screen, check_point[0], check_point[1], WHITE)

    pygame.display.flip()