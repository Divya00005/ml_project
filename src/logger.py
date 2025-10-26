import logging
import os
from datetime import datetime

# Step 1: Create a log file name based on the current time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Create a 'logs' directory in the current working directory
logs_folder = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_folder, exist_ok=True)

# Step 3: Define the complete log file path
LOG_FILE_PATH = os.path.join(logs_folder, LOG_FILE)

# Step 4: Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s %(lineno)d %(name)s %(levelname)s %(message)s",
    level=logging.INFO
)
