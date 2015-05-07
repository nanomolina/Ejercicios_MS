def maxP(k):
    max_val = 0.0
    #buesco evaluando en el intervalo (1, k) el maximo f(i)/g(i)
    for i in range(k + 1):
        div = f(i) / g(i)
        max_val = max(max_val, div)
    return max_val


def rechazo(k):
    while True:
        var_random1 = random()
        var_random2 = random()
        # Y es una v.a que pertenece al intervalo (1, k)
        Y = int((k + 1) * var_random1) + 1
        max_val = maxP(k)
        p_Y = f(Y)
        q_Y = g(Y)
        if var_random2 <= p_Y/(max_val * q_Y):
            result = Y
            break
    return result
