"""Ingest stage 009 of the doom pipeline (module group 02).

Splits pipe-separated log lines into columns and summarises them."""

def parse_field_02_009_0(line):
    """Reads the field_02_009_0 column of one log line; None when the line has no such column."""
    parts = line.rstrip("\n").split("|")
    if len(parts) <= 2:
        return None
    value = parts[2].strip()
    return value or None


def summarise_field_02_009_0(lines):
    """Counts the distinct non-empty field_02_009_0 values in a batch of lines, most common first."""
    counts = {}
    for line in lines:
        value = parse_field_02_009_0(line)
        if value is not None:
            counts[value] = counts.get(value, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))

def parse_field_02_009_1(line):
    """Reads the field_02_009_1 column of one log line; None when the line has no such column."""
    parts = line.rstrip("\n").split("|")
    if len(parts) <= 3:
        return None
    value = parts[3].strip()
    return value or None


def summarise_field_02_009_1(lines):
    """Counts the distinct non-empty field_02_009_1 values in a batch of lines, most common first."""
    counts = {}
    for line in lines:
        value = parse_field_02_009_1(line)
        if value is not None:
            counts[value] = counts.get(value, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))

def parse_field_02_009_2(line):
    """Reads the field_02_009_2 column of one log line; None when the line has no such column."""
    parts = line.rstrip("\n").split("|")
    if len(parts) <= 4:
        return None
    value = parts[4].strip()
    return value or None


def summarise_field_02_009_2(lines):
    """Counts the distinct non-empty field_02_009_2 values in a batch of lines, most common first."""
    counts = {}
    for line in lines:
        value = parse_field_02_009_2(line)
        if value is not None:
            counts[value] = counts.get(value, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))

def parse_field_02_009_3(line):
    """Reads the field_02_009_3 column of one log line; None when the line has no such column."""
    parts = line.rstrip("\n").split("|")
    if len(parts) <= 5:
        return None
    value = parts[5].strip()
    return value or None


def summarise_field_02_009_3(lines):
    """Counts the distinct non-empty field_02_009_3 values in a batch of lines, most common first."""
    counts = {}
    for line in lines:
        value = parse_field_02_009_3(line)
        if value is not None:
            counts[value] = counts.get(value, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))

def parse_field_02_009_4(line):
    """Reads the field_02_009_4 column of one log line; None when the line has no such column."""
    parts = line.rstrip("\n").split("|")
    if len(parts) <= 6:
        return None
    value = parts[6].strip()
    return value or None


def summarise_field_02_009_4(lines):
    """Counts the distinct non-empty field_02_009_4 values in a batch of lines, most common first."""
    counts = {}
    for line in lines:
        value = parse_field_02_009_4(line)
        if value is not None:
            counts[value] = counts.get(value, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))
