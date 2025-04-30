import bpy


class RENDER_OT_cycle_gpu_button(bpy.types.Operator):
    """Change Render Settings to Cycles to work on the GPU"""
    bl_idname = "render.cycle_gpu_button"
    bl_label = "Change the Render Settings to Cycles on GPU"
    
    def execute(self, context):
        context.scene.render.engine = 'CYCLES'
        context.scene.cycles.device = 'GPU'
        context.scene.cycles.preview_samples = 100
        context.scene.cycles.use_preview_denoising = True
        context.scene.cycles.samples = 75
        context.scene.render.use_motion_blur = True
        context.scene.render.motion_blur_shutter = 0.5
        context.scene.render.use_persistent_data = True
        return {"FINISHED"}
    
def register():
    bpy.utils.register_class(RENDER_OT_cycle_gpu_button)
        
def unregister():
    bpy.utils.unregister_class(RENDER_OT_cycle_gpu_button)
        
if __name__ == "__main__":
    register()