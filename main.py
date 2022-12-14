# { 'USER_ID': int, 'FUNCTION': reference, 'ARGS': [ARGS] }
from time import sleep
from threading import Thread
def test(args):
    print(args)

class queue():
    def __init__(self, time):
        self.line = []
        self.time = time
        self.picking = False

    def main(self):
        while True:
            if self.picking == False:
                pass
            else:
                if self.line != []:
                    self.line[0]['function'](self.line[0]['arguments'])
                    self.line.remove(self.line[0])
                else:
                    pass
            sleep(self.time)

    def add(self, user, reference, args):
        queue.line.append({'id':user, 'function':reference, 'arguments':args})

    def remove(self, user):
        for i in queue.line:
            if i['id'] == user:
                del i
    
    def start(self):
        queue.picking = True

    def stop(self):
        queue.picking = False

queue = queue(1)
Thread(target=queue.main).start()

queue.add('123', test, 'hello!')
queue.start()
