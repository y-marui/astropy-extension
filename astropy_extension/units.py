"""Define additional units."""

import astropy.units as u

uohm_cm = u.def_unit("uohm_cm", u.uohm * u.cm, format={"latex": r"\mu\Omega\,cm"})
u.add_enabled_units([uohm_cm])

A_m2 = u.def_unit("A_m2",u.A * (u.m**-2),format={"latex": r"A\,m^{-2}"})
u.add_enabled_units([A_m2])
