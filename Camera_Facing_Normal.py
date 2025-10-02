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

class RENDER_OT_CameraFacingNormal(bpy.types.Operator):
    bl_label="Render the normal map facing the camera"
    bl_idname="render.camera_facing_normal"
    bl_options={'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return context.space_data.type == 'VIEW_3D' and context.scene is not None

    def execute(self, context):
        camera = context.scene.camera
        if  camera and camera.data.type != 'ORTHO':
            self.report({'WARNING'}, "Using non orthographic camera will lead to a gradient on the normal map")
        context.scene.render.engine = 'BLENDER_WORKBENCH'
        context.scene.display.shading.light = 'MATCAP'
        bpy.context.scene.display.shading.studio_light = 'check_normal+y.exr'
        bpy.context.scene.display.shading.color_type = 'SINGLE'
        bpy.context.scene.display.shading.single_color = (1, 1, 1)
        bpy.ops.render.render('INVOKE_DEFAULT')
        bpy.context.scene.view_settings.view_transform = 'Standard'
        bpy.context.scene.world.color = (0.21423, 0.21423, 0.99902)
        return {'FINISHED'}


class NORMALCAMERA_PT_Panel(bpy.types.Panel):
    bl_label = "Camera Facing Normal"
    bl_idname = "NORMALCAMERA_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Camera Facing Normal'

    def draw(self, context):
        layout = self.layout
        layout.operator("render.camera_facing_normal", text="Render", icon='RENDER_STILL')

def register():
    bpy.utils.register_class(NORMALCAMERA_PT_Panel)
    bpy.utils.register_class(RENDER_OT_CameraFacingNormal)

def unregister():
    bpy.utils.unregister_class(NORMALCAMERA_PT_Panel)
    bpy.utils.unregister_class(RENDER_OT_CameraFacingNormal)

if __name__ == "__main__":
    register()