s = input()
s2 = ['_' for i in range(len(s))]
print('Welcome to Hangman!')
done = 0
while not done:
    ch = input('Guess your letter: ')
    for i in range(len(s)):
        if ch == s[i]:
            s2[i] = ch
        elif ch not in s:
            print('Incorrect!')
            break
    if '_' not in s2:
        done = 1
        print('WIN!')
    else:
        done = 0
    print(''.join(s2))