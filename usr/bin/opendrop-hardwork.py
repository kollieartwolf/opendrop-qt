#!/usr/bin/env python
import subprocess as sb
import os


class ProcessHandler:
    def __init__(self, log_file_cons, args):
        self.__log_tag = log_file_cons
        self.__sb_args = args
        self.process = None
        self.log_stdout = None
        self.log_stderr = None

    def __prepare_files__(self):
        if not os.path.exists("/var/log/opendrop-qt"):
            os.mkdir("/var/log/opendrop-qt")
        self.log_stdout = open("/var/log/opendrop-qt/{}_out.log".format(self.__log_tag), "w")
        self.log_stderr = open("/var/log/opendrop-qt/{}_err.log".format(self.__log_tag), "w")

    def __posthandle_files__(self):
        self.log_stdout.close()
        self.log_stderr.close()

    def start(self):
        self.__prepare_files__()
        self.process = sb.Popen(self.__sb_args,
                                stdout=self.log_stdout,
                                stderr=self.log_stderr)

    def terminate(self):
        self.process.terminate()
        self.__posthandle_files__()
        return self.process.poll()


networkmanager_off_handler = ProcessHandler("nm_off", ["systemctl", "stop", "NetworkManager"])
owl_handler = ProcessHandler("owl", ["owl", "-i", "mon0", "-N"])
networkmanager_on_handler = ProcessHandler("nm_on", ["systemctl", "start", "NetworkManager"])


