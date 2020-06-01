class Package:

  def __init__(self):
    self.id = None
    self.name = None
    self.description = None

    self.main_dependencies = []
    self.alternative_dependencies = []
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

  def add_dependency(self, dependency):
    if not dependency in self.main_dependencies:
      self.main_dependencies.append(dependency)
  
  def add_alternative_dependency(self, dependency):
    if not dependency in self.alternative_dependencies:
      self.alternative_dependencies.append(dependency)

  def add_dependant(self, dependant):
    if not dependant in self.dependants:
      self.dependants.append(dependant)

  def alternatives_as_string(self):
    if len(self.alternative_dependencies) > 0:
      alternatives = '\"{}'.format(self.alternative_dependencies[0])

      for i in range (1, len(self.alternative_dependencies)):
        alternatives += '\", \"{}'.format(self.alternative_dependencies[i])

      return '[{}\"]'.format(alternatives)
    return '[]'



  def print_all(self):
    print("{}: {}".format(self.id, self.name))
    print("Description: {}".format(self.description))
    print("Dependencies: {}".format(self.main_dependencies))
    print("Dependants: {}".format(self.dependants))

  def package_as_json(self):
    alternatives = self.alternatives_as_string()
    return '{{"id":{},"name":"{}","description":"{}","dependencies":{}, "alternatives":{},"dependants":{}}}'.format(self.id, self.name, self.description, self.main_dependencies, alternatives, self.dependants)