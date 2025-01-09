import pylightxl as xl
from astropy.table import QTable
import astropy.units as u


def get_units(units):
    if isinstance(units, list):
        return [_get_unit(unit) for unit in units]
    else:
        return _get_unit(units[0])


def _get_unit(unit):
    if unit == "":
        return None
    else:
        v = u.Unit(unit)
        if v.is_equivalent(1):
            return 1 * v
        else:
            return v


def read_excel_sheet(
    ws: xl.pylightxl.Worksheet, has_unit: bool = False, remove_sharp: bool = False
) -> QTable:
    if remove_sharp:
        _table = read_excel_sheet(ws, has_unit=has_unit)
        _colnames = [c for c in _table.colnames if not c.startswith("#")]
        return _table[_colnames]
    else:
        if has_unit:
            _dataset = ws.range(address=f"A3:{chr(64+ws.maxcol)}{ws.maxrow}")
            (_colnames,) = ws.range(address=f"A1:{chr(64+ws.maxcol)}1")
            (_units,) = ws.range(address=f"A2:{chr(64+ws.maxcol)}2")
            return QTable(
                dict(zip(_colnames, list(zip(*_dataset)))), units=get_units(_units)
            )

        else:
            _dataset = ws.range(address=f"A2:{chr(64+ws.maxcol)}{ws.maxrow}")
            (_colnames,) = ws.range(address=f"A1:{chr(64+ws.maxcol)}1")
            return QTable(dict(zip(_colnames, list(zip(*_dataset)))))
