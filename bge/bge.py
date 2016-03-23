#     Dynamic text 3D - bge script
#     Mandax - Anderson Ferreira Pinto (mandax.contato@gmail.com)

import bge

controller = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
objs = scene.objects
objs_inactive = scene.objectsInactive
ob_scale = objs

def dt3d(text, target):
    target = objs[target]
    phrase = {}
    length = len(text)
    ob_x = target.position.x
    ob_y = target.position.y
    ob_z = target.position.z
    ob_col = 0
    chr_spacing = 0.3
    
    for x in range (0, length):
        this = text[x]
        
        if this == ' ':
            ob_x = ob_x + (1*chr_spacing)
        else:
            add = scene.addObject(this, target)
            add['letter'] = x
            phrase[add['letter']] = add
        
            add = phrase[x]
            
            ob = phrase[x]
            ob_col = ob_col+1
            ob_x = ob_x + (ob.localScale.x*chr_spacing)
        
            ob.setParent(target, True, False)
            ob.worldPosition = [ob_x, ob_y, ob_z]
            ob.applyRotation([1.57, 0, 0], True)
            
dt3d('This is a test', 'text_point')