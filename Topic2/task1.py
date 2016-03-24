lkey=['a','b','c','d']
lval=[1,2,3,4,5]

def fdict(lkey,lval):
    if len(lkey)>len(lval):
        while len(lkey)>len(lval):
            lval.append(None)
    else:
        lval=lval[0:len(lkey)]
    return {key:value for key,value in zip(lkey, lval).sort()}

print (fdict(lkey,lval))
