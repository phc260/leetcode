class TwoSum:
    
    # initialize your data structure here
    def __init__(self):
        self.hashmap = {}

    # @return nothing
    def add(self, number):
        if number not in self.hashmap:
            self.hashmap[number] = 0
        self.hashmap[number] += 1
    # @param value, an integer
    # @return a Boolean
    def find(self, value):
        for i in self.hashmap:
            if (value-i) in self.hashmap:
                if self.hashmap[i]>1 or value!=2*i:
                    return True
        return False