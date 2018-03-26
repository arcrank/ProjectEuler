def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True



Lychrel = 0

for i in range(0,10001):
    temp = True
    k = 0
    while temp and k < 50:

        if isPalindrome(str(i)):
            temp = False

        if not isPalindrome(str(i)):
            r = int(str(i)[::-1])

            

        while a == False:

            for j in range(0,49):



                reve = int(str(ate)[::-1])

                if isPalindrome(str(ate+reve)):
                    print('palindrome found', i)
                    a = True
                    break



                ate = ate + reve
                if j == 49:
                    print('Lychecl nubmer at ',i)
                    Lychrel += 1
                    a = True


    print('current lycrhels',Lychrel)