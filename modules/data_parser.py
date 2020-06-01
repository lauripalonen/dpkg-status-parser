import re

class Data_parser:

  def __init__(self):
    pass

  def parse_dependencies(self, dependencies):
    dependency_list = re.split("\,\s", dependencies)

    parsed_dependencies = []

    for dep in dependency_list:
      if self.group_of_alternatives(dep):
        parsed_group = self.parse_group_of_alternatives(dep)
        for dep in parsed_group:
          parsed_dependencies.append(dep.strip())
      else:
        try:
          (dep, version) = dep.split(maxsplit=1)
        except ValueError:
          pass
        parsed_dependencies.append(dep.strip())
      
    return parsed_dependencies
   
  def parse_group_of_alternatives(self, dependency_group):
    dependency_list = re.split("\s\|\s", dependency_group)
    parsed_group =[]

    for dep in dependency_list:
      try:
        (dep, version) = dep.split(maxsplit=1)
      except ValueError:
        pass
      parsed_group.append(dep)

    return parsed_group

  def group_of_alternatives(self, dependency):
    if re.search("\|", dependency):
      return True
    return False