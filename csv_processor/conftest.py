# fixtures to be accessed globally across all tests can be put here
import csv
from io import StringIO
import os
import pandas as pd

# from pandas import testing

from django.core.files.base import ContentFile
from factory.django import ImageField
import pytest
from rest_framework.test import APIClient
from csv_processor.uploader.tests.factories import AddressFactory, CustomerFactory


@pytest.fixture(autouse=True)
def enable_db_access(db):
    """
    Global DB access to all tests.
    :param db:
    :return:
    """
    pass


@pytest.fixture
def synchronize_celery_tasks(settings):
    """
    https://pytest-django.readthedocs.io/en/latest/helpers.html#settings
    :param settings:
    :return:
    """
    settings.CELERY_TASK_ALWAYS_EAGER = True


@pytest.fixture
def client():
    """
    better off using rest framework's api client instead of built in django test client for pytest
    since we'll be working with developing and testing apis
    :return:
    """
    return APIClient()


@pytest.fixture
def image():
    return ContentFile(
        ImageField()._make_data({"width": 1024, "height": 768}), "image.jpg"
    )


@pytest.fixture
def wrong_csv_file():
    tmp_file = r"/tmp/tmp.csv"
    with open(tmp_file, "w") as file:
        writer = csv.writer(file)
        writer.writerows([["Data0", "A0A0A0", 1, "Data3", "Data4", "Data5", 4000]])

    return tmp_file


@pytest.fixture
def csv_file():
    row = ["Name", "Location", "Price"]
    csv_buffer = StringIO()
    csv_writer = csv.writer(csv_buffer)
    csv_writer.writerow(row)

    return ContentFile(csv_buffer.getvalue().encode("utf-8"), "output.csv")


@pytest.fixture
def customer():
    return CustomerFactory()


@pytest.fixture
def address(customer):
    return AddressFactory(customer=customer)


# @pytest.mark.parametrize('test_data, expected', [
#     ([['Data0', 'A0A0A0', 1, 'Data3', 'Data4', 'Data5', 4000]],
#       pd.DataFrame([['A0A0A0', 1, 4000]], columns=['Postal_Code', 'Store_Num', 'Sales'])),
#     ([['Data0', 'A0A0A0', 1, 'Data3', 'Data4', 'Data5', 'Data6', 4000]],
#       pd.DataFrame([['A0A0A0', 1, 4000]], columns=['Postal_Code', 'Store_Num', 'Sales']))
# ])
# def test_sales_dataframe(test_data, expected):

#     # Write your test data in a temporary file
#     tmp_file = r'/tmp/tmp.csv'
#     with open(tmp_file, 'w') as file:
#         writer = csv.writer(file)
#         writer.writerows(test_data)

#     # Process the data
#     sales_df = sales_dataframe(tmp_file)

#     # Compare expected and actual output
#     testing.assert_frame_equal(expected, sales_df)

#     # Clean the temporary file
#     os.remove(tmp_file)


# def sales_dataframe(file):
#     try:
#         with open(file, 'r') as f:
#             reader = csv.reader(f)
#             num_cols = len(next(reader))
#             columns = [1, 2, (num_cols - 1)]  # Number of columns is variable, this is used later to accurately specify which columns should be read. This is part I'm testing!

#         sales_df = pd.read_csv(file, usecols=columns, names=['Postal_Code', 'Store_Num', 'Sales'])
#         return sales_df
#     except FileNotFoundError:
#         raise FileNotFoundError(file)
