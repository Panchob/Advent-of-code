from Instance import Instance
import copy

class Node():
    def __init__(self, path):
        self.__path = path
        self.__weight = 0
        self.__parent = None
        self.__children = None
    
    def __repr__(self):
        return ("{value}, {weight}").format(value = self.__path, weight = self.__weight)
    
    def path(self):
        return self.__path
    
    def listKeys(self):
        keys = []
        for elem in self.__path:
            if elem.islower():
                keys.append(elem)
        return keys

    def weight(self, instance):
        path = self.__path
        weight = 0

        for c in path:
            weight += instance.nbStepTo(c, instance.position())
            instance.toggleFound()

        self.__weight = weight
        return weight


def createGraphFromString(string):
    graph = []
    line = []
    x, y = 0, 0
    for character in string:
        if character == '\n':
            graph.append(line[:])
            line = []
        else:
            line.append(character)

    return graph


def generateAllNodes(paths):
    nodes = []

    for p in paths:
        nodes.append(Node("".join(p)))

    return nodes


def minNumberOfSteps(instance):
        totals = []
        global visited
        visited = {}

        # A node represent a path, not a single point. Each nodes have its own instance.
        # Example ['aA']
        nodes = generateAllNodes(instance.generateAllPossiblePath())
  
        for n in nodes:
            totals.append(deepSearch(n, copy.deepcopy(instance)))
    
        return min(totals)

visited = {}
def deepSearch(node, instance):
    # From the current node, generate all possible path.
    # Example: ['b']
    instance.keyFound(node.listKeys())
    p = node.path()

    if p in visited:
        weight = visited[p] + instance.nbStepTo(p[0], instance.position())
        instance.setCurrentPosition(instance.getPostionFromValue(p[-1]))
    else:
        buffer = instance.nbStepTo(p[0], instance.position())
        weight = node.weight(instance)
        if len(p) > 1:
            visited[p] = weight
        weight += buffer

    instance.updateTokens()
    newNodes = generateAllNodes(instance.generateAllPossiblePath())
    children = []

    for n in newNodes:
        path = n.path()
        w = deepSearch(n, copy.deepcopy(instance))
        children.append(w)
            
    if children:
        weight += min(children)

    return weight


if __name__ == "__main__":
        # Graph example:#########
                        #b.A.@.a#
                        #########

        graph = createGraphFromString("#########\n#b.A.@.a#\n#########\n")
        # An instance contains useful information of a search
        # - Graph
        # - Current Position
        # - Key found
        # - Number of step taken
        # - All available keys and doors for the current position
        instance = Instance(graph)
        
        # Find all available keys and doors and store it in the first instance
        instance.updateTokens()
        instance.listPositions()
        minNumberOfSteps(instance)


    

