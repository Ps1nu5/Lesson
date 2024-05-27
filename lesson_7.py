characteristic = {'hp': 100, 'money': 50, }
l = ['да', 'нет', 'отпор']
a = input('хотите ли вы купить золотой меч ценой в 10 монет?')
if a == 'да':
    characteristic['money'] -= 10
    print('вы купили меч')
    print(f'ваш баланс {characteristic["money"]} монет.')
else:
    print('вы отказались')

print('вы идете по тропинке...')
b = input('вы нашли кошелек, хотите подобрати?')
if b == 'да':
    characteristic['money'] += 30
    print(f'вы подобрали кошелек, ваш баланс {characteristic["money"]} монет. ')
else:
    print('вы не стали подбирать кошелек.')

print('вы идете по тропинке...')

if b != 'да':
    print('по пути вы встретили богатого человека, он дал вам 100 монет.')
    characteristic['money'] += 100
    print(f'ваш баланс {characteristic["money"]} монет.')

if b == 'да':
    print('по пути вы встретили грабителя, он потребовал у вас монеты')
    c = input('отдать ему монеты?: да, дать отпор: отпор, не довать монет: нет')

if c == 'да':
    characteristic['money'] -= 40
    print(f'вы отдали монеты грабителю, ваш баланс {characteristic["money"]} монет. ')
if (a == 'да' and c == 'отпор'):
    characteristic['money'] += 40
    print(f'вы победили грабителя, забрав его монеты себе, ваш баланс {characteristic["money"]} монет. ')
if a != 'да':
    print(f'у вас нет меча')
    characteristic['money'] -= 40
    print(f'вы отдали монеты грабителю, ваш баланс {characteristic["money"]} монет. ')
if c == 'нет':
    characteristic['money'] -= 40
    characteristic['hp'] -= 75
    print(f'вы отдали монеты грабителю, ваш баланс {characteristic["money"]} монет, {characteristic["hp"]} ')