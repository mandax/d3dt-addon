#     Dynamic text 3D - creator
#     Mandax (http://blog.mandax.com.br)

# TODO
# check if empty exists
# errors tratment
# fix layers creating
# fix spacing creating

import bpy 
import math
from math import pi
from config import *
                              
font = bpy.data.fonts.load(chr_font) 
mat = bpy.data.materials[chr_material]

#creating a empty object, to be a parent of all characteres
bpy.ops.object.empty_add( 
type = 'PLAIN_AXES', 
view_align = False, 
location = (0, 0, 0))
chars = bpy.context.object
chars.name = chr_parent
chars.hide = chr_hide

meshed_x = chars.location.x
meshed_y = chars.location.y
meshed_z = chars.location.z

column_count = 0
line_count = 0

#the magic happens
for i, x in enumerate(range(ord('!'), ord('~'))):
    current_chr = chr(x)
    
    bpy.ops.object.text_add(
    location = (0, 0, 0),
    rotation = (pi/2, 0, 0))
    
    ob = bpy.context.object
    ob.name = current_chr
    ob.data.name = current_chr
    ob.data.body = current_chr
    ob.data.align = 'CENTER'
    ob.data.size = chr_size
    ob.data.bevel_depth = chr_bevel_depth
    ob.data.bevel_resolution = chr_bevel_resolution
    ob.data.extrude = chr_extrude
    ob.data.materials.append(mat)
    ob.data.font = font
    ob.parent = chars

    bpy.ops.object.convert(target='MESH', keep_original = False)
    meshed = bpy.data.objects[current_chr]
    meshed.hide = chr_hide                                         
    meshed.hide_render = chr_hide 
    meshed_x = column_count*(meshed.scale.x*chr_spacing)
    
    column_count = column_count+1
  
    if column_count == columns:
        column_count = 0
        line_count = line_count+1     
        meshed_z = -1*(line_count*(meshed.scale.z*chr_spacing))
        
    #Setting letter position        
    meshed.location.x = meshed_x
    meshed.location.y = meshed_y
    meshed.location.z = meshed_z
    
    #hide in second layer
    chars.layers = 20*[False]
    meshed.layers = 20*[False]
    chars.layers[1] = True
    meshed.layers[1] = True