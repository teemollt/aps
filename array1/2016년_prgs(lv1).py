def solution(a, b):
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    w = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    d = sum(m[:a]) - m[a-1] + b
    return w[d%7]