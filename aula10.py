n1 = float(input('digit a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2) / 2
print('a sua media foi {:.1f}'.format(m))
if m >= 6.0:
    print('parabens voce consegui a media nessesaria')
else:
    print('voce fracassou, estude mais')
