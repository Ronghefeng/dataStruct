import time


def consumer():
    r = ""
    while True:
        print("start ....")
        n = yield r
        print("n = %s" % n)
        if not n:
            return
        print("[CONSUMER] Consuming %s..." % n)
        time.sleep(1)
        r = "200 OK"


def produce(c):
    r = c.__next__()
    print("r = %s" % r)
    n = 0
    while n < 3:
        n = n + 1
        print("[PRODUCER] Producing %s..." % n)
        r = c.send(n)
        print("[PRODUCER] Consumer return: %s" % r)
    c.close()


if __name__ == "__main__":

    c = consumer()
    produce(c)
