from numpy import isnan

def trim_nans(filt, trim='fb'):
    """
    Trim leading and/or trailing numpy.nan values from a numpy.array.
    Forked from Numpy's numpy.trim_zeros.
    """
    first = 0
    trim = trim.upper()
    if 'F' in trim:
        for i in filt:
            if ~isnan(i):
                break
            else:
                first = first + 1

    last = len(filt)
    if 'B' in trim:
        for i in filt[::-1]:
            if ~isnan(i):
                break
            else:
                last = last - 1
    return filt[first:last]
