bl_info = {
    "name": "D3DT - Dynamic 3D Text",
    "author": "Anderson Ferreira Pinto (Mandax)",
    "version": (0, 1, 2),
    "blender": (2, 7, 7),
    "location": "Panel",
    "description": "Generate 3D characters to be used on BGE",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Add Mesh"}

import bpy
from bpy.props import *
from . import ui
from . import logic

def register():
    ui.initialize()
    bpy.utils.register_class(ui.DrawPanel)
    bpy.utils.register_class(logic.TextGenerator)

def unregister():
    bpy.utils.unregister_class(ui.DrawPanel)
    bpy.utils.unregister_class(ui.TextGenerator)
    ui.clean()
    
if __name__ == "__main__":
    register()
