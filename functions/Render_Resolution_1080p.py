import bpy 

class RENDER_OT_change_resolution_1920x1080p(bpy.types.Operator):
    """Change Default Resolution to 1920x1080p"""
    bl_idname = "render.resolution_1920x1080p"
    bl_label = "Change the Resolution to 1920x1080p"
    
    def execute(self, context):
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(RENDER_OT_change_resolution_1920x1080p)
        
def unregister():
    bpy.utils.unregister_class(RENDER_OT_change_resolution_1920x1080p)
        
if __name__ == "__main__":
    register()