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
            if not self.picking:
                pass
            else:
                if self.line != []:
                    self.line[0]['function'](self.line[0]['arguments'])
                    self.line.remove(self.line[0])
                else:
                    pass
            sleep(self.time)

    def add(self, id, reference, args):
        queue.line.append({'id' : id, 'function' : reference, 'arguments' : args})

    def remove(self, id):
        for i in queue.line:
            if i['id'] == id:
                self.line.remove(i)
    
    def start(self):
        queue.picking = True

    def stop(self):
        queue.picking = False

    def position(self, id):
        for i in queue.line:
            if i['id'] == id:
                return queue.line.index(i) + 1
        return None

queue = queue(1) # set the arg to the amount of you time you between each function execution
Thread(target=queue.main).start() # tbh couldnt put this into class but make sure this is here

queue.add('123', test, 'hello!') # first arg is like a identifier, second arg is the function reference, third arg is the args for that function
queue.start() # starts queue
print(queue.position('123')) # prints out the index of the identifier in queue, more helpful for the user not server btw
