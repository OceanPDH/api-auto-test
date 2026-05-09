import logging
import os


def get_logger(name="api-test"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # 控制台输出
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)

        # 文件输出
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, "test.log")
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console)
        logger.addHandler(file_handler)

    return logger
