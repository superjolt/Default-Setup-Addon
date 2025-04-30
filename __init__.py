import bpy

from . operators import Render_GPU_btn
from . operators import Render_Optimize_Cycles
from . operators import Constraint_Track
from . operators import Constraint_Track_Remove
from . operators import Data_Purge_Unused
from . operators import External_Data_Pack
from . operators import External_Data_Relative
from . operators import Material_Rainbow_BSDF
from . operators import Material_Rainbow_Color_Ramp
from . operators import Output_Exr_Btn
from . operators import Output_Mp4_Btn
from . operators import Phyx_Active_Rigid
from . operators import Phyx_Clear_Rigid
from . operators import Phyx_Cloth_Collision
from . operators import Phyx_Cloth_Collision_Clear
from . operators import Phyx_Cloth_Sim
from . operators import Phyx_Cloth_Sim_Clear
from . operators import Phyx_Passive_Rigid
from . operators import Render_Resolution_1080p
from . operators import Render_Resolution_1440p
from . operators import World_SkyTex_Btn

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


classes = (
    VIEW3D_PT_Default_Setup_Addon,
    VIEW3D_PT_Render_Settings,
    VIEW3D_PT_Output_Settings,
    VIEW3D_PT_File_Sharing,
    VIEW3D_PT_Physics_Tab_Settings,
    VIEW3D_PT_Rigid_Bodies,
    VIEW3D_PT_Cloth_sims,
    VIEW3D_PT_Object_Constraints,
    VIEW3D_PT_Misc,
    VIEW3D_OT_toggle_overlays
)




def register():
    Render_GPU_btn.register()
    Render_Optimize_Cycles.register()
    Constraint_Track.register()
    Constraint_Track_Remove.register()
    Data_Purge_Unused.register()
    External_Data_Pack.register()
    External_Data_Relative.register()
    Material_Rainbow_BSDF.register()
    Material_Rainbow_Color_Ramp.register()
    Output_Exr_Btn.register()
    Output_Mp4_Btn.register()
    Phyx_Active_Rigid.register()
    Phyx_Clear_Rigid.register()
    Phyx_Cloth_Collision.register()
    Phyx_Cloth_Sim.register()
    Phyx_Cloth_Sim_Clear.register()
    Phyx_Cloth_Collision_Clear.register()
    Phyx_Passive_Rigid.register()
    Render_Resolution_1080p.register()
    Render_Resolution_1440p.register()
    World_SkyTex_Btn.register()
    for cls in classes:
        bpy.utils.register_class(cls)
    
    
    
def unregister():
    Render_GPU_btn.unregister()
    Render_Optimize_Cycles.unregister()
    Constraint_Track.unregister()
    Constraint_Track_Remove.unregister()
    Data_Purge_Unused.unregister()
    External_Data_Pack.unregister()
    External_Data_Relative.unregister()
    Material_Rainbow_BSDF.unregister()
    Material_Rainbow_Color_Ramp.unregister()
    Output_Exr_Btn.unregister()
    Output_Mp4_Btn.unregister()
    Phyx_Active_Rigid.unregister()
    Phyx_Clear_Rigid.unregister()
    Phyx_Cloth_Collision.unregister()
    Phyx_Cloth_Sim.unregister()
    Phyx_Cloth_Sim_Clear.unregister()
    Phyx_Cloth_Collision_Clear.unregister()
    Phyx_Passive_Rigid.unregister()
    Render_Resolution_1080p.unregister()
    Render_Resolution_1440p.unregister()
    World_SkyTex_Btn.unregister()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    