# mean function for list
def mean(x):
    """
    mean(x)
    Returns the mean of x.
    """
    # calculate the sum of x
    sum_x = sum(x)
    # calculate the mean of x
    mean_x = sum_x / len(x)
    return mean_x

# pearson correlation coefficient test function
def pearson_correlation_coefficient(x, y):
    """
    pearson_correlation_coefficient(x, y)
    Returns the Pearson correlation coefficient of x and y.
    """
    # check if x and y are of same length
    if len(x) != len(y):
        raise ValueError("The length of x and y must be the same.")
    # check if x and y are of same length
    if len(x) < 2:
        raise ValueError("The length of x and y must be greater than 2.")
    # calculate the mean of x and y
    x_mean = mean(x)
    y_mean = mean(y)

    # calculate the numerator
    numerator = 0
    for i in range(len(x)):
        numerator += (x[i] - x_mean) * (y[i] - y_mean)
    # calculate the denominator
    denominator_x = 0
    for i in range(len(x)):
        denominator_x += (x[i] - x_mean) ** 2
    denominator_y = 0
    for i in range(len(y)):
        denominator_y += (y[i] - y_mean) ** 2
    denominator = (denominator_x * denominator_y) ** (1 / 2)

    # calculate the pearson correlation coefficient
    r = numerator / denominator
    return r

testx = [1, 2, 3, 4, 5]
testy = [10, 9, 8, 7, 6]
print(mean(testx))
print(pearson_correlation_coefficient(testx, testy))