NAMESPACE = "PSCustomProjects.Libs"
from logger.log_handler import LogHandler

def main():
    log = LogHandler(namespace=NAMESPACE)
    log.info("Call from Libs/Lib-X")
    print("Hello from lib-x")


if __name__ == '__main__':
    main()
