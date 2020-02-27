import re

class Data_parser:

  def __init__(self):
    pass

  def parse_depencies(self, depencies):
    depency_list = re.split("\,\s", depencies)

    parsed_depencies = []

    for dep in depency_list:
      if self.group_of_alternatives(dep):
        parsed_group = self.parse_group_of_alternatives(dep)
        for dep in parsed_group:
          parsed_depencies.append(dep.strip())
      else:
        try:
          (dep, version) = dep.split(maxsplit=1)
        except ValueError:
          pass
        parsed_depencies.append(dep.strip())
      
    return parsed_depencies
   
  def parse_group_of_alternatives(self, depency_group):
    depency_list = re.split("\s\|\s", depency_group)
    parsed_group =[]

    for dep in depency_list:
      try:
        (dep, version) = dep.split(maxsplit=1)
      except ValueError:
        pass
      parsed_group.append(dep)

    return parsed_group

  def group_of_alternatives(self, depency):
    if re.search("\|", depency):
      return True
    return False