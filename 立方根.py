"编写一个算法找出正数、小数、负数的立方根"

def cube_root(cube, error_value):
 
    positive_num  = abs(cube)
    low = 0
    high = positive_num
    guess = (low + high) / 2.
 
    while abs(guess**3 - positive_num) > epsilon:
        if guess**3 > positive_num:
            high = mid
        else:
            low = mid
 
        guess = (low + high) / 2.
 
    return mid if num>=0 else -mid
