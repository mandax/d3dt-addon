import bpy
from bpy.props import *
      
def initialize(scene):
    bpy.types.Scene._dt3d_objName = StringProperty(
        name = "Object name",
        description = "Alphabet parent name")
    
    bpy.types.Scene._dt3d_txtMaterial = StringProperty(
        name = "Material",
        description = "Select one material")
    
    bpy.types.Scene._dt3d_txtFont = StringProperty(
      name = "Font",
      default = "dt3d_default",
      description = "",
      subtype = 'FILE_PATH')
    
    bpy.types.Scene._dt3d_txtSize = FloatProperty(
        name = "Size",
        default = 0.3,
        description = "Set font size")
        
    bpy.types.Scene._dt3d_txtSpacing = FloatProperty(
        name = "Spacing",
        default = 0.7,
        description = "Set font spacing")
        
    bpy.types.Scene._dt3d_txtExtrude = FloatProperty(
        name = "Extrude",
        default = 0.05,
        description = "Set extrude value")
        
    bpy.types.Scene._dt3d_txtBevelDepth = FloatProperty(
        name = "Bevel depth",
        default = 0,
        description = "Set bevel depth value")
    
    bpy.types.Scene._dt3d_txtBevelResolution = FloatProperty(
        name = "Bevel resolution",
        default = 0,
        description = "Set bevel resolution value")
        
    bpy.types.Scene._dt3d_txtColumns = IntProperty(
        name = "Number of columns",
        default = 12,
        description = "Set max number of character columns")
        
    bpy.types.Scene._dt3d_txtHide = BoolProperty(
        name = "Hide characters",
        default = true, 
        description = "Check this if you want to hide the generated characters.")
    
    return
    
def clean():
  del bpy.types.Scene._dt3d_objName
  del bpy.types.Scene._dt3d_txtMaterial
  del bpy.types.Scene._dt3d_txtFont
  del bpy.types.Scene._dt3d_txtSize
  del bpy.types.Scene._dt3d_txtSpacing
  del bpy.types.Scene._dt3d_txtExtrude
  del bpy.types.Scene._dt3d_txtBevelDepth
  del bpy.types.Scene._dt3d_txtBevelResolution
  del bpy.types.Scene._dt3d_txtColumns
  del bpy.types.Scene._dt3d_txtHide
    
class DrawPanel(bpy.types.Panel):
    bl_label = "Characters generator"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOL_PROPS"
 
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        initialize(scene)
        
        layout.prop(scene, '_dt3d_objName')
        layout.prop_search(scene, '_dt3d_txtMaterial', bpy.data, 'materials', icon='MATERIAL')
        layout.prop(scene, '_dt3d_txtFont')
        
        layout.label("Font properties:")
        
        split = layout.split(percentage=0.5)
        
        col = split.column()
        col.prop(scene, '_dt3d_txtSize')
        col.prop(scene, '_dt3d_txtSpacing')
        col.prop(scene, '_dt3d_txtExtrude')
        
        col = split.column()
        col.prop(scene, '_dt3d_txtBevelDepth')
        col.prop(scene, '_dt3d_txtBevelResolution')
        col.prop(scene, '_dt3d_txtColumns')
        
        layout.prop(scene, '_dt3d_txtHide')    
        layout.operator('dt3d.generator')