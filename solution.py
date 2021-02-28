def to_bytes(value, unit):
    if unit == 'KB':
        return 1024 * value
    if unit == 'MB':
        return 1024 * 1024 * value
    if unit == 'GB':
        return 1024 * 1024 * 1024 * value
    return value


def in_largest_units(bytes):
    if bytes < 1024:
        return f'{bytes} B'
    kbytes = bytes / 1024
    if kbytes < 1024:
        return f'{int(kbytes + 0.5)} KB'
    mbytes = kbytes / 1024
    if mbytes < 1024:
        return f'{int(mbytes + 0.5)} MB'
    gbytes = mbytes / 1024
    return f'{int(gbytes + 0.5)} GB'
