#     Dynamic text 3D - core
#     Mandax <mandax.contato@gmail.com>
#     http://blog.mandax.com.br

# TODO
# fix space character - get character size
# make wrap line
# make reduce size
# make Actuator
# make scroll box
# make virtual keyboard

import bge
from config import chr_parent, chr_spacing

controller = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
objs = scene.objects
ob_scale = objs

def theText(text, target):
    phrase = {}
    length = len(text)
    ob_x = target.position.x
    ob_y = target.position.y
    ob_z = target.position.z
    ob_col = 0
    
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
            
theText('I ae mocaaada', objs['sample'])
theText('teting', objs['teting'])