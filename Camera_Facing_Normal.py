bl_info = {
    "name": "Camera Facing Normal",
    "author": "Lambdah",
    "version": (0,0,1),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Camera Facing Normal",
    "description": "Takes a rendered normal map facing towards the camera",
    "doc_url": "https://github.com/Lambdah/Camera_Facing_Normal",
    "category": "Renders"
}

import bpy

class NORMALCAMERA_PT_Panel(bpy.types.Panel):
    bl_label = "Camera Facing Normal"
    bl_idname = "NORMALCAMERA_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Camera Facing Normal'

    def draw(self, context):
        layout = self.layout

def register():
    bpy.utils.register_class(NORMALCAMERA_PT_Panel)

def unregister():
    bpy.utils.unregister_class(NORMALCAMERA_PT_Panel)

if __name__ == "__main__":
    register()