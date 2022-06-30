# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Blender Workspace Pie",
    "author" : "Azfar Danish",
    "description" : "Blender Workspace Pie",
    "blender" : (2, 90, 0),
    "version" : (1, 1, 6),
    "location" : "Pie Menu",
    "warning" : "",
    "category" : "Interface",
}


import bpy
from bpy.utils import register_class, unregister_class
from bpy.props import PointerProperty


from . ui.preferences import *
from . ui.workspace_mt import *

from . operators.workspace_op import *

from . prop.properties import *

##########   CLASSES

addon_classes = (
    Workspace_MT_Menu,
    Workspace_OT_Operator,
    AddonPreferences,
    Properties,
)

##########   REGISTER & UNREGISTER

def register():
    register_keymap()

    for ac in addon_classes:
        register_class(ac)

    bpy.types.Scene.properties = PointerProperty(type=Properties)


def unregister():
    unregister_keymap()

    for ac in addon_classes:
        unregister_class(ac)

    del bpy.types.Scene.properties


if __name__ == "__main__":
    register()
