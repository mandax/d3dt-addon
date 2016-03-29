import bge

scene = bge.logic.getCurrentScene()
controller = bge.logic.getCurrentController()
collection_parent = controller.owner.get('d3dt_collection')
text = controller.owner.get('d3dt_text')
collection = { obj.name: obj for obj in scene.objectsInactive if obj.parent and obj.parent.name == collection_parent }

for char in text:
  if char != ' ':
    collection[char].position = controller.owner.position
    scene.addObject(collection[char])