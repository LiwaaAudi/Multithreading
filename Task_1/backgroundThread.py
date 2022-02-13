from threading import Thread
import time


class AsyncWriteFile(Thread):
    def __init__(self, text, out):
        Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, 'a')
        f.write(self.text + '\n')
        f.close()
        time.sleep(3)
        print("Finished Background file write to " + self.out)


message = input('Enter a Message to add to a file: ')
background = AsyncWriteFile(message, input('Enter file Name: '))
background.start()
num = int(input('Enter Some Number: '))
if num % 2 == 0:
    print("Entered number is Even")
else:
    print("Entered number is ODD")
background.join()
print("Waited until thread was complete")
