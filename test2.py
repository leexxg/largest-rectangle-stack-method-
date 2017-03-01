from xml.etree import ElementTree
d,level = {'red' : 0, 'green':0,  'blue':0},1
def getChildren(root,level):
    level+=1
    for child in root:  
        d[child.attrib['color']] += level
        getChildren(child,level)
x='<cube color="blue"><cube color="red"><cube color="green"><cube color="red"></cube></cube></cube><cube color="red"></cube></cube>'        
tree=ElementTree.fromstring(x)
d[tree.attrib['color']] += level
getChildren(tree,level)
print(d['red'],d['green'],d['blue'])
    

