import threading
from threading import Condition


# 条件变量
class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name='小爱')
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}：在".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}：好呀".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}：疑是地上霜!".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}：低头思故乡!".format(self.name))
            self.cond.notify()


class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name='天猫精灵')
        self.cond = cond

    def run(self):
        with self.cond:
            print('{}:小爱同学'.format(self.name))
            self.cond.notify()
            self.cond.wait()

            print('{}:我们来对古诗吧!'.format(self.name))
            self.cond.notify()
            self.cond.wait()

            print('{}:床前明月光!'.format(self.name))
            self.cond.notify()
            self.cond.wait()

            print('{}:举头望明月!'.format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == '__main__':
    cond = Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    xiaoai.start()
    tianmao.start()
