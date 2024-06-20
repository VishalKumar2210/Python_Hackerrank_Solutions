digits = '(V?[I]{0,3}|I[VX])'
tens = '(L?[X]{0,3}|X[LC])'
hundreds = '(D?[C]{0,3}|C[DM])'
thousands = 'M{0,3}'
regex_pattern = thousands + hundreds + tens + digits +'$'

import re
print(str(bool(re.match(regex_pattern, input()))))