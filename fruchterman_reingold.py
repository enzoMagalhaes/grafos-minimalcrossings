import numpy as np

def fruchterman_reingold(
    A, l=None, pos=None, iterations=100, threshold=1e-4, dim=2, seed=None
):

    V_SIZE, _ = A.shape

    if pos is None:
        pos = np.asarray(seed.rand(V_SIZE, dim), dtype=A.dtype)
    else:
        pos = pos.astype(A.dtype)

    if l is None:
        l = np.sqrt(1.0 / V_SIZE)


    epsilon = max(max(pos.T[0]) - min(pos.T[0]), max(pos.T[1]) - min(pos.T[1])) * 0.1

    dt = epsilon / (iterations + 1)
    euclidean_delta = np.zeros((pos.shape[0], pos.shape[0], pos.shape[1]), dtype=A.dtype)

    for it in range(iterations):
        euclidean_delta = pos[:, np.newaxis, :] - pos[np.newaxis, :, :]
        distance = np.linalg.norm(euclidean_delta, axis=-1)
        
        np.clip(distance, 0.01, None, out=distance)
        forces_summation = np.einsum(
            "ijk,ij->ik", euclidean_delta, (l * l / distance**2 - A * distance / l)
        )

        length = np.linalg.norm(forces_summation, axis=-1)
        length = np.where(length < 0.01, 0.1, length)
        delta_pos = np.einsum("ij,i->ij", forces_summation, epsilon / length)
        pos += delta_pos

        epsilon -= dt
        if (np.linalg.norm(delta_pos) / V_SIZE) < threshold:
            break
    return pos