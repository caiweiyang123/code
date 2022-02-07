from threading import Thread
import time


def task(name):
    print("%s is running.." % name)
    time.sleep(2)
    print("%s is end" % name)


if __name__ == '__main__':
    t = Thread(target=task, args=("xiaowang",))
    t.start()
    t.join()  # 主线程等到子线程结束后，才执行主线程
    print("主")
