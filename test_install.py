import os
import sys

SPECIAL_VERSIONS = ["2.6", "3.2", "3.3"]
VERSION = "%s.%s" % sys.version_info[:2]


def test_install_remote():
    cmd = "curl https://bootstrap.pypa.io/"

    if VERSION in SPECIAL_VERSIONS:
        cmd += "%s/" % VERSION

    cmd += "get-pip.py | python"
    print(cmd)
    ret = os.system(cmd)

    exit_status = ret >> 8
    assert exit_status == 0


def test_install_local():
    cmd = "python "

    if VERSION in SPECIAL_VERSIONS:
        cmd += "%s/" % VERSION

    cmd += "get-pip.py"
    print(cmd)
    ret = os.system(cmd)

    exit_status = ret >> 8
    assert exit_status == 0


if os.getenv("SRCIPT_SRC") == "remote":
    test_install_remote()
else:
    test_install_local()
