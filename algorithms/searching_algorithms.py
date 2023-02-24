class SearchingAlgorithms:

    def BinarySearch(self, seq, element):
        # seq should be sorted
        if len(seq) > 1:
            #  if len(seq) is even
            if len(seq) % 2 == 0:
                midpoint = int(len(seq) / 2)
            else:
                #  if len(seq) is odd
                midpoint = int(len(seq) / 2) + 1

            #  if seq[midpoint] is the element
            if seq[midpoint] == element:
                return True

            # if seq[midpoint] > element lookup in left
            elif seq[midpoint] > element:
                return self.BinarySearch(seq=seq[0:midpoint], element=element)

            # if seq[midpoint] < element lookup in right
            elif seq[midpoint] < element:
                return self.BinarySearch(seq=seq[midpoint:len(seq) + 1],
                                         element=element)
            # if nothing works
            else:
                return False
        else:
            if seq[0] == element:
                return True
            else:
                return False
