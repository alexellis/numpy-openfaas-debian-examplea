import numpy as np

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    a = np.arange(15).reshape(3, 5)

    return str(a)
