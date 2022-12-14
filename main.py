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
                self.line.remove(i)
    
    def start(self):
        queue.picking = True

    def stop(self):
        queue.picking = False

queue = queue(1) # set the arg to the amount of you time you between each function execution
Thread(target=queue.main).start() # tbh couldnt put this into class but make sure this is here

queue.add('123', test, 'hello!') # first arg is like a identifier, second arg is the function reference, third arg is the args for that function
# queue.remove('123') # place identifier into arg to remove a certain queued request, tbh I havent tested out this function yet lol
queue.start() # starts queue
# queue.stop() # stops queue
