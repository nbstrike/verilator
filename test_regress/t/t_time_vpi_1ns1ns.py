#!/usr/bin/env python3
# DESCRIPTION: Verilator: Verilog Test driver/expect definition
#
# Copyright 2024 by Wilson Snyder. This program is free software; you
# can redistribute it and/or modify it under the terms of either the GNU
# Lesser General Public License Version 3 or the Perl Artistic License
# Version 2.0.
# SPDX-License-Identifier: LGPL-3.0-only OR Artistic-2.0

import vltest_bootstrap

test.scenarios('simulator_st')
test.pli_filename = "t/t_time_vpi_c.cpp"
test.top_filename = "t/t_time_vpi.v"
test.main_time_multiplier = 1e-9 / 1e-9

test.compile(
    v_flags2=['+define+time_scale_units=1ns +define+time_scale_prec=1ns', test.pli_filename],
    verilator_flags2=['--vpi --trace-vcd'])

test.execute(expect_filename=test.golden_filename)

test.file_grep(test.trace_filename, r'timescale +1ns')

test.passes()
