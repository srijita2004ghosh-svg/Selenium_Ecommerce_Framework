import logging
import os


class Logger:

    @staticmethod
    def get_logger(name):

        # Find project root
        project_root = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

        # Create reports directory
        reports_dir = os.path.join(
            project_root,
            "reports"
        )

        os.makedirs(
            reports_dir,
            exist_ok=True
        )

        # Log file path
        log_file = os.path.join(
            reports_dir,
            "automation.log"
        )

        # Create logger
        logger = logging.getLogger(name)

        # Avoid duplicate handlers
        if not logger.handlers:

            logger.setLevel(
                logging.INFO
            )

            # File handler
            file_handler = logging.FileHandler(
                log_file,
                encoding="utf-8"
            )

            # Console handler
            console_handler = logging.StreamHandler()

            # Log format
            formatter = logging.Formatter(
                "%(asctime)s - "
                "%(levelname)s - "
                "%(name)s - "
                "%(message)s"
            )

            file_handler.setFormatter(
                formatter
            )

            console_handler.setFormatter(
                formatter
            )

            logger.addHandler(
                file_handler
            )

            logger.addHandler(
                console_handler
            )

        return logger