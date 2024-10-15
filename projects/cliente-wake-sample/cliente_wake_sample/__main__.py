# Definindo o namespace para este módulo
NAMESPACE = "PSCustomProjects.cliente_wake_sample"

from logger.log_handler import LogHandler
from lib_x.main import main as lib_x_main

def main():
    log = LogHandler(namespace=NAMESPACE, level="DEBUG")
    log.debug("This is a debug message.")
    log.critical("This is a critical message.")
    lib_x_main()

if __name__ == '__main__':
    main()



