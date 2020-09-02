"编写一个算法找出正数、小数、负数的立方根"

def cube_root(cube, epsilon):
 
    positive_num  = abs(cube)
    low = 0
    high = positive_num
    guess = (low + high) / 2. # guess = low + (high - low) / 2.  防止(low + high)大于 int ，即大于65535，而溢出的写发。
 
    while abs(guess**3 - positive_num) > epsilon:
        if guess**3 > positive_num:
            high = mid
        else:
            low = mid
 
        guess = (low + high) / 2. # guess = low + (high - low) / 2.  防止(low + high)大于 int ，即大于65535，而溢出的写发。
 
    return mid if cube>=0 else -mid
