#!/usr/bin/python

import os
import sys

import apt

def is_available(dist):
    etcdir = os.path.join(dist, "etc", "apt")
    if not os.path.exists(etcdir):
        os.makedirs(etcdir)
    with open(os.path.join(etcdir, "sources.list"), "w") as f:
        for pocket in ["", "-updates", "-security", "-proposed"]:
            f.write("deb http://archive.ubuntu.com/ubuntu %s%s main restricted universe multiverse\n" % (dist, pocket))
    cache = apt.Cache(rootdir="./%s" % dist)
    cache.update()
    for line in sys.stdin.readlines():
        if not line:
            continue
        want_pkg, want_ver = line.split()
        if not want_pkg in cache:
            print("%s missing")
            return False
        if want_ver in cache[want_pkg].versions:
            break
        else:
            print("%s not available for %s" % (want_ver, want_pkg))
            return False
    return True


if __name__ == "__main__":
        res = is_available("trusty")
        if res is True:
            print("all good")
