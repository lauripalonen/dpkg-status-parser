class Package_library:

  def __init__(self):
    self.package_catalog = {}
    self.packages = []
    pass

  def add_package(self, pkg):
    index = len(self.package_catalog)
    pkg.set_id(index)
    pkg_name = pkg.get_name()

    self.package_catalog[pkg_name] = index
    self.packages.append(pkg)

  def find_id(self, pkg_name):
    return self.package_catalog.get(pkg_name)

  def get_package(self, pkg_name):
    for pkg in self.packages:
      if pkg.get_name() == pkg_name:
        return pkg
    return None

  def get_packages(self):
    return self.packages