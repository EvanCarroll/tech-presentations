import ast

content = open("test.py").read()
#print ast.dump( ast.parse(content) )

import astpretty

astpretty.pprint( ast.parse(content) )

