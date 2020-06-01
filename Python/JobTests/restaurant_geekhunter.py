import math;
class RestaurantItem:
  def __init__(self, itemName, val):
    self.itemName = itemName
    self.val = val
  def setitemName(self, itemName):
    self.itemName = itemName
  def setval(self, val):
    self.val = int(val)
  def getitemName(self):
    return self.itemName
  def getval(self):
    return int(self.val)

def processInput():
    c = int(input())
    n = int(input())
    sum_total = 0
    sum_no_consider = 0
    i = 0
    items_arr = []
    while(i < int(n)):
      itemName, val = input().split();
      item = RestaurantItem(itemName, val)
      sum_total += item.getval()
      i += 1
      items_arr.append(item)
    no_consider = input().split()
    for nc in no_consider:
      for item in items_arr:
        # Para uma lista grande, um for-dentro-de-for (complexidade n^2)
        # não é recomendado; este código é apenas um exemplo.
        if(item.getitemName() == nc):
          sum_no_consider += item.getval()
    print(sum_total)
    print(math.floor((sum_total-sum_no_consider)/c))
    print(sum_no_consider)
    return input

processInput();
