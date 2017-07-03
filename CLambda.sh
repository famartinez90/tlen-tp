#!/usr/bin/env python
import sys
from analyzer import parse

exp_str = sys.argv[1]
print parse(str(exp_str))
