#!/usr/bin/env python

# https://stackoverflow.com/questions/39187886/what-is-the-difference-between-subprocess-popen-and-subprocess-run
#
# Не использовать run. run для запустить и ждать, обёртка для popen
#

from subprocess import run, PIPE
run('/bin/lsblk -o name -n -s -l'.split(), stdout=PIPE)

# По возможности рекомендуется избегать оболочки при выполнении подпроцессов.
# Оболочка представляет набор потенциальных уязвимостей безопасности
# - например, махинации с переменной среды PATH. Лучше всего запускать команду
# с определенным исполняемым файлом и предварительно проанализированными
# параметрами командной строки
# На самом деле я бы вообще не стал анализировать вывод lsblk.
# В конце концов, lsblk - это всего лишь способ сообщить о содержимом файловой
# системы sysfs. Лучше проверить /sys напрямую
################################################################################

from glob import glob
from os.path import basename, dirname

def physical_drives():
    drive_glob = "/sys/block/*/device"
    return [basename(dirname(d)) for d in glob(drive_glob)]


def partitions(disk):
    if disk.startswith(".") or "/" in disk:
        raise ValueError("Invalid disk name {0}".format(disk))
    partition_glob = "/sys/block/{0}/*/start".format(disk)
    return [basename(dirname(p)) for p in glob(partition_glob)]