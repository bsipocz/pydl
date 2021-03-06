# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
def fchebyshev(x,m):
    """Compute the first `m` Chebyshev polynomials.

    Parameters
    ----------
    x : array-like
        Compute the Chebyshev polynomials at these abscissa values.
    m : :class:`int`
        The number of Chebyshev polynomials to compute.  For example, if
        :math:`m = 3`, :math:`T_0 (x)`, :math:`T_1 (x)` and :math:`T_2 (x)` will be computed.

    Returns
    -------
    fchebyshev : :class:`numpy.ndarray`
    """
    import numpy as np
    from scipy.special import chebyt
    if isinstance(x,np.ndarray):
        n = x.size
    else:
        n = 1
    if m < 1:
        raise ValueError('Order of Chebyshev polynomial must be at least 1.')
    try:
        dt = x.dtype
    except AttributeError:
        dt = np.float64
    leg = np.ones((m,n),dtype=dt)
    if m >= 2:
        leg[1,:] = x
    if m >= 3:
        for k in range(2,m):
            leg[k,:] = np.polyval(chebyt(k),x)
    return leg
