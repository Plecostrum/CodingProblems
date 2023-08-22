class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    val = node.val
    if node.left:
        left = serialize(node.left)
    else:
        left = None
    if node.right:
        right = serialize(node.right)
    else:
        right = None
    serialized = [val, left, right]
    return serialized

def deserialize(serializedTree):
    if not serializedTree:
        return None
    value = serializedTree[0]
    if serializedTree[1]:
        left = deserialize(serializedTree[1])
    else:
        left = None
    if serializedTree[2]:
        right = deserialize(serializedTree[2])
    else:
        right = None
    return (Node(value,left,right))
    


if __name__=="__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(node))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
