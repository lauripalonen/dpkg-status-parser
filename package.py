import re

class Package:

  id = None
  name = None
  description = None

  def __init__(self):
    self.depencies_with_alternatives = []
    self.depencies = []
    self.dependants = []
    self.depencies_by_id = []
    pass

  def set_name(self, name):
    self.name = name
  
  def get_name(self):
    return self.name

  def set_description(self, descript):
    self.description = descript

  def get_description(self):
    return self.description

  def set_depencies(self, depencies):
    depency_array = self.parse_depencies(depencies)
    self.depencies = depency_array

  def get_depencies(self):
    return self.depencies

  def set_id(self, id):
    self.id = id

  def get_id(self):
    return self.id

  def get_alternative_depencies(self):
    return self.depencies_with_alternatives

  def parse_depencies(self, depencies):
    depency_array = []

    #Separate depencies
    separated_depencies = re.split("\,\s", depencies)
    trimmed_depencies = []

    #Trim depencies - remove version information
    for dep in separated_depencies:
      if not re.search("\|", dep):
        trimmed_depencies.append(re.split("\s", dep)[0])
      else:
        self.handle_alternate_depencies(dep)

    for depency in trimmed_depencies:
      depency_array.append(depency)

    return depency_array

  def handle_alternate_depencies(self, alternates):
    separated_alts = re.split("\s\|\s", alternates)
    trimmed_alts = []
    for dep in separated_alts:
      trimmed_alts.append(re.split('\s', dep)[0])
    self.depencies_with_alternatives = trimmed_alts


  def set_reference_list(self, name_index_list):
    self.refefence_list = name_index_list

  def add_dependant(self, dependant):
    self.dependants.append(dependant)

  def add_depency_by_id(self, depency):
    self.depencies_by_id.append(depency)

  def get_depency_id_list(self):
    return self.depencies_by_id

  def get_dependant_id_list(self):
    return self.dependants

  def print_all(self):
    print("{}: {}".format(self.id, self.name))
    print("Description: {}".format(self.description))
    print("Depencies: {}".format(self.depencies_by_id))
    print("Dependants: {}".format(self.dependants))

  def package_as_json(self):
    return '{{"id":{},"name":"{}","description":"{}","depencies":{},"dependants":{}}}'.format(self.id, self.name, self.description, self.depencies_by_id, self.dependants)