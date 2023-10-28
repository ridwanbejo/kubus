import subprocess  # nosec
import shlex


def get_file_permission(control_item):
    file_permission = subprocess.check_output(
        ["stat", "-c", "%a", shlex.quote(control_item)], text=True
    )  # nosec

    return file_permission


def get_file_owner_group(control_item):
    file_owner_group = subprocess.check_output(
        ["stat", "-c", "%U:%G", shlex.quote(control_item)], text=True
    )  # nosec

    return file_owner_group


def get_dir_permission(control_item):
    dir_permission = subprocess.check_output(
        "ls -laR " + shlex.quote(control_item), shell=True
    )  # nosec
    dir_permission = dir_permission.decode().split("\n")
    dir_permission = [x for x in dir_permission if x != ""]

    return dir_permission


def get_dir_owner_group(control_item):
    dir_owner_group = subprocess.check_output(
        ["ls", "-laR", shlex.quote(control_item)], text=True
    )  # nosec
    dir_owner_group = dir_owner_group.split("\n")
    dir_owner_group = [x for x in dir_owner_group if "dr" in x] + [
        x for x in dir_owner_group if "-r" in x
    ]

    return dir_owner_group


def get_running_process(control_item):
    processes = subprocess.check_output(
        "ps -ef | grep {0}".format(shlex.quote(control_item)), shell=True
    ).decode()  # nosec
    processes = processes.split("\n")
    processes = [x for x in processes if control_item in x]

    return "".join(processes)
