import subprocess


def run_cmd(cmd):
    """Run a command and get back the output
    """
    ret = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE
    ).communicate()
    return ret[0][:-1]
