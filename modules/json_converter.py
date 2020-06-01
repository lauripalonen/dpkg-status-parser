from modules.package import Package
from modules.package_library import Package_library
from modules.data_parser import Data_parser

class Json_converter:

  def __init__(self, input_name, output_name):
    self.input_name = input_name
    self.output_name = output_name
    self.library = Package_library()
    self.parser = Data_parser()

  def initiate_packages(self):
    package = Package()
    input_file = open(self.input_name)

    for line in input_file:
      if line.startswith('Package: '):
        (title, name) = line.split(maxsplit=1)
        package.set_name(name.strip())
        self.library.add_package(package)
  
      if not line.strip():
        package = Package()

    input_file.close()

  def set_package_data(self):
    package = Package()
    input_file = open(self.input_name)

    for line in input_file:
      if line.startswith('Package: '):
        (title, name) = line.split(maxsplit=1)
        package = self.library.get_package(name.strip())

      if line.startswith('Description: '):
        (title, description) = line.split(maxsplit=1)
        description = description.replace("\"", "'")
        package.set_description(description.strip())

      if line.startswith('Depends: '):
        (title, dependencies) = line.split(maxsplit=1)
        parsed_dependencies = self.parser.parse_dependencies(dependencies)

        for dep in parsed_dependencies:
          if self.library.find_id(dep):
            dep_id = self.library.find_id(dep)
            package.add_dependency(dep_id)

            dep_pkg = self.library.get_package(dep)
            dep_pkg.add_dependant(package.get_id())

          else:
           package.add_alternative_dependency(dep)

    input_file.close()

  def create_json_data(self, packages):
    json_data = packages[0].package_as_json()

    for i in range (1, len(packages)):
      pkg = packages[i]
      json_data += ",{}".format(pkg.package_as_json())

    output_file = "[{}]".format(json_data)
    return output_file

  def run(self):
    self.initiate_packages()
    self.set_package_data()

    packages = self.library.get_packages()
    packages.sort(key=lambda pkg: pkg.name)
 
    json_packages = self.create_json_data(packages)

    output = open(self.output_name, "x")
    output.write(json_packages)
    output.close()





