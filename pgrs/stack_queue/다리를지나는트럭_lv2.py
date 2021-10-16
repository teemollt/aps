def solution(bridge_length, weight, truck_weights):
    answer = 0
    l, w, t = bridge_length, weight, truck_weights
    on = [0] * l
    while on:
        answer += 1
        on.pop(0)
        if t:
            if sum(on) + t[0] <= w:
                on.append(t.pop(0))
            else:
                on.append(0)
    return answer