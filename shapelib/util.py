##################################
#
# helpers
#
###################################

def window(iterable, size, step):
    """
    iterate over subseqs of iterable
    
    Example
    =======
    
    >>> seq = range(6)
    
    >>> list(window(seq, 3, 1))
    [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5)]
    
    >>> list(window(seq, 3, 2))
    [(0, 1, 2), (2, 3, 4)]
    """
    iterators = _itertools.tee(iterable, size)
    for skip_steps, itr in enumerate(iterators):
        for ignored in _itertools.islice(itr, skip_steps):
            pass
    window_itr = _itertools.izip(*iterators)
    if step != 1:
        window_itr = _itertools.islice(window_itr, 0, 99999999, step)
    return window_itr