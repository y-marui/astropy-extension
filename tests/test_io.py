from astropy_extension.io import get_units
import astropy.units as u

assert get_units(["", "m", "s"]) == [None, u.m, u.s]
