from time import sleep
from fabric import Connection

class Driver:
    def __init__(self, hostname):
        self.connection = Connection(hostname)

    def run(self, command):
        sleep(5)
        return self.connection.run(command, hide=True).stdout.strip()

    def disk_free(self):
        return self.run("df -h")

    @staticmethod
    def extract_percent(output):
        free_line = output.split("\n")[1]
        percent = free_line.split()[4]
        return percent
