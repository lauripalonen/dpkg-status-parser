from package import Package
from package_library import Package_library

package_library = Package_library()
status_data = open("sample_status.real")

def setup_package_library(status_data):
  index = 0

  package = Package()

  for line in status_data:
    if line.startswith('Package: '):
      pkg_name = parse_line('Package: ', line)
      package.set_name(pkg_name)
      package.set_id(index)

    if line.startswith('Description: '):
      pkg_description = parse_line('Description: ', line)
      package.set_description(pkg_description)

    if line.startswith('Depends: '):
      pkg_depencies = parse_line('Depends: ', line)
      package.set_depencies(pkg_depencies)

    if not line.strip():
      package_library.add_package(package)
      package = Package()
      index += 1

def parse_line(argument, line):
  title_and_content = line.split(argument)
  content = (title_and_content[1].strip()).replace("\"", "'")
  return content

setup_package_library(status_data)
pkg_by_id = package_library.get_packages_by_id()
pkg_by_name = package_library.get_packages_by_name()

package_library.arrange_depencies()

def create_json_data():
  json_data = pkg_by_id.get(0).package_as_json()

  for i in range (1, len(pkg_by_id)):
    pkg = pkg_by_id.get(i)
    json_data += ", {}".format(pkg.package_as_json())

  outputfile = "[{}]".format(json_data)
  return outputfile
  

output = open("db.json", "x")
output.write(create_json_data())
output.close()