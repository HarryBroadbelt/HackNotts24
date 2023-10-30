from nltk import word_tokenize

class PeekableStream:
  def __init__(self, iterator):
    self.iterator = iter(iterator)
    self._fill()
  def _fill(self):
    try:
      self.next = next(self.iterator)
    except StopIteration:
      self.next = None
  def move_next(self):
    ret = self.next
    self._fill()
    return ret

tokens = []
file = open('test.txt')
charstream = str(file.readlines())

tokens = word_tokenize(charstream)

for word in tokens:
    