# Definindo o namespace para este módulo
NAMESPACE = "PSCustomProjects.cliente_wake_sample2"

from logger.log_handler import LogHandler

def main():
    log = LogHandler(namespace=NAMESPACE, level="DEBUG")
    log.warning("This is a warning message.")
    log.error("This is a error message.")
    

if __name__ == '__main__':
    main()
