import os 
import sys 
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"

loggingdir ="logs"
log_filepath = os.path.join(loggingdir, "running_logs.log")
os.makedirs(loggingdir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("datascincelogger")