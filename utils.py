def get_common_prefix(label, suffix):
    """Returns the longest common prefix between the label of an edge and the current suffix

    Args:
        label (string):
        suffix (string):
    """
    i = 0
    while i < min(len(label), len(suffix)) and label[i] == suffix[i]:
        i += 1
    return i, label[:i]
