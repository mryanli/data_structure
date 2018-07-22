# 链表,按照 结构 可以分为
#   线性链表，
#   圆形链表，

# 按照方向，链表可以分为
#   单向链表
#   双向链表

#不管是哪种链表，链表 的数据单元 都有 以下 信息
#   数据
#   指向下一个或上一个数据单元的链接

#单项线性列表的python 实现
#须实现以下功能
# is_empty() :判断是否为空
# length():返回长度
# travel():遍历打印
#
# add(data)：在头部添加数据
# append(data):在尾部添加数据
# insert(pos,data):在链表中pos位置增加数据
#
# remove(data):删除数据
# search(data):查找数据

#单个数据单元
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

#数据单元的链表
class Linked_list():
    def __init__(self): #初始化头节点为空
        self._head = None

    def is_empty(self): #是否为空
        return self._head

    def length(self): #返回长度
        cur = self._head
        count = 0
        while cur != None:
            cur = cur.next
            count += 1
        return count

    def travel(self): #遍历打印
        cur = self._head
        while cur != None:
            print(cur.data,end = ',')
            cur = cur.next
        print()

    def add(self,data): #在头部添加数据
        node = Node(data)
        node.next = self._head
        self._head = node


    def append(self,data):#在尾部添加数据
        tail = self._head
        node = Node(data)
        while tail.next != None:
            tail = tail.next
        tail.next = node



    def insert(self,pos,data):#在链表中pos位置增加数据
        curpos = 0
        cur = self._head
        node = Node(data)
        if pos >= self.length():
            return self.append(node)
        else:
            while curpos <= pos:
                cur = cur.next
                curpos +=1
            node.next = cur.next
            cur.next = node



    def remove(self,data): #删除数据
        cur = self._head
        while cur != None:
            if cur.next and cur.next.data == data:
                cur.next = cur.next.next
            cur = cur.next


    def search(self,data):#查找数据
        if self._head ==  None:
            return False
        cur = self._head
        while cur !=  None:
            if cur.data == data:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    link = Linked_list()
    link.add(1)
    link.add(2)
    link.append(3)
    link.append(8)

    link.insert(1,5)
    link.insert(1,5)
    link.insert(1,5)
    print(link.is_empty())
    print(link.length())
    link.travel()
