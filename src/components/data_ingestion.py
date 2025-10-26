# Import required libraries
import os                      # for file path and directory handling
import sys                     # for system-specific parameters (used in CustomException)
from src.exception import CustomException   # custom exception handling class
from src.logger import logging              # custom logger to record program flow
import pandas as pd             # for data handling and CSV operations

from sklearn.model_selection import train_test_split  # to split dataset into train/test sets
from dataclasses import dataclass                     # to easily create configuration classes


# =============================
# Configuration for data paths
# =============================
@dataclass
class DataIngestionConfig:
    """
    This class stores all the file paths where data will be saved.
    The @dataclass decorator automatically creates an __init__ method for us.
    """
    train_data_path: str = os.path.join('artifacts', "train.csv")  # path for training data
    test_data_path: str = os.path.join('artifacts', "test.csv")    # path for testing data
    raw_data_path: str = os.path.join('artifacts', "data.csv")     # path for raw data copy


# =====================================
# Main Data Ingestion Class Definition
# =====================================
class DataIngestion:
    def __init__(self):
        """
        Constructor method initializes the configuration for data ingestion.
        Creates an instance of DataIngestionConfig which holds all file paths.
        """
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Reads the raw dataset, performs a train-test split,
        and saves the data into the 'artifacts' folder.
        """
        logging.info("Entered the data ingestion method or component")

        try:
            # 1️⃣ Read dataset from the source CSV file
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the dataset as a DataFrame')

            # 2️⃣ Create artifacts directory if it doesn’t exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # 3️⃣ Save a copy of the raw data inside artifacts folder
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # 4️⃣ Split the dataset into training and testing sets
            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # 5️⃣ Save the training and testing data into separate CSV files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            # 6️⃣ Return the file paths of train and test data
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            # Handle any exceptions that occur and raise a custom exception
            raise CustomException(e, sys)


# =====================================
# Run the script directly (for testing)
# =====================================
if __name__ == '__main__':
    # Create an object of DataIngestion class
    obj = DataIngestion()

    # Call the ingestion process and get back the paths
    train_path, test_path = obj.initiate_data_ingestion()

    # Optional: print paths to confirm successful execution
    print("Training data saved at:", train_path)
    print("Testing data saved at:", test_path)
