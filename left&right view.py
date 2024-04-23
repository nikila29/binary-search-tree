class Node:
    def __init__(self,d):
        self.lc=None
        self.rc=None
        self.data=d
        self.hd=0
def level_order(root):
    level_map={}
    q=[(root,0)]
    while q:
        node,level=q.pop(0)
        if level not in level_map:
            level_map[level]=[]
        level_map[level].append(node.data)
        if node.lc:
            q.append((node.lc,level+1))
        if node.rc:
            q.append((node.rc,level+1))
    print ("\nlevel_order:")
    for level in level_map:
        print(level,":",level_map[level])
    print ("\nleft view")
    for level in level_map:
        print(level,":",level_map[level][0],end=",")
    print ("\nright view")
    for level in level_map:
        print(level,":",level_map[level][-1],end=",")
root=Node(1)
root.lc=Node(2)
root.rc=Node(3)
root.lc.lc=Node(4)
root.lc.rc=Node(5)
root.rc.lc=Node(6)
root.rc.rc=Node(7)
root.lc.rc.lc=Node(8)
root.rc.lc.rc=Node(9) 
level_order(root)
