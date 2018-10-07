
import bpy
from bpy.types import Menu

# spawn a selection of tools for speeding up VSE workflow


#Select all strips to the left
class SelectAllToTheLeft(bpy.types.Operator):
    bl_idname = "sequencer.allleft"
    bl_label = "All strips to the left"
    
    def execute(self, context) : 
        bpy.ops.sequencer.select(left_right='LEFT', linked_time=True)
        return {'FINISHED'}
    

    
#Select all strips to the right
class SelectAllToTheRight(bpy.types.Operator):
    bl_idname = "sequencer.allright"
    bl_label = "All strips to the right"
    
    def execute(self, context) : 
        bpy.ops.sequencer.select(left_right='RIGHT', linked_time=True)
        return {'FINISHED'}

#Set current override camera as active camera in the viewport
class OverrideToActiveCamera(bpy.types.Operator):
    bl_idname = "sequencer.overrideactivecamera"
    bl_label = "Overide Camera to active"
    
    def execute(self, context) :
        print("coucou")
        return {"FINISHED"}


class VSE_PIE_riton(Menu):
    bl_idname = "pie.vsetools"
    bl_label = "VSE Tool"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()

        #pie.operator("sequencer.allleft", text = "All strips to the left", icon="BACK")
        #pie.operator("sequencer.allright", text = "All strips to the right", icon="FORWARD")
        pie.operator("sequencer.reload", text = "Reload strips",icon="FILE_REFRESH")
        pie.operator("sequencer.overrideactivecamera", text = "Override to Active Camera", icon = "SCENE")
        pie.operator("sequencer.cut", text="Cut (Hard) at frame").type = 'HARD'
        pie.operator("sequencer.cut", text="Cut (Soft) at frame").type='SOFT'
        pie.operator("sequencer.gap_remove").all = False
        pie.operator("sequencer.gap_insert")
        #pie.separator()
        '''
        props = layout.operator("sequencer.strip_jump", text="Jump to Previous Strip")
        props.next = False
        props.center = False
        props = layout.operator("sequencer.strip_jump", text="Jump to Next Strip")
        props.next = True
        props.center = False   
        '''         
        #pie.separator()            
        pie.operator("transform.transform", text="Grab/Move").mode = 'TRANSLATION'
        pie.operator("transform.transform", text="Grab/Extend from Frame").mode = 'TIME_EXTEND'
        pie.operator("sequencer.slip", text="Slip Strip Contents")        

def register():
    #tools
    bpy.utils.register_class(SelectAllToTheLeft)
    bpy.utils.register_class(SelectAllToTheRight)
    bpy.utils.register_class(OverrideToActiveCamera)
    
    #pie
    bpy.utils.register_class(VSE_PIE_riton)
    
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name="Sequencer",
             space_type='SEQUENCE_EDITOR')
    kmi = km.keymap_items.new("wm.call_menu_pie", 
            type="W", 
            value="PRESS")
    kmi.properties.name = "pie.vsetools"


def unregister():
    #tools
    bpy.utils.unregister_class(SelectAllToTheLeft)
    bpy.utils.unregister_class(SelectAllToTheRight)
    bpy.utils.unregister_class(OverrideToActiveCamera)
    
    #pie
    bpy.utils.unregister_class(VSE_PIE_riton)


if __name__ == "__main__":
    register()

