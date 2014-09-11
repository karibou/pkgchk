#!/usr/bin/python

import os
import sys

import apt


def get_info(pkg):
    cache = apt.Cache()
#    pkg="udev"
    if pkg in cache:
        print("%s:" % pkg)
        if cache[pkg].is_installed:
            print("  Installed : {}".format(cache[pkg].installed.version))
            print("  Candidate : {}".format(cache[pkg].candidate.version))
        else:
            print("  Installed : (none)")
            print("  Candidate : {}".format(cache[pkg].candidate.version))
    print("  Revision Table :")
    print("      {}".format(cache[pkg].candidate.version))
    for origin in cache[pkg].candidate.origins:
        print("          {} http://{}/ubuntu/ {}/{} {}".format(
                            cache[pkg].candidate.policy_priority,
                            origin.site,
                            origin.codename,
                            origin.component,
                            cache[pkg].candidate.architecture
                        ))

if __name__ == "__main__":
    get_info("udev")
