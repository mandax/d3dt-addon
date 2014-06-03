#     Dynamic text 3D generator
#     Mandax (mandax.com.br)

# TODO
# fix spacing creating
# pull existing text properties

import bpy 
from bpy.props import *
import math
from math import pi
from config import *
                         
      
def initDefaultProps(scn):
    bpy.types.Scene.objName = StringProperty(
        name = "Object name",
        description = "Alphabet parent name")
    scn['objName'] = "dt3d_alphabet"
    
    bpy.types.Scene.txtMaterial = StringProperty(
        name = "Material",
        description = "Select one material")
    
    bpy.types.Scene.txtFont = StringProperty(
      name = "Font",
      default = "",
      description = "",
      subtype = 'FILE_PATH')
    
    bpy.types.Scene.txtSize = FloatProperty(
        name = "Size",
        default = 0.3,
        description = "Set font size")
        
    bpy.types.Scene.txtSpacing = FloatProperty(
        name = "Spacing",
        default = 0.7,
        description = "Set font spacing")
        
    bpy.types.Scene.txtExtrude = FloatProperty(
        name = "Extrude",
        default = 0.05,
        description = "Set extrude value")
        
    bpy.types.Scene.txtBevelDepth = FloatProperty(
        name = "Bevel depth",
        default = 0,
        description = "Set bevel depth value")
    
    bpy.types.Scene.txtBevelResolution = FloatProperty(
        name = "Bevel resolution",
        default = 0,
        description = "Set bevel resolution value")
        
    bpy.types.Scene.txtColumns = IntProperty(
        name = "Number of columns",
        default = 12,
        description = "Set max number of character columns")
        
    bpy.types.Scene.txtHide = BoolProperty(
        name = "Hide characters", 
        description = "Check this if you want to hide the generated characters.")
    scn['txtHide'] = True
    
    return
 
initDefaultProps(bpy.context.scene)

        
class drawPanel(bpy.types.Panel):
    bl_label = "DoGUI - Characters generator"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOL_PROPS"
 
    def draw(self, context):
        layout = self.layout
        scn = context.scene
        layout.prop(scn, 'objName')
        layout.prop_search(scn, 'txtMaterial', bpy.data, 'materials', icon='MATERIAL')
        layout.prop(scn, 'txtFont')
        
        layout.label("Font properties:")
        
        split = layout.split(percentage=0.5)
        col = split.column()
        col.prop(scn, 'txtSize')
        col.prop(scn, 'txtSpacing')
        col.prop(scn, 'txtExtrude')
        col = split.column()
        col.prop(scn, 'txtBevelDepth')
        col.prop(scn, 'txtBevelResolution')
        col.prop(scn, 'txtColumns')
        
        layout.prop(scn, 'txtHide')    
        layout.operator("dt3d.generator")
        
              
class TextGenerator(bpy.types.Operator):
    bl_idname = "dt3d.generator"
    bl_label = "Generate"
 
    def execute(self, context):
        scn = context.scene
        
        font = bpy.data.fonts.load(scn.txtFont) 
        mat = bpy.data.materials[scn.txtMaterial]

        #empty obj alphabet
        bpy.ops.object.empty_add( 
        type = 'PLAIN_AXES', 
        view_align = False, 
        location = (0, 0, 0))
        chars = bpy.context.object
        chars.name = scn.objName
        chars.hide = scn.txtHide

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
            ob.data.size = scn.txtSize
            ob.data.bevel_depth = scn.txtBevelDepth
            ob.data.bevel_resolution = scn.txtBevelResolution
            ob.data.extrude = scn.txtExtrude
            ob.data.materials.append(mat)
            ob.data.font = font
            ob.parent = chars

            bpy.ops.object.convert(target='MESH', keep_original = False)
            meshed = bpy.data.objects[current_chr]
            meshed.hide = chr_hide                                         
            meshed.hide_render = chr_hide 
            meshed_x = column_count*(meshed.scale.x*scn.txtSpacing)
        
            column_count = column_count+1
      
            if column_count == scn.txtColumns:
                column_count = 0
                line_count = line_count+1     
                meshed_z = -1*(line_count*(meshed.scale.z*scn.txtSpacing))
           
            #position        
            meshed.location.x = meshed_x
            meshed.location.y = meshed_y
            meshed.location.z = meshed_z
       
        print('GENERATED!')
        
        return{'FINISHED'}


    
def register():
    bpy.utils.register_module(__name__)
    bpy.types.Scene.theChosenObject = bpy.props.StringProperty()

def unregister():
    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.objName
    del bpy.types.Scene.txtMaterial
    del bpy.types.Scene.txtFont
    del bpy.types.Scene.txtSize
    del bpy.types.Scene.txtSpacing
    del bpy.types.Scene.txtExtrude
    del bpy.types.Scene.txtBevelDepth
    del bpy.types.Scene.txtBevelResolution
    del bpy.types.Scene.txtColumns
    del bpy.types.Scene.txtHide
    
if __name__ == "__main__":
    register()
