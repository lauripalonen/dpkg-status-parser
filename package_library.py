class Package_library:

  packages_by_name = {}
  packages_by_id = {}

  def __init__(self):
    pass

  def add_package(self, package):
    self.packages_by_name[package.get_name()] = package.get_id()
    self.packages_by_id[package.get_id()] = package

  def get_packages_by_id(self):
    return self.packages_by_id

  def get_packages_by_name(self):
    return self.packages_by_name

  def arrange_depencies(self):
    for pkg_id in self.packages_by_id:
      if self.packages_by_id.get(pkg_id):
        package = self.packages_by_id.get(pkg_id)
        depencies = package.get_depencies()
        alt_depencies = package.get_alternative_depencies()

        for dep_name in depencies:
          if self.packages_by_name.get(dep_name):
            depency_id = self.packages_by_name.get(dep_name)
            depency_as_package = self.packages_by_id.get(depency_id)

            package.add_depency_by_id(depency_id)
            depency_as_package.add_dependant(pkg_id)

        for alt_dep_name in alt_depencies:
          if self.packages_by_name.get(alt_dep_name):

            depency_id = self.packages_by_name.get(alt_dep_name)
            depency_as_package = self.packages_by_id.get(depency_id)

            package.add_depency_by_id(depency_id)
            depency_as_package.add_dependant(pkg_id)
            break