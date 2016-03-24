import bpy
from bpy.props import *
      
def initialize():
    bpy.types.Scene.d3dt_objName = StringProperty(
        name = "Object name",
        default = "d3dt_default",
        description = "Alphabet parent name")
    
    bpy.types.Scene.d3dt_txtMaterial = StringProperty(
        name = "Material",
        description = "Select one material")
    
    bpy.types.Scene.d3dt_txtFont = StringProperty(
      name = "Font",
      description = "",
      subtype = 'FILE_PATH')
    
    bpy.types.Scene.d3dt_txtSize = FloatProperty(
        name = "Size",
        default = 0.3,
        description = "Set font size")
        
    bpy.types.Scene.d3dt_txtSpacing = FloatProperty(
        name = "Spacing",
        default = 0.7,
        description = "Set font spacing")
        
    bpy.types.Scene.d3dt_txtExtrude = FloatProperty(
        name = "Extrude",
        default = 0.05,
        description = "Set extrude value")
        
    bpy.types.Scene.d3dt_txtBevelDepth = FloatProperty(
        name = "Bevel depth",
        default = 0,
        description = "Set bevel depth value")
    
    bpy.types.Scene.d3dt_txtBevelResolution = FloatProperty(
        name = "Bevel resolution",
        default = 0,
        description = "Set bevel resolution value")
        
    bpy.types.Scene.d3dt_txtColumns = IntProperty(
        name = "Number of columns",
        default = 12,
        description = "Set max number of character columns")
        
    bpy.types.Scene.d3dt_txtHide = BoolProperty(
        name = "Hide characters",
        default = 1, 
        description = "Check this if you want to hide the generated characters.")
    
    return
    
def clean():
  del bpy.types.Scene.d3dt_objName
  del bpy.types.Scene.d3dt_txtMaterial
  del bpy.types.Scene.d3dt_txtFont
  del bpy.types.Scene.d3dt_txtSize
  del bpy.types.Scene.d3dt_txtSpacing
  del bpy.types.Scene.d3dt_txtExtrude
  del bpy.types.Scene.d3dt_txtBevelDepth
  del bpy.types.Scene.d3dt_txtBevelResolution
  del bpy.types.Scene.d3dt_txtColumns
  del bpy.types.Scene.d3dt_txtHide
    
class DrawPanel(bpy.types.Panel):
    bl_label = "Characters generator"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOL_PROPS"
 
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        layout.prop(scene, 'd3dt_objName')
        layout.prop_search(scene, 'd3dt_txtMaterial', bpy.data, 'materials', icon='MATERIAL')
        layout.prop(scene, 'd3dt_txtFont')
        
        layout.label("Font properties:")
        
        split = layout.split(percentage=0.5)
        
        col = split.column()
        col.prop(scene, 'd3dt_txtSize')
        col.prop(scene, 'd3dt_txtSpacing')
        col.prop(scene, 'd3dt_txtExtrude')
        
        col = split.column()
        col.prop(scene, 'd3dt_txtBevelDepth')
        col.prop(scene, 'd3dt_txtBevelResolution')
        col.prop(scene, 'd3dt_txtColumns')
        
        layout.prop(scene, 'd3dt_txtHide')    
        layout.operator('d3dt.generator')