import bpy
import math
from math import pi

class TextGenerator(bpy.types.Operator):
    bl_idname = "d3dt.generator"
    bl_label = "Generate"
 
    def execute(self, context):
        scn = context.scene
        
        font = bpy.data.fonts.load(scn.d3dt_txtFont) 
        mat = bpy.data.materials[scn.d3dt_txtMaterial]

        bpy.ops.object.empty_add( 
          type = 'PLAIN_AXES', 
          view_align = False, 
          location = (0, 0, 0))
        
        chars = bpy.context.object
        chars.name = scn.d3dt_objName
        chars.hide = scn.d3dt_txtHide

        meshed_x = chars.location.x
        meshed_y = chars.location.y
        meshed_z = chars.location.z

        column_count = 0
        line_count = 0
    
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
            ob.data.size = scn.d3dt_txtSize
            ob.data.bevel_depth = scn.d3dt_txtBevelDepth
            ob.data.bevel_resolution = scn.d3dt_txtBevelResolution
            ob.data.extrude = scn.d3dt_txtExtrude
            ob.data.materials.append(mat)
            ob.data.font = font
            ob.parent = chars

            bpy.ops.object.convert(target='MESH', keep_original = False)
            meshed = bpy.data.objects[current_chr]                               
            meshed.hide_render = scn.d3dt_txtHide
            meshed.hide = scn.d3dt_txtHide
            meshed_x = column_count*(meshed.scale.x*scn.d3dt_txtSpacing)
        
            column_count = column_count+1
      
            if column_count == scn.d3dt_txtColumns:
                column_count = 0
                line_count = line_count+1     
                meshed_z = -1*(line_count*(meshed.scale.z*scn.d3dt_txtSpacing))
           
            meshed.location.x = meshed_x
            meshed.location.y = meshed_y
            meshed.location.z = meshed_z
       
        print('GENERATED!')
        
        return{'FINISHED'}
