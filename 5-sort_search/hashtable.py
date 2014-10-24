class HashTable():
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
            print 'searching for nextslot'
            nextslot = self.rehash(hashvalue,len(self.slots))
            print 'nextslot: %s' % nextslot
            while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
                print 'nextslot != None and != key'
                nextslot = self.rehash(nextslot,len(self.slots))
                print 'nextslot from while loop: %s' % nextslot

            if self.slots[nextslot] == None:
                self.slots[nextslot]=key
                self.data[nextslot]=data
            else:
                self.data[nextslot] = data #replace

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        pos = startslot

        while self.slots[pos] != None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]
            else:
                pos = self.rehash(pos, len(self.slots))
                if pos == startslot:
                    # Searched whole table; not found.
                    stop = True

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size
