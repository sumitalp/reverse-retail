import csv
from celery.utils.log import get_task_logger
from csv_processor.celery import app
from csv_processor.uploader.services import CsvParserService


logger = get_task_logger(__name__)


@app.task
def process_csv(file_path: str):
    """
    @param file: string - File path

    This is a background which is called by application when needed to run
    long running tasks. As we know, the csv file is too long and it will need
    some times to process, thus, we make it here.
    """
    with open(file_path, "r") as infile:
        reader = csv.DictReader(infile)
        logger.info(f"CSV headers: {reader.fieldnames}")
        if reader.fieldnames == [
            "name",
            "first_name",
            "address_street",
            "phone",
            "address_zipcode",
            "address_city",
            "address_country",
            "bank_account_no",
            "bank_name",
            "email",
        ]:
            CsvParserService(file_path).process()
