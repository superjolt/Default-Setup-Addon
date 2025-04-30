import bpy

class EXTERNAL_DATA_OT_relative_files(bpy.types.Operator):
    """Makes all external files and textures have relative file path"""
    bl_idname = "external.data_relative_files"
    bl_label = "Relative Files"

    def execute(self, context):
        bpy.ops.file.make_paths_relative()
        self.report({'INFO'}, "Files Paths Made Relative.")
        return {"FINISHED"}
    
def register():
    bpy.utils.register_class(EXTERNAL_DATA_OT_relative_files)
        
def unregister():
    bpy.utils.unregister_class(EXTERNAL_DATA_OT_relative_files)
        
if __name__ == "__main__":
    register()