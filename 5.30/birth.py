birth = input('birthday? :')
birth = int(birth)

if birth > 2000:
    print('00后')
elif birth > 1900:
    print('90后')
else:
    print('old')
