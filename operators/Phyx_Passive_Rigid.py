import bpy 

class PHYSICS_OT_passive_rigid_body(bpy.types.Operator):
    """Adds a Passive Rigid Body"""  
    bl_idname = "physics.passive_rigid_body"
    bl_label = "Add Passive Rigid Body"
    
    def execute(self, context):
        bpy.ops.rigidbody.object_add()
        bpy.context.object.rigid_body.type = 'PASSIVE'
        bpy.context.object.rigid_body.collision_shape = 'MESH'
        
        return {"FINISHED"}
    
def register():
    bpy.utils.register_class(PHYSICS_OT_passive_rigid_body)
        
def unregister():
    bpy.utils.unregister_class(PHYSICS_OT_passive_rigid_body)
        
if __name__ == "__main__":
    register()