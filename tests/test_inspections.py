# -*- coding: utf-8 -*-

"""
jishaku.inspections test
~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2021 Devon (Gorialis) R
:license: MIT, see LICENSE for more details.

"""

import collections  # for __iadd__ test

import nextcord
import pytest
from jishaku.repl.inspections import all_inspections
from utils import run_async


@pytest.mark.parametrize(
    "target",
    [
        4,
        nextcord.Client,  # cover type subclasses
        tuple,  # cover many-subclass truncation
        [False, 1, "2", 3.0],  # cover content types
        collections.Counter,  # cover inplace operators
        run_async,  # cover current-working-directory inspections
    ],
)
def test_object_inspection(target):
    for _, _ in all_inspections(target):
        pass
