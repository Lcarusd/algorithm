# coding:utf-8

# class Entity:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __call__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# if __name__ == '__main__':
#     someone = Entity(1, 2)
#     # 相当于调用someone.__call__(3, 4)
#     someone(3, 4)
#     print(someone.x)
#     print(someone.y)






import numpy as np

class My_Container():
    def __init__(self):
        self.data = np.random.randn(3, 2)

    def __len__(self):
        return self.data.shape[0]

    def __getitem__(self, item):
        sample = self.data[item, :]
        return sample


if __name__ == '__main__':
    contain = My_Container()
    print(contain[0])


