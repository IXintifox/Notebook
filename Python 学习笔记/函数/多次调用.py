#多次调用结果

def function( ob = [] ):
    print(ob)
    ob.append(1)

function()
function()

#>>>>> []  [1]

#改进：
def function_c( nb = None ):
    if nb == None:
        nb = []
    print(nb)
    nb.append(1)

function_c()
function_c()

#>>>>> []  []

