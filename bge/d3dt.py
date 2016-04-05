import bge

scene = bge.logic.getCurrentScene()
controller = bge.logic.getCurrentController()
collection_parent = controller.owner.get('d3dt_collection')
collection = { obj.name: obj for obj in scene.objectsInactive if obj.parent and obj.parent.name == collection_parent }

def add(charObj):
  return scene.addObject(charObj, controller.owner, 0)
  
def placeObject(obj, column):
  scale = controller.owner.localScale.x
  offset = 0.025*scale

  obj.position.x = (scale+offset)*column
  obj.scaling = controller.owner.scaling
  obj.visible = True
  obj.setParent(controller.owner)

def spawn(text):
  column = 0
  for char in text:
    if char != ' ':
      placeObject(add(collection[char]), column)
      column += 1
      
spawn(controller.owner.get('d3dt_text'))