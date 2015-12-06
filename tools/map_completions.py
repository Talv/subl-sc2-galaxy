import sys
import json
from nectan import ast
from nectan import parser
from nectan import symtable

p = parser.Parser()
fAst = p.parseFile(sys.argv[1])
smTable = symtable.Symbol(fAst)
symtable.mapSymbols(fAst, smTable)

completions = []

for key in smTable.entries:
    sm = smTable.entries[key]
    if isinstance(sm.node, ast.FunctionDefinition):
        contents = sm.node.name + "("
        for i, x in enumerate(sm.node.arguments):
            if not i == 0:
                contents += ", "
            contents += "${%d:%s %s}" % (i + 1, x.type.name, x.name)
        contents += ")"
    elif isinstance(sm.node, ast.VariableDeclaration):
        contents = sm.node.name
    else:
        continue
    completions.append({
        "trigger": sm.node.name,
        "contents": contents
    })

print(json.dumps(
    {
        "scope": "meta.block.galaxy",
        "completions": completions
    },
    indent=4,
    sort_keys=False
))
