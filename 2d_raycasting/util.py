import pygame
from numpy import *


# ---------- UTILS ----------#

def distance_between(pos0, pos1):
    x1 = pos0[0]
    x2 = pos1[0]
    y1 = pos0[1]
    y2 = pos1[1]

    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def crossing_point(pos00, pos01, pos10, pos11):
    x1 = pos00[0]
    x2 = pos01[0]
    x3 = pos10[0]
    x4 = pos11[0]
    y1 = pos00[1]
    y2 = pos01[1]
    y3 = pos10[1]
    y4 = pos11[1]

    if (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4) == 0 or (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4) == 0:
        return False

    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
                (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
                (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

    return (px, py)


def points_in_line(pos0, pos1, pos2):
    if pos0 == pos1:
        return True
    elif pos1 == pos2:
        return True
    elif pos0 == pos2 and pos0 != pos1:
        return False

    err = 2  # allowed error
    vec1 = (pos1[0] - pos0[0], pos1[1] - pos0[1])
    dist = distance_between(pos1, pos2)
    vec1 = (vec1[0] / distance_between((0, 0), vec1) * dist, vec1[1] / distance_between((0, 0), vec1) * dist)
    pos2_go = (pos1[0] + vec1[0], pos1[1] + vec1[1])
    if distance_between(pos2_go, pos2) < err:
        return True
    else:
        return False