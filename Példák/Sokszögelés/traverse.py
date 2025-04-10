from math import cos, sin, atan2, sqrt, degrees, radians


def dms2deg(dms):
    sign = 1
    if dms[0] == "-":
        sign = -1
        dms = dms[1:]
    
    d, m, s = dms.split("-")
    return sign * (int(d) + int(m) / 60 + float(s) / 3600)


def deg2dms(deg):
    sign = 1
    if deg < 0:
        sign = -1
    
    deg = abs(deg)
    d = int(deg)
    m = int((deg - d) * 60)
    s = (deg - d - m / 60) * 3600
    d *= sign

    return f"{d:d}-{m:02d}-{s:02f}"


def load_coords(filepath, header):
    with open(filepath) as file:
        coords = {}
        if header:
            next(file)
        for row in file:
            pt, y, x = row.strip().split(",")
            coords[pt] = (float(y), float(x))
        
    return coords


def load_obs(filepath, header):
    with open(filepath) as file:
        obs = {}
        if header:
            next(file)
        for row in file:
            st, pt, b, r = row.strip().split(",")
            obs[(st, pt)] = (
                dms2deg(b),
                float(r) if r else None
            )
        
    return obs


def pol(y, x):
    r = sqrt(y**2 + x**2)
    delta = degrees(atan2(y, x))
    return r, delta % 360


def rec(r, delta):
    y = sin(radians(delta)) * r
    x = cos(radians(delta)) * r
    return y, x


def weigthed_avg(values, weights):
    scaled = [v * w for v, w in zip(values, weights)]
    return sum(scaled) / sum(weights)   


def orient(coords, obs, st, pts):
    l0 = []
    ranges = []
    
    y0, x0 = coords[st]
    for pt in pts:
        yi, xi = coords[pt]
        li, _ = obs[(st, pt)]
        ri, di = pol(yi - y0, xi - x0)
        ranges.append(ri)
        l0.append((di - li) % 360)

    return weigthed_avg(l0, ranges) % 360


coo = load_coords("...", True) # valami fajl elresei ut
obs = load_obs("...", True) # valami fajl elresei ut

l0_start = orient(coo, obs, "2305", ["813", "1106", "3254"])
print(deg2dms(l0_start))
