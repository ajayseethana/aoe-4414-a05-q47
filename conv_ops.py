# script_name.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Ajay Seethana
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import math # math module
import sys # argv

# constants
R_E_KM = 6378.137
E_E    = 0.081819221456

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
# arg1 = '' # description of argument 1
# arg2 = '' # description of argument 2
# parse script arguments
if len(sys.argv)==9:
  c_in = float(sys.argv[1])
  h_in = float(sys.argv[2])
  w_in = float(sys.argv[3])
  n_filt = float(sys.argv[4])
  h_filt = float(sys.argv[5])
  w_filt = float(sys.argv[6])
  s = float(sys.argv[7])
  p = float(sys.argv[8])
else:
  print(\
   'Usage: '\
   'python3 arg1 arg2 ...'\
  )
  exit()

# write script below this line

c_out = c_in
h_out = (h_in + 2*p - h_filt)/s + 1
w_out = (w_in + 2*p - w_filt)/s + 1

adds = n_filt*h_out*w_out*c_in*h_filt*w_filt
muls = n_filt*h_out*w_out*c_in*h_filt*w_filt
divs = 0


print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed
