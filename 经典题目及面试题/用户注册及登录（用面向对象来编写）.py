# 1、补充代码完成用户注册和登录

# class user:
#     def __init__(self, name, pwd):
#         self.name = name
#         self.pwd = pwd
#
#
# class Account:
#     def __init__(self):
#         self.user_list = []  # 用户列表,数据格式:[User对象,User对象,User对象]
#
#     def login(self):
#          ###用户登录,用户输入用户名和密码并去self,user1ist中检查用户是否合法
#           # return##
#         pass
#
#     def register(self):
#     ### 用户注册,动态创建User对象,并添加到self, user list中
#     # return###
#         pass
#
#     def run(self):
#     ### Q主程序,先进行2次用户注册,再进行用户登录(3次重试机
#     # return:####
#         pass

#
# if __name__ == "__main__":
#     obj = Account()
#     obj.run()

# 16.补充上述代码：实现用户注册和登录(升级题)

# 解题一、

class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        self.user_list = []  # 用户列表,数据格式:[User对象,User对象,User对象],相当于将User函数的每一个对象作为一个变量


    def login(self):
         ###用户登录,用户输入用户名和密码并去self,user1ist中检查用户是否合法
          # return##
        print("用户登录")
        name2 = input("请输入登录名：")
        pwd2 = input("请输入登录密码：")
        for i in self.user_list:    # 这里循环拿到列表中的每一个元素，是User中的每一个对象，
            if name2 == i.name and pwd2 == i.pwd:  # 所以i.name等于注册时的用户名，i.pwd等于用户的注册时的密码
                return True  # 返回给三次登录的主程序，是否登录成功
        else:
            return False

    def register(self):
        print("用户注册")
    ### 用户注册,动态创建User对象,并添加到self, user list中
        name1 = input("请输入用户名：")
        pwd1 = input("请输入密码")
        u = User(name1, pwd1)
        self.user_list.append(u) # 这里关键是要理解到，是将每个User的对象添加到了self.user_list中

    # return###


    def run(self):
    ### Q主程序,先进行2次用户注册,再进行用户登录(3次重试机会
        self.register()  # 2次注册
        self.register()

        for i in range(3):  # 3次登录

            ret = self.login()  # 执行登录的函数，ret接收返回值

            if ret == True:  # 如果接收到返回True,则登录成功,跳出循环，否则继续下一次登录，超过3次后，执行登录失败
                print("登录成功")
                break
        else:
            print("登录失败") # 循环三次失败后，才到失败




    # return:####
        pass


if __name__ == "__main__":
    obj = Account()
    obj.run()

































