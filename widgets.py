from ipywidgets import interact, interactive, fixed
import ipywidgets

@interact(x=True,y=1.0)
def g(x,y):
    return (x,y)


