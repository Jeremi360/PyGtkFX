import os
import importlib
imports = os.listdir(os.path.join('.'))
print(imports)
for i in imports:
    n = i.split('.')[0]
    p = "grabbo." + n
    importlib.import_module(n.capitalize(), p)



