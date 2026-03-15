def f(x, y, s):
    if x+y <= 100: return s % 2 ==0
    if s ==0 : return False
    h = [f(x-3,y,s-1), f(if x+y % 2 ==0: x// 3,y,s-1), f(x,y-3,s-1), f(x, if x+y%2 ==0: y //3,s-1)]
    return any(h) if (s - 1) % 2 == 0 else any(h)
print('19', [x for x in range(53, 300) if f(x,48, 2)])
print('20', [x for x in range(53,300) if f(x, 48, 3) and not f(x, 48, 1)])
print('21', [x for x in range(53,300) if f(x, 48, 4)and not f(x,48,2 )])