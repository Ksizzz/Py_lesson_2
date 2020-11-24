
def my_f(n):
    lt = n.split(' ')
    for el in lt:
        for i in el:
            s = ord(i)
            n_word = ""
            for s in range(99, 122):
            # if s >= 97 or s <= 122 or s == 32:
                n_word = n_word + i
                # return n_word

                print(n_word)
my_f('nice авп ъghj jапро hjjпаро вапрghgh cool')
# ещё не докрутил