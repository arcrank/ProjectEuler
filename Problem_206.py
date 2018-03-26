"""
Max value is where all of the _ are 9's. Can pull out the last 0 and factor it back in later

"""
import math

def soln():
    max_val = math.ceil(math.sqrt(19293949596979899))



    def check_val(val):

        return not all(int(val[x*2]) == x+1 for x in range(0,9))


    while check_val(str(max_val*max_val)):
        max_val -= 1

    return max_val*10 #took the 10 out before


if __name__ == '__main__':
    print(soln())