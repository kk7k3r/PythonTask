class DoubleElement:
    def __init__(self, *lst):
        self.list = list()
        prev_elem = None
        counter = 0
        for i_index, i_elem in enumerate(lst):
            if (i_index % 2 == 1):
                self.list.append((prev_elem, i_elem))
            prev_elem = i_elem
            counter += 1
            if (counter == len(lst) and counter % 2 == 1):
                self.list.append((prev_elem, None))

    def __next__(self):
        pass
        raise StopIteration
            
    def __iter__(self):
        return iter(self.list)        
            

dL = DoubleElement(1)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1,2,3)
for pair in dL:
    print(pair)    

