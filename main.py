from __future__ import print_function
import io
import re
import collections
from apt.pyy import Package

pkg_dict = dict()
pack = u'Package'
depends = u'Depends'

with io.open('Packages', encoding='utf-8') as file:

    for line in file:

        if pack in line:
            line = re.sub(r'\w+\,', '', line)
            pgk = Package(line)

            if pkg_dict.keys() is None:
                pkg_dict[0] = pgk

            else:
                last = collections.deque(pkg_dict, maxlen=1)
                pkg_dict[last+1] = pgk

        if depends in line:
            line = re.sub(r'\w+\,', '', line)

            for word in line:

                if word[0].isupper() is True:
                    break
                pgk.depends_list.append(word)


