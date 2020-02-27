class Package:

  def __init__(self):
    self.id = None
    self.name = None
    self.description = None

    self.main_depencies = []
    self.alternative_depencies = []
    self.dependants = []
    pass

  def set_name(self, name):
    self.name = name
  
  def get_name(self):
    return self.name

  def set_description(self, descript):
    self.description = descript

  def set_id(self, id):
    self.id = id

  def get_id(self):
    return self.id

  def add_depency(self, depency):
    if not depency in self.main_depencies:
      self.main_depencies.append(depency)
  
  def add_alternative_depency(self, depency):
    if not depency in self.alternative_depencies:
      self.alternative_depencies.append(depency)

  def add_dependant(self, dependant):
    if not dependant in self.dependants:
      self.dependants.append(dependant)

  def alternatives_as_string(self):
    if len(self.alternative_depencies) > 0:
      alternatives = '\"{}'.format(self.alternative_depencies[0])

      for i in range (1, len(self.alternative_depencies)):
        alternatives += '\", \"{}'.format(self.alternative_depencies)

      return '[{}\"]'.format(alternatives)
    return '[]'



  def print_all(self):
    print("{}: {}".format(self.id, self.name))
    print("Description: {}".format(self.description))
    print("Depencies: {}".format(self.main_depencies))
    print("Dependants: {}".format(self.dependants))

  def package_as_json(self):
    alternatives = self.alternatives_as_string()
    return '{{"id":{},"name":"{}","description":"{}","depencies":{}, "alternatives":{},"dependants":{}}}'.format(self.id, self.name, self.description, self.main_depencies, alternatives, self.dependants)