#!/usr/bin/python3
class MyInt(int):
    def __eq__(self, num):
        if (self.real == num):
            return False
        return True

    def __ne__(self, num):
        if(self.real != num):
            return False
        return True
