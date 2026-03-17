# homework7

"""homework 7"""


def hw7_1(a):
    """BRIDGES"""
    t = abs(a)
    h = (t // 60) % 24
    m = t % 60
    dig_h = [int(d) for d in str(h)]
    dig_m = [int(m) for m in str(m)]
    return sum(dig_h) + sum(dig_m)


def hw7_2(b):
    """EXP"""
    exp = 10
    new_exp = b + exp
    lv_dict = {1: 15, 2: 25, 3: 35, 4: 45}
    for level, required in lv_dict.items():
        if new_exp == required:
            return True
    return False


def hw7_3(h, m):
    """HOURS"""
    if h < 12:
        period = "a.m."
    else:
        period = "p.m."

    if h == 0 or h == 12:
        hours = 12
    elif h > 12:
        hours = h - 12
    else:
        hours = h

    time = f"{hours}:{m:02d} {period}"
    return time
