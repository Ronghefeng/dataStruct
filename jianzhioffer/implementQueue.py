
class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:

        if len(self.stack2) == 0:

            if len(self.stack1) == 0:
                return -1

            for i in range(len(self.stack1))[::-1]:
                self.stack2.append(self.stack1.pop(-1))

        return self.stack2.pop()


if __name__ == '__main__':
    # Your CQueue object will be instantiated and called as such:
    obj = CQueue()
    obj.appendTail(5)
    obj.appendTail(2)
    print(obj.deleteHead())
    print(obj.deleteHead())