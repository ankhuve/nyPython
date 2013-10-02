class BodyMassIndex(object): #Inheriting from object in 2.x ensures a new-style class.
  count = 0
  def __init__(self, name, weight, height):
    self.name = name
    self.weight = 14 * weight
    self.height = 12 * height
    self.notes = None
    self.bmitotal = 0
    BodyMassIndex.count += 1

  def display_count(self):
    print ("Total number of objects is %d" % BodyMassIndex.count)

  def calculate_bmi(self):
    return ( self.weight * 703 ) / ( self.height ** 2 )

test = BodyMassIndex("bob", 10, 10)
test.notes = "some notes"
print(BodyMassIndex, test.notes)
