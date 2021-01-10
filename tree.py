class _TreeNode:
    def __init__(self, element, parent):
        self._key = element
        self._children = []
        self._parent = parent

    def size(self):
        pass

    def element(self):
        pass

    def parent(self):
        return self._parent

    def isRoot(self):
        return self._parent is None

class _File(_TreeNode):
    def __init__(self, name, parentDirectory, size):
        super().__init__(name, parentDirectory)
        self.__size = size

    def size(self):
        return self.__size

    def element(self):
        return "f: " + self._key
    

class _Directory(_TreeNode):
    def __init__(self, name, parentDirectory):
        super().__init__(name, parentDirectory)

    def size(self):  
        s = 0
        for node in self._children:
            s += node.size()
        return s

    def items(self):
        return map(lambda i: i.element(), self._children)

    def addChild(self, item):
        self._children.append(item)

    def element(self):
        return "d: " + self._key

    def find(self, name):
        for child in self._children:
            if child._key == name:
                return child
        return None

class Tree:
    def __init__(self):
        self.__root = _Directory("/", None)
        self.__current = self.__root

    def ls(self):
        return list(self.__current.items())

    def touch(self, name, size):
        self.__current.addChild(_File(name, self.__current, size))

    def mkdir(self, name):
        self.__current.addChild(_Directory(name, self.__current))

    def cd(self, param):
        if param == ".." and not self.__current.isRoot():
            self.__current = self.__current.parent()
        else:
            node = self.__current.find(param)
            if node is None:
                return
            else:
                self.__current = node
        self.path()


    def path(self):
        path = ""
        arr = []
        node = self.__current
        while node:
            if not node.isRoot():
                arr.append(node._key + "/")
            else:
                arr.append(node._key)
                    
            node = node.parent()
        for i in range(len(arr)-1 , -1, -1):
            path += arr[i]

        print(path) 

tree = Tree()
tree.mkdir("home")
tree.cd("home")
tree.mkdir("user")
tree.cd("user")
tree.path()
