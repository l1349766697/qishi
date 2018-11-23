
# 分页工作，跳转页码题

class Page:
    def __init__(self, lst, pageSize):
        self.lst = lst
        self.pageSize = pageSize

    def start(self):
        return self.lst[: self.pageSize]  # 直接切片出第一页

    def end(self):
        return self.lst[(self.total_page - 1)* self.pageSize: self.total_page* self.pageSize]  # 调用总页数来计算最后一页

    @property       # 将一个方法变成属性，方便调用
    def total_page(self):
        if len(self.lst) % self.pageSize == 0:
            return len(self.lst) // self.pageSize  # 总数据长度整除每页数据量，整除没有余数则，除数就是总页数
        else:
            return len(self.lst) // self.pageSize + 1  # 整除有余数，则（除数 + 1) 就是总页数


    def index(self):
        ye = int(input("请输入要查询的页数："))
        return self.lst[(ye - 1)* self.pageSize : ye * self.pageSize]  # 找出页数和每页数据的规律，写出切片方法





lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 每页3条数据，
#     [(ye - 1)* pageSize: ye * pageSize]

# 每页4条数据

obj = Page(lst, 3)

print(obj.index())
print(obj.end())