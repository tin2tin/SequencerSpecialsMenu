# Add a 'Specials Menu' to Blender Video Editing Sequencer. Shortcut key: 'w'.
# By tintwotin

import bpy

class SequencerEditMenu(bpy.types.Menu):
    bl_label = "Specials"
    bl_idname = "SEQUENCER_OT_sequencer_edit_menu"

    def draw(self, context):

        print("space_date.type: "+context.space_data.type)      
        if context.space_data.type == 'SEQUENCE_EDITOR':

            layout = self.layout
            layout.operator("sequencer.gap_remove").all = False
            layout.operator("sequencer.gap_insert")
            layout.separator()
            props = layout.operator("sequencer.strip_jump", text="Jump to Previous Strip")
            props.next = False
            props.center = False
            props = layout.operator("sequencer.strip_jump", text="Jump to Next Strip")
            props.next = True
            props.center = False            
            layout.separator()            
            layout.operator("transform.transform", text="Grab/Move").mode = 'TRANSLATION'
            layout.operator("transform.transform", text="Grab/Extend from Frame").mode = 'TIME_EXTEND'
            layout.operator("sequencer.slip", text="Slip Strip Contents")            
            layout.separator()
            layout.operator("sequencer.cut", text="Cut (Hard) at frame").type = 'HARD'
            layout.operator("sequencer.cut", text="Cut (Soft) at frame").type='SOFT'         

addon_keymaps = []
def register():
    bpy.utils.register_class(SequencerEditMenu)

    # handle the keymap
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:    
        km = wm.keyconfigs.addon.keymaps.new(name='Sequencer', space_type='SEQUENCE_EDITOR')
        kmi = km.keymap_items.new('wm.call_menu', 'W', 'PRESS')
        kmi.properties.name = "SEQUENCER_OT_sequencer_edit_menu"    
        addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(SequencerEditMenu)

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
if __name__ == "__main__":
    register()
