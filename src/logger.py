import logging
import os
from datetime import datetime

# Create a unique file name based on current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the folder path where logs will be stored
# It creates a 'logs' folder in your current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

#  Create the directory even if it already exists
os.makedirs(logs_path, exist_ok=True)

#  Final path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

#  Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("logging has started")