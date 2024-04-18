# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""astropy の既存クラスの一部を拡張して、便利な関数を定義する."""
import numpy as np
from astropy import units as u
from astropy.units.format import core, utils


def def_exponential_as_unit(n):
    return u.def_unit(f'10^{{{n}}}', 10**n * u.one, format={"LaTeX": f'10^{{{n}}}'})

class LatexInlineNoFrac(u.format.Latex):
    """
    Output LaTeX to display the unit based on IAU style guidelines with negative
    powers.

    Attempts to follow the `IAU Style Manual
    <https://www.iau.org/static/publications/stylemanual1989.pdf>`_ and the
    `ApJ and AJ style guide
    <https://journals.aas.org/manuscript-preparation/>`_.
    """

    name = "latex_inline_no_flac"

    @classmethod
    def to_string(cls, unit, fraction="inline"):
        return super().to_string(unit, fraction=fraction)
