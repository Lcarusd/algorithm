# coding:utf-8
# Python语法相关面试题


class Parent(object):
    x = 1
class Child1(Parent):
    pass
class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x)

Child1.x = 2
print(Parent.x, Child1.x, Child2.x)

Parent.x = 3
print(Parent.x, Child1.x, Child2.x)




def div1(x, y):
    print("%s/%s = %s" %(x, y, x/y))
def div2(x, y):
    print("%s//%s = %s" %(x, y, x//y))
div1(5, 2)
div1(5., 2)          #
div2(5, 2)           #
div2(5., 2.)





list = ['a', 'b', 'c', 'd', 'e']
print(list[10:])





def multiprocess():
	return [lambda x:x * i for i in range(4)]
print([m(2) for m in multiprocess()])






def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print("list1 = %s" %(list1))
print("list2 = %s" %(list2))
print("list3 = %s" %(list3))
