from loguru import logger
import inspect

class LogHandler:
    def __init__(self, namespace: str, log_file: str = "app.log", level: str = "INFO"):
        # Remove qualquer configuração anterior
        logger.remove()

        # Define um formato de log estruturado incluindo o namespace e o chamador
        log_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{extra[namespace]}</cyan>:<cyan>{extra[caller]}</cyan>:<cyan>{extra[line]}</cyan> - "
            "<level>{message}</level>"
        )

        # Configura o logger para registrar em um arquivo e na saída padrão
        logger.add(log_file, level=level, format=log_format, rotation="10 MB", retention="10 days", compression="zip")
        logger.add(lambda msg: print(msg, end=''), level=level, format=log_format)

        # Armazena o namespace para ser usado nos logs
        self.namespace = namespace

    def _get_caller_info(self):
        # Captura o nome da classe e a linha que chamou o log
        frame = inspect.currentframe().f_back.f_back.f_back  # Subindo três níveis na pilha
        module = inspect.getmodule(frame)
        line_number = frame.f_lineno
        class_name = frame.f_locals.get('self', None).__class__.__name__ if 'self' in frame.f_locals else '__Main__'
        return (module.__name__, class_name, line_number)

    def _lognamespace(self, level: str, message: str):
        # Vincula o namespace, o chamador e a linha do chamador ao log
        module_name, class_name, line_number = self._get_caller_info()
        caller_info = f"{class_name}" if class_name else "Function"
        logger.bind(namespace=self.namespace, caller=caller_info, line=line_number).log(level, message)

    def debug(self, message: str):
        self._lognamespace("DEBUG", message)

    def info(self, message: str):
        self._lognamespace("INFO", message)

    def warning(self, message: str):
        self._lognamespace("WARNING", message)

    def error(self, message: str):
        self._lognamespace("ERROR", message)

    def critical(self, message: str):
        self._lognamespace("CRITICAL", message)