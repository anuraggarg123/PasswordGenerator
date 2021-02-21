import random
import string as s
def func(length):
    fullElements = s.ascii_letters + s.digits + s.punctuation
    passwd = random.choice(s.ascii_lowercase)
    passwd = passwd + random.choice(s.ascii_uppercase)
    passwd = passwd + random.choice(s.digits)
    passwd = passwd + random.choice(s.punctuation)
    list1 = list(passwd)
    random.shuffle(list1)
    for i in range(length - 4):
        list1.extend(random.choice(fullElements))
    new = ''.join(list1)
    return new

length = int(input('Enter the length of password you want = '))
print('your password is : ')
print(func(length))