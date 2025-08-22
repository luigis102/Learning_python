names = ["black","brown","red","orange","yellow","green","blue","violet","grey","white",]
def value(colors):
    if len(colors) > 2:
        colors = colors[:2]
    resist = [f"{names.index(i)}" for i in colors]
    return  int("".join(resist))
