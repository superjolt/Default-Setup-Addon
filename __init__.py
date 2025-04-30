import bpy

from . Operators import (
    Render_GPU_btn,
    Render_Optimize_Cycles,
    Constraint_Track,
    Constraint_Track_Remove,
    Data_Purge_Unused,
    External_Data_Pack,
    External_Data_Relative,
    Material_Rainbow_BSDF,
    Material_Rainbow_Color_Ramp,
    Output_Exr_Btn,
    Output_Mp4_Btn,
    Phyx_Active_Rigid,
    Phyx_Clear_Rigid,
    Phyx_Cloth_Collision,
    Phyx_Cloth_Collision_Clear,
    Phyx_Cloth_Sim,
    Phyx_Cloth_Sim_Clear,
    Phyx_Passive_Rigid,
    Render_Resolution_1080p,
    Render_Resolution_1440p,
    World_SkyTex_Btn,
)

class VIEW3D_PT_Default_Setup_Addon(bpy.types.Panel):
    bl_label = "Default Setup"
    bl_idname = "VIEW3D_PT_Default_Setup_Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Default Setup"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
class VIEW3D_PT_Render_Settings(bpy.types.Panel):
    """Render Settings"""
    bl_label = "Render Settings"
    bl_idname = "VIEW3D_PT_Render_Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "VIEW3D_PT_Default_Setup_Addon"
    #bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("render.cycle_gpu_button", text="Render Engine to Cycles", icon="OUTLINER_OB_CAMERA")
        row = layout.row()
        row.operator("render.render_optimization", text="Optimize Render", icon="SHADING_RENDERED")
        
        
        # Row for adding the Nishita sky texture
        row = layout.row()
        row.operator("world.add_nishita_sky_texture", text="Add Fine Tuned Sky Texture", icon="WORLD")
        
class VIEW3D_PT_Output_Settings(bpy.types.Panel):
    """Output Settings"""
    bl_label = "Output Settings"
    bl_idname = "VIEW3D_PT_Output_Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "VIEW3D_PT_Default_Setup_Addon"
    #bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("render.resolution_1440p", text="1440p Camera Resolution", icon="VIEW_CAMERA")
        row = layout.row()
        row.operator("render.resolution_1920x1080p", text="Portrait Camera Resolution", icon="VIEW_CAMERA")
        row = layout.row()
        row.operator("output.equal_to_exr", text="Output as EXR", icon="IMAGE_DATA")
        row = layout.row()
        row.operator("output.equal_to_mp4", text="Output as MP4", icon="FILE_MOVIE")

class VIEW3D_PT_File_Sharing(bpy.types.Panel):
    """File Sharing"""
    bl_label = "File Sharing"
    bl_idname = "VIEW3D_PT_File_Sharing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "VIEW3D_PT_Default_Setup_Addon"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("external.data_pack_resources", text="Pack Resources", icon="PACKAGE")
        row = layout.row()
        row.operator("external.data_relative_files", text="Make Paths Relative", icon="FILEBROWSER")
        row = layout.row()
        row.operator("data.purge_unused", text = "Delete Unused Data", icon = "TRASH")
        
class VIEW3D_PT_Physics_Tab_Settings(bpy.types.Panel):
    """Rigid Body Settings Panel"""
    bl_label = "Physics Settings"
    bl_idname = "VIEW3D_PT_Physics_Tab_Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "VIEW3D_PT_Default_Setup_Addon"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()   

class VIEW3D_PT_Rigid_Bodies(bpy.types.Panel):
    """Rigid Bodies"""
    bl_label = "Rigid Bodies"
    bl_idname = "VIEW3D_PT_Rigid_Bodies"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "VIEW3D_PT_Physics_Tab_Settings"
    #bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        row = layout.row()

        row.label(text="Rigid Bodies")
        row = layout.row(align=True)  # Corrected to align buttons
        row.operator("physics.active_rigid_body", text="Active Collision", icon="RIGID_BODY")
        row.operator("physics.passive_rigid_body", text="Passive Collision", icon="RIGID_BODY")
        row = layout.row()
        row.operator("physics.clear_rigid_body", text="Clear Active Rigid Bodies", icon="CANCEL")
        layout.separator()
        
class VIEW3D_PT_Cloth_sims(bpy.types.Panel):
    """Cloth Simulations"""
    bl_label = "Cloth Simulations"
    bl_idname = "VIEW3D_PT_Cloth_sims"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "VIEW3D_PT_Physics_Tab_Settings"
    #bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        row = layout.row()

        row.label(text ="Cloth Simulations")
        row = layout.row()
        row.operator("physics.cloth_sims", text = "Add Cloth Sim", icon="MOD_CLOTH")
        row = layout.row()
        row.operator("physics.cloth_sims_collision", text = "Add Collision to Active Object", icon="MOD_PHYSICS")
        row = layout.row()
        row.operator("physics.clear_cloth_sims", text = "Clear Cloth Sim", icon = "CANCEL")
        row.operator("physics.clear_collision", text = "Clear Collisons")
        
class VIEW3D_PT_Object_Constraints(bpy.types.Panel):
    """Object Constraints Settings Panel"""
    bl_label = "Object Constraints Settings"
    bl_idname = "VIEW3D_PT_Object_Constraints"  # Ensure to add an ID
    bl_parent_id = "VIEW3D_PT_Default_Setup_Addon"
    bl_space_type = "VIEW_3D"  # Match parent space type
    bl_region_type = "UI"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("constraints.add_track_to_constraint", text='Add "Track To" Constraint')
        row = layout.row()
        row.operator("constraints.remove_track_to_constraint", text='Remove "Track To" Constraint')
        
class VIEW3D_PT_Misc(bpy.types.Panel):
    """Miscellaneous Buttons"""
    bl_label = "Miscellaneous Functions"
    bl_idname = "VIEW3D_PT_Misc"  # Ensure to add an ID
    bl_parent_id = "VIEW3D_PT_Default_Setup_Addon"
    bl_space_type = "VIEW_3D"  # Match parent space type
    bl_region_type = "UI"
    #bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
                
        # Row for toggling specific overlays
        row = layout.row()
        row.operator("view3d.toggle_overlays", text="Toggle Specific Overlays", icon="OVERLAY")
        layout.separator()
        
        #Row for adding Rainbow Colour Ramp w bsdf
        row = layout.row()
        row.operator("material.rainbow_colour_with_principled_bsdf", text = "Add Rainbow Color Ramp with BSDF", icon = "MATERIAL")
        
        # Row for adding Rainbow Colour alone
        row = layout.row()
        row.operator("material.rainbow", text = "Add Rainbow Color Ramp", icon = "MATERIAL")
        
class VIEW3D_OT_toggle_overlays(bpy.types.Operator):
    """Toggle Overlays"""
    bl_idname = "view3d.toggle_overlays"
    bl_label = "Toggle Overlays"
    
    def execute(self, context):
        overlay = context.space_data.overlay
        context.space_data.overlay.show_stats = True
        overlay.show_axis_z = not overlay.show_axis_z  # Toggle the Z-axis overlay
        return {"FINISHED"}

""" Old classes
classes = [
    VIEW3D_PT_Default_Setup_Addon,
    VIEW3D_PT_Render_Settings,
    VIEW3D_PT_Output_Settings,
    VIEW3D_PT_File_Sharing,
    VIEW3D_PT_Physics_Tab_Settings,
    VIEW3D_PT_Cloth_sims,
    VIEW3D_PT_Rigid_Bodies,
    VIEW3D_PT_Object_Constraints,
    VIEW3D_PT_Misc,

    VIEW3D_OT_toggle_overlays,
    
    RENDER_OT_cycle_gpu_button,
    RENDER_OT_change_resolution_1440p,
    RENDER_OT_change_resolution_1920x1080p,
    RENDER_OT_render_optimization,
    WORLD_OT_sky_texture_button,

    OUTPUT_OT_mp4_video_button,
    OUTPUT_OT_exr_video_button,

    EXTERNAL_DATA_OT_pack_resources,
    EXTERNAL_DATA_OT_relative_files,
    DATA_OT_purge_unused,
    
    PHYSICS_OT_passive_rigid_body,
    PHYSICS_OT_active_rigid_body,
    PHYSICS_OT_clear_rigid_body,

    CONSTRAINT_OT_add_track_to_constraint,
    CONSTRAINT_OT_remove_track_to_constraint,

    Material_OT_rainbow_colour_with_principled_bsdf,
    Material_OT_rainbow_colour,

    PHYSICS_OT_cloth_sims,
    PHYSICS_OT_cloth_sims_collision,
    PHYSICS_OT_cloth_sims_clear,
    PHYSICS_OT_collision_sims_clear,
    
]
"""

classes = [
    VIEW3D_PT_Default_Setup_Addon,
    VIEW3D_PT_Render_Settings,
    VIEW3D_PT_Output_Settings,
    VIEW3D_PT_File_Sharing,
    VIEW3D_PT_Physics_Tab_Settings,
    VIEW3D_PT_Rigid_Bodies,
    VIEW3D_PT_Cloth_sims,
    VIEW3D_PT_Object_Constraints,
    VIEW3D_PT_Misc,
    
    VIEW3D_OT_toggle_overlays,

    Render_GPU_btn,
    Render_Optimize_Cycles,

    Constraint_Track,
    Constraint_Track_Remove,
    Data_Purge_Unused,
    External_Data_Pack,
    External_Data_Relative,

    Material_Rainbow_BSDF,
    Material_Rainbow_Color_Ramp,

    Output_Exr_Btn,
    Output_Mp4_Btn,

    Phyx_Active_Rigid,
    Phyx_Clear_Rigid,
    Phyx_Cloth_Collision,
    Phyx_Cloth_Collision_Clear,
    Phyx_Cloth_Sim,
    Phyx_Cloth_Sim_Clear,
    Phyx_Passive_Rigid,
    
    Render_Resolution_1080p,
    Render_Resolution_1440p,
    World_SkyTex_Btn,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
    