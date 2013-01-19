# Beuarg - an OpenERP code puker
# Copyright (C) 2013 Laurent Peuch <cortex@worlddomination.be>
#                    Railnova SPRL <railnova@railnova.eu>
#
# This file is part of Beuarg.
#
# Beuarg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# Beuarg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Beuarg.  If not, see <http://www.gnu.org/licenses/>.

import _ast
import ast

class ClassFinder(ast.NodeVisitor):
    def __init__(self):
        self.models = {}

    def is_oerp_mode(self, class_node):
        for i in class_node.bases:
            if isinstance(i, _ast.Name) and i.id == "osv":
                return True
            if isinstance(i, _ast.Attribute) and i.attr == "osv" and i.value.id == "osv":
                return True

        return False

    def visit_ClassDef(self, class_node):
        if not self.is_oerp_mode(class_node):
            return
        self.models[class_node.name] = {"class_name": class_node.name}
        KeyAttributesFinder(self.models[class_node.name]).visit(class_node)

class KeyAttributesFinder(ast.NodeVisitor):
    def __init__(self, model):
        self.model = model

    def visit_Assign(self, assign_node):
        if assign_node.targets[0].id in ("_name", "_inherit"):
            self.model[assign_node.targets[0].id] = assign_node.value.s
        if assign_node.targets[0].id == "_columns":
            self.model[assign_node.targets[0].id] = map(lambda x: x.s, assign_node.value.keys)

    def visit_FunctionDef(self, _):
        pass

def get_classes(string):
    class_finder = ClassFinder()
    class_finder.visit(ast.parse(string))
    return class_finder.models
