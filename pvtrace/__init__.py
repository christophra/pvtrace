# pvtrace is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# pvtrace is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import division
import numpy as np
from external import transformations
from external import pov
from external import quickhull
from external import mathutils

print "pvtrace pre-flight checks..."
from Materials import *
from Devices import *
from Geometry import *
from ConstructiveGeometry import *
from LightSources import *
from Visualise import *
from Trace import *
from Interpolation import *

import os
import sys
# Module constants -- location of the data folder
found_pvtdata = False
for path in sys.path:
    if path.find('pvtrace') != -1:
        pvtrace_directory = path
        PVTDATA = os.path.join(pvtrace_directory, 'data')
        if os.path.exists(PVTDATA):
            found_pvtdata =  True
            break
if  found_pvtdata:
    print "pvtrace data directory:", PVTDATA
else:
    sys.exit("Did not find PVTDATA directory")
