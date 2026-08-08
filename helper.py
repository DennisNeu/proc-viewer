"""Utilities for reading system information from /proc."""

def kb_to_gib(kb):
    """calculate kilobytes into gibibyte"""
    return int(kb)/1024/1024