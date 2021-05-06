def fibonacci(num):
    series = []
    i,j=1,1
    while(i<=num):
        if(i<=num):
            series.append(i)
        if(j<=num):
            series.append(j)
        i+=j
        j+=i
    return series

series = fibonacci(13)
