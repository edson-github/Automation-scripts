"""Module to combine all faces."""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-


class Combine:
    """Combine class."""

    def sides(self, sides):
        """Join all the sides together into one single string.

        :param sides: dictionary with all the sides
        :returns: string
        """
        return ''.join(''.join(sides[face]) for face in 'URFDLB')


combine = Combine()
