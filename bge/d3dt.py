import bge

scene = bge.logic.getCurrentScene()
controller = bge.logic.getCurrentController()
collection_parent = controller.owner.get('d3dt_collection')
collection = { obj.name: obj for obj in scene.objectsInactive if obj.parent and obj.parent.name == collection_parent }

def add(charObj):
  obj = scene.addObject(charObj, controller.owner, 0)
  obj.orientation = controller.owner.orientation
  obj.visible = True

def spawn(text):
  i = 0
  for char in text:
    if char != ' ':
      add(collection[char])
      
spawn(controller.owner.get('d3dt_text'))