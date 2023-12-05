#!/usr/bin/python3
"""Solves the lock abox puzzle """


def my_opener(openbox):
    """Looks for the next opened box
    Args:
        openbox (dict): Dictionary which contains abox already opened
    Returns:
        list: List with the keys contained in the opened box
    """
    for index, box in openbox.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(abox):
    """Check if all abox can be opened
    Args:
        abox (list): List which contain all the abox with the keys
    Returns:
        bool: True if all abox can be opened, otherwise, False
    """
    if len(abox) <= 1 or abox == [[]]:
        return True

    xas = {}
    while True:
        if len(xas) == 0:
            xas[0] = {
                'status': 'opened',
                'keys': abox[0],
            }
        keys = my_opener(xas)
        if keys:
            for key in keys:
                try:
                    if xas.get(key) and xas.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    xas[key] = {
                        'status': 'opened',
                        'keys': abox[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in xas.values()]:
            continue
        elif len(xas) == len(abox):
            break
        else:
            return False

    return len(xas) == len(abox)


def main():
    """Entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
