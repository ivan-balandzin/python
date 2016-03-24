import collections
with open('access.log','r') as f:
          iplist = [r.split()[0] for r in f]
#Находит в iplist-е 10 самых частовстречающихся элементов, выводит в виде IP, количество повторений
print(collections.Counter(iplist).most_common(10))

