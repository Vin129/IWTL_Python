class Coach:
    CoachName = "教练" #公共变量
    __weight = 100 #开头两个下滑线代表私有 变量与方法都可以加两个下滑线来表示私有
    def __init__(self,name:str): #构造函数，self不是关键字，可以是其他任何命名
        self.CoachName = name # 赋值操作，操作的都是实例而不是类，所以要用self.
    def speak(self): # def 是声明函数的关键字
        print("%s:小伙子，你有对象吗？"%self.__class__.CoachName)
    def agree(self):
        print("%s:行吧行吧，找不到对象至少你能创建一个了吧"%self.CoachName)

class LiuChuanFeng(Coach): # 继承
    Name = "流川枫"
    def __init__(self): #继承后构造函数中需要对父级进行初始化（如果父级有需要的情况）
        Coach.__init__(self,"教练")
        print(self.Name)

    def speak(self): #父级方法的重写
        print("%s:八嘎"%self.Name)
    def agree(self):
        print("%s:Zzz...."%self.Name)
    def coachAgree(self):
        super(LiuChuanFeng, self).agree() #子类调用父级被重写的方法

class Adream:
    state = "这是一个梦"

class YingMuHuaDao(Coach,Adream): #多重继承
    def __init__(self):
        Coach.__init__(self,"教练")
    def dreaming(self):
        print("%s(%s):哈哈哈，你俩都被我继承了！"%(Name,Adream.state))

coach = Coach("胖子")  #创建对象实例
liuChuanFeng = LiuChuanFeng()
Name = "樱木花道"

print("%s:%s你是哪个？"%(Name,coach.CoachName))
coach.speak()
print("%s:你为啥这么高级的speak,我就会Print"%Name)
liuChuanFeng.speak()
print("%s:教练，我想学Python！"%Name)
liuChuanFeng.agree()
liuChuanFeng.coachAgree()
me = YingMuHuaDao()
me.dreaming()
