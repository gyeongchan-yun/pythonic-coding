#!/usr/bin/python3

import os
import multiprocessing


class Worker(multiprocessing.Process):

    def __init__(self, args, name=""):
        super().__init__()
        self.name = name
        self.args = args

    def run(self):
        print("name: %s, argument: %s" % (self.name, self.args[0]))
        print("parent pid: %s, pid: %s" % (os.getppid(), os.getpid()))


def main():
    for i in range(5):
        p = Worker(name="process %i" % i, args=(i,))
        p.start()


if __name__ == "__main__":
    main()
