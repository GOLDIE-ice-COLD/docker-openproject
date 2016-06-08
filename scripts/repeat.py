#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# :Project:   docker-openproject -- incoming email processor
# :Created:   mer 08 giu 2016 15:34:30 CEST
# :Author:    Alberto Berti <alberto@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2016 Alberto Berti

import os
import sys
import time


def main(delay, *command):
    while True:
        os.system(' '.join(command))
        time.sleep(delay)


if __name__ == '__main__':
    main(int(sys.argv[1]), *sys.argv[2:])
