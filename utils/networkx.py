
import time
import numpy as np
import networkx as nx
from networkx.drawing.layout import _process_params,  rescale_layout
from networkx.utils import np_random_state

from fruchterman_reingold import fruchterman_reingold

"""
Wrapper following networkx API to preprocess input and run fruchterman_reingold
"""

@np_random_state(10)
def preprocess_input_and_run_fruchterman_reingold(
    G,
    l=None,
    pos=None,
    fixed=None,
    iterations=50,
    threshold=1e-4,
    weight="weight",
    scale=1,
    center=None,
    dim=2,
    seed=None,
):
    G, center = _process_params(G, center, dim)


    if pos is not None:
        dom_size = max(coord for pos_tup in pos.values() for coord in pos_tup)
        if dom_size == 0:
            dom_size = 1
        pos_arr = seed.rand(len(G), dim) * dom_size + center

        for i, n in enumerate(G):
            if n in pos:
                pos_arr[i] = np.asarray(pos[n])
    else:
        pos_arr = None
        dom_size = 1

    if len(G) == 0:
        return {}
    if len(G) == 1:
        return {nx.utils.arbitrary_element(G.nodes()): center}


    A = nx.to_numpy_array(G, weight=weight)

    start_time = time.time()
    pos = fruchterman_reingold(
        A, l, pos_arr, iterations, threshold, dim, seed
    )
    end_time = time.time()
    
    if scale is not None:
        pos = rescale_layout(pos, scale=scale) + center
    pos = dict(zip(G, pos))
    return pos, end_time - start_time