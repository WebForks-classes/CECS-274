#https://www.chegg.com/homework-help/questions-and-answers/2-design-implement-random-queue-implementation-queue-interface-remove-operation-removes-el-q45403618

import random

class RandomQueue:
    def __init__(self):
        self.list=[]
        self.count=0

    def add(self, item):
        self.list.append(item)
        self.count+=1

    def remove(self):
        if self.count==0:
            return None
        radnomnumber=random.randint(0,self.count-1)
        element=self.list[radnomnumber]
        self.list[radnomnumber]
        self.list[-1]=self.list[-1]
        self.list[radnomnumber]
        self.list.pop()
        self.count-=1
        return element

    def isEmpty(self):
        return self.count==0


q=RandomQueue()
for i in range(1,11):
    q.add(i)

while not q.isEmpty():
    print(q.remove())