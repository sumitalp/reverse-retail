import csv
import pandas as pd
from celery.utils.log import get_task_logger
from csv_processor.celery import app
from csv_processor.uploader.models import Address, Customer


logger = get_task_logger(__name__)


@app.task
def process_csv(file_path: str):
    '''
    @param file: string - File path

    This is a background which is called by application when needed to run 
    long running tasks. As we know, the csv file is too long and it will need
    some times to process, thus, we make it here.
    '''
    with open(file_path, 'r') as infile:
        reader = csv.DictReader(infile)
        logger.info(f"CSV headers: {reader.fieldnames}")
        if reader.fieldnames == ['name', 'first_name', 'address_street', 'phone', 'address_zipcode', 'address_city', 'address_country', 'bank_account_no', 'bank_name', 'email']:
            # Read CSV file and converts it to Panda's DataFrame
            try:
                df = pd.read_csv(file_path)
                for row in df.itertuples(index=False, name="Customer"):
                    name = row[0]
                    first_name = row[1]
                    bank_account_no = row[7]
                    bank_name = row[8]
                    phone = row[2]
                    email = row[9]

                    # Customer data is storing in table
                    try:
                        customer, create = Customer.objects.get_or_create(
                            name=name,
                            first_name=first_name,
                            bank_account_no=bank_account_no,
                            bank_name=bank_name,
                            phone=phone,
                            email=email
                        )
                    except Exception as e:
                        logger.error(e)

                    if create:
                        addresses =  df[(df["name"]==name) & (df["first_name"]==first_name)].filter(regex='^address_',axis=1)

                        for address in addresses.itertuples(index=False, name="Address"):
                            street = address[0]
                            zipcode = address[1]
                            city = address[2]
                            country = address[3]

                            # Address data is storing in table
                            try:
                                address, create = Address.objects.get_or_create(
                                    street=street,
                                    zipcode=zipcode,
                                    city=city,
                                    country=country,
                                    customer=customer
                                )
                            except Exception as ex:
                                logger.error(ex)
            except (FileNotFoundError, UnicodeDecodeError, pd.parser.CParserError) as exc:
                logger.error(exc)

                