# from text_copy import func as t
# from second_module import func  as s
# print(s('Fluent Python'))
# print(t('Luciano Ramalo'))
# print(sentence)

# from collections import defaultdict
# def func(items):
#     d=defaultdict(list)
#     for key,value in items:
#         d[key].append(value)
#
#     c=d.copy()
#     print('copy valie:',c)
#     x={'elephant':7,'tiger':12}
#     t=c.setdefault('cat',5)
#     print("VALUE",c,t)
#
# hardware=(('keyboard',2),('cpu',4),('monitor',3),('mouse',3))
#
# test = func(hardware)

# from collections import namedtuple
# chocolate=namedtuple('chocolate','variety number name')
# dark_chocolate=chocolate(variety='home made',number=5,name='Caudbaury')
# milk_chocolate=chocolate(variety='company product',number=8,name='Milky bar')
# print(milk_chocolate.name,milk_chocolate.number,milk_chocolate.variety,dark_chocolate.name)

# from collections import Counter
#
# b = 'asaddddssd'
# c = Counter(b)
# print(dict(c))
# x =sorted(c.elements())
# print(x)
#
# sentence = 'You cannot belive in god Until you belive in yourself'
# C= Counter(sentence.split())
# v=C.most_common()[0]
# t =C.items()
# d = list(t)

from collections import OrderedDict,defaultdict
books=['Python_book','C_book','C_book','java','Python_book']
dt = defaultdict(int)
for key in books:
    dt[key]+=1
print("D:",dt)
o = OrderedDict(dt)
print(dt)
