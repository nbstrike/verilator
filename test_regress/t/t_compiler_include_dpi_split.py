#!/usr/bin/env python3
# DESCRIPTION: Verilator: Verilog Test driver/expect definition
#
# Copyright 2024 by Wilson Snyder. This program is free software; you
# can redistribute it and/or modify it under the terms of either the GNU
# Lesser General Public License Version 3 or the Perl Artistic License
# Version 2.0.
# SPDX-License-Identifier: LGPL-3.0-only OR Artistic-2.0

import vltest_bootstrap

test.scenarios('vlt')
test.top_filename = "t/t_compiler_include_dpi.v"

test.compile(v_flags2=["t/t_compiler_include_dpi.cpp"],
             verilator_flags2=[
                 "-Wall -Wno-DECLFILENAME --compiler-include",
                 test.t_dir + "/t_compiler_include_dpi.h", "--output-split 1"
             ])

test.execute()

test.passes()
