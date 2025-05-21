def conditional_odd_series(a):
    result = []
    i = 1
    while i <= a:
        result.append(i)
        i += 2
    print(", ".join(map(str, result)))

conditional_odd_series(10)  
