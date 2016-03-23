bl_info = {
    "name": "DT3D - Dynamic Text 3D",
    "author": "Anderson Ferreira Pinto (Mandax)",
    "version": (0, 1),
    "blender": (2, 7, 7),
    "location": "Panel",
    "description": "Generate 3D alphabet to be used on BGE",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Add Mesh"}

import bpy
from bpy.props import *
from . import ui
from . import logic

def register():
    bpy.utils.register_class(ui.DrawPanel)
    bpy.utils.register_class(logic.TextGenerator)

def unregister():
    bpy.utils.unregister_class(ui.DrawPanel)
    bpy.utils.unregister_class(ui.TextGenerator)
    ui.clean()
    
if __name__ == "__main__":
    register()
