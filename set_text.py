#     Dynamic text 3D - converter
#     Mandax (http://blog.mandax.com.br)

import bge
from config import chr_parent, chr_spacing

controller = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
objs = scene.objects
phrase = {}

sample = 'This is a fucking test, dude!'
length = len(sample)
target = objs['sample']
ob_x = target.position.x
ob_y = target.position.y
ob_z = target.position.z
ob_col = 0

target.applyRotation([1.57, 0, 0], True)

for x in range (0, length):
    this = sample[x]
    
    if this == ' ':
        ob_col = ob_col+1
    else:
        add = scene.addObject(this, target)
        add['letter'] = x
        phrase[add['letter']] = add
    
        add = phrase[x]
        
        ob = phrase[x]
        ob_col = ob_col+1
        ob_x = ob_col*(ob.localScale.x*chr_spacing)
    
        ob.setParent(target, True, False)
        ob.worldPosition = [ob_x, ob_y, ob_z]

        
        
        
    