
class Stats:

  def __init__(self, data):
    self.stats = dict()
    self.build_stats(data)

  def build_stats(self, data):
    self.stats = dict()
    data.sort()
    total = len(data)
    for index in range(total):
      item = data[index]
      if item not in self.stats:
        self.stats[item] = {
          'less': index,
          'greater': total - 1 - index
        }

  def less(self, n):
    return self.stats[n]['less']

  def between(self, a, b):
    return self.stats[b]['less'] - self.stats[a]['less'] + 1

  def greater(self, n):
    return self.stats[n]['greater']


class DataCapture:

  def __init__(self):
    self.data = list()

  def add(self, n):
    self.data.append(n)

  def build_stats(self):
    stats = Stats(self.data)
    return stats
   

capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
print(stats.less(4)) # should return 2 - only two values 3, 3 are less than 4
print(stats.between(3, 6)) # should return 4 (3, 3, 4 and 6 are between 3 and 6)
print(stats.greater(4)) # should return 2 (6 and 9 are the only two values greater than 4)
