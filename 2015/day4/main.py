from hashlib import md5
secret = 'ckczppom'

i = 0
while 1:
  h = md5((secret + str(i)).encode()).hexdigest()
  if h[:5] == '00000':
    print(h)
    print(i)
    break
  i += 1

# Part Two
i = 0
while 1:
  h = md5((secret + str(i)).encode()).hexdigest()
  if h[:6] == '000000':
    print(h)
    print(i)
    break
  i += 1
