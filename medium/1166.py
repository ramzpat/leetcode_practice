# https://leetcode.com/problems/design-file-system/

from typing import Dict, List, Set

class pathTree:
  def __init__(self, folder_name:str, associated_value:int):
    self.folder_name = folder_name
    self.associated_value = associated_value 
    self.sub_dirs:Dict[str, pathTree] = {}
  
  def createFolder(self, folder_name:str, associated_value:int) -> bool:
    if folder_name in self.sub_dirs.keys():
      # Cannot create a folder because the same name already exists
      return False
    self.sub_dirs[folder_name] = (pathTree(folder_name, associated_value))
    return True 


class FileSystem:

  def __init__(self):
    self.root = pathTree("", 0)
    self.mapValue:Dict[str] = {}

  def createPath(self, path: str, value: int) -> bool:
    paths = path[1:].split(sep="/")
    depth = len(paths)
    ptr:pathTree = self.root
    for folder_name in paths[:depth-1]:
      if folder_name not in ptr.sub_dirs.keys():
        return False
      ptr = ptr.sub_dirs[folder_name]

    if len(paths[depth-1]) > 0 and ptr.createFolder(paths[depth-1], value):
      self.mapValue[path] = value
      return True 
    else:
      return False

  def get(self, path: str) -> int:
    return self.mapValue.get(path, -1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

# f = FileSystem()
# print(f.createPath("/a",1))
# print(f.get("/a"))


fileSystem = FileSystem()
print(fileSystem.createPath("/leet", 1))   # return true
print(fileSystem.createPath("/leet/code", 2))  # return true
print(fileSystem.get("/leet/code"))   # return 2
print(fileSystem.createPath("/c/d", 1))   # return false because the parent path "/c" doesn't exist.
print(fileSystem.get("/c"))  # return -1 because this path doesn't exist.