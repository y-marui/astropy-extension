# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""astropy の既存クラスの一部を拡張して、便利な関数を定義する."""
import numpy as np
from astropy import units as u
from astropy.units.format import core, utils


class LatexInline_Extention(u.format.LatexInline):
    """LatexInline_Extention."""

    @classmethod
    def format_exponential_notation(cls, val, format_spec="0.1e"):
        """Format a value in exponential notation for LaTeX.

        Parameters
        ----------
        val: number
            The value to be formatted
        format_spec: str, optional
            Format used to split up mantissa and exponent

        Returns
        -------
        latex_string: str
            The value in exponential notation in a format suitable for LaTeX.
        """
        if np.isfinite(val):
            m, ex = utils.split_mantissa_exponent(val, format_spec)

            parts = []
            if m == "1":
                pass
            elif m:
                parts.append(m)
            if ex:
                parts.append("10^{{{0}}}".format(ex))

            return r" \times ".join(parts)
        else:
            if np.isnan(val):
                return r'{\rm NaN}'
            elif val > 0:
                # positive infinity
                return r'\infty'
            else:
                # negative infinity
                return r'-\infty'


class Latex_Extention(u.format.Latex):
    """Latex_Extention."""

    @classmethod
    def format_exponential_notation(cls, val, format_spec="0.1e"):
        """Format a value in exponential notation for LaTeX.

        Parameters
        ----------
        val: number
            The value to be formatted
        format_spec: str, optional
            Format used to split up mantissa and exponent

        Returns
        -------
        latex_string: str
            The value in exponential notation in a format suitable for LaTeX.
        """
        if np.isfinite(val):
            m, ex = utils.split_mantissa_exponent(val, format_spec)

            parts = []
            if m == "1":
                pass
            elif m:
                parts.append(m)
            if ex:
                parts.append("10^{{{0}}}".format(ex))

            return r" \times ".join(parts)
        else:
            if np.isnan(val):
                return r'{\rm NaN}'
            elif val > 0:
                # positive infinity
                return r'\infty'
            else:
                # negative infinity
                return r'-\infty'


class Latex_Extention_no_flac(Latex_Extention):
    """Latex_Extention_no_flac."""

    @classmethod
    def to_string(cls, unit):
        latex_name = None
        if hasattr(unit, '_format'):
            latex_name = unit._format.get('latex')

        if latex_name is not None:
            s = latex_name
        elif isinstance(unit, core.CompositeUnit):
            if unit.scale == 1:
                s = ''
            else:
                s = cls.format_exponential_notation(unit.scale) + r'\,'

            if len(unit.bases):
                s += cls._format_bases(unit, previous=s)

        elif isinstance(unit, core.NamedUnit):
            s = cls._latex_escape(unit.name)

        return fr'$\mathrm{{{s}}}$'

    @classmethod
    def _format_bases(cls, unit, previous=""):
        positives, negatives = utils.get_grouped_by_powers(
            unit.bases, unit.powers)

        if len(negatives):
            if len(positives):
                positives = cls._format_unit_list(positives)
            else:
                if previous == "":
                    positives = '1'
                else:
                    positives = ''
            negatives = cls._format_unit_list(negatives)
            s = r'{}/{}'.format(positives, negatives)
        else:
            positives = cls._format_unit_list(positives)
            s = positives

        return s
