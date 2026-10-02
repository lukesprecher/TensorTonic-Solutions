import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    
    
    if max_len is None:
        max = 0
        for seq in seqs:
            if len(seq) > max:
               max = len(seq)

        l = max

    else:
        l = max_len

    n = len(seqs)

    vals = np.full((n,l), pad_value, np.int64)



    for i, seq in enumerate(seqs):
        vals[i, :len(seq)] = seq[:l]

    return vals
    