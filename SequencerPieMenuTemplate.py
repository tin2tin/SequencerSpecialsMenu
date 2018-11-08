
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
 
bl_info = {
    "name": "VSE Pie-Menu",
    "author": "tintwotin",
    "version": (0,1),
    "blender": (2, 79, 0),
    "location": "Sequencer > Shortcut key: 'W'",
    "description": "Pie Menu for the Sequencer",
    "category": "Sequencer"}

import bpy
from bpy.types import Menu


class VSE_PIE_menu(Menu):
    bl_idname = "pie.vsetools"
    bl_label = "VSE Pie Menu"

    def draw(self, context):
        layout = self.layout

        layout = layout.menu_pie()
        layout.operator("transform.transform", text="Grab/Extend from Frame").mode = 'TIME_EXTEND'
        layout.operator("sequencer.slip", text="Slip Strip Contents")
 
        #hardcut=layout.operator("sequencer.cut", text="Cut (Hard) at frame")
        #hardcut.type = 'HARD'
        #hardcut.frame=bpy.context.scene.frame_current
        layout.operator("sequencer.delete")

        softcut=layout.operator("sequencer.cut", text="Cut (Soft) at frame")
        softcut.type = 'SOFT'
        softcut.frame=bpy.context.scene.frame_current 
        
        props = layout.operator("sequencer.strip_jump", text="Jump to Previous Strip")#, icon="BACK")
        props.next = False
        props.center = False
        props = layout.operator("sequencer.strip_jump", text="Jump to Next Strip")#, icon="FORWARD")
        props.next = True
        props.center = False        
                    
        #layout.operator("transform.transform", text="Grab/Move").mode = 'TRANSLATION'
        #layout.operator("sequencer.copy")
        #layout.operator("sequencer.paste")
        layout.operator("sequencer.gap_remove").all = False
        layout.operator("sequencer.gap_insert")

def register():
    
    #pie
    bpy.utils.register_class(VSE_PIE_menu)
    
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name="Sequencer",
             space_type='SEQUENCE_EDITOR')
    kmi = km.keymap_items.new("wm.call_menu_pie", 
            type="W", 
            value="PRESS")
    kmi.properties.name = "pie.vsetools"


def unregister():
    
    #pie
    bpy.utils.unregister_class(VSE_PIE_menu)


if __name__ == "__main__":
    register()
