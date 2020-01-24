#coding:utf8
import Queue
class Player():
    def __init__(self):
        self.msg_q = Queue.Queue()

    # 获取用户队列里的所有消息
    def getMsg(self):
        msgs = [] # 获取这个对象的所有消息并添加到列表中
        for msg in range(self.msg_q.qsize()):  # 循环消息列表
            msg = self.msg_q.get()  # 获取消息
            msgs.append(msg) # 加到列表中
        return msgs  # 返回消息列表
