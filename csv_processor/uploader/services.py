from dataclasses import dataclass
import logging
import pandas as pd
from csv_processor.uploader.models import Address, Customer

logger = logging.getLogger(__name__)


@dataclass
class CsvParserService:
    """Class for processing csv file."""

    file_path: str

    def process(self):
        # Read CSV file and converts it to Panda's DataFrame
        try:
            df = pd.read_csv(self.file_path)
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
                        email=email,
                    )
                except Exception as e:
                    logger.error(e)

                if create:
                    addresses = df[
                        (df["name"] == name) & (df["first_name"] == first_name)
                    ].filter(regex="^address_", axis=1)

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
                                customer=customer,
                            )
                        except Exception as ex:
                            logger.error(ex)
        except (FileNotFoundError, UnicodeDecodeError, pd.parser.CParserError) as exc:
            logger.error(exc)
