# RSA error printout, written by MatheusArtur

# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import platform
import sys
def usage():
    OPTIONS= r"""
    USAGE:

        rsa [COMMAND] [ARGUMENTS] [FILES]
        rsa [COMMAND] |...| [FILES]

        examples:

        rsa encrypt 3 7 my_text.txt
        rsa decrypt my_text.csv

    """
    print(OPTIONS)

