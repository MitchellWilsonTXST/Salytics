from model import Model
from view import View
from controller import Controller
import pytest


@pytest.fixture(scope="module")
def init():
    pass

def test_read():
    print("\n---------- TEST READ ----------")
    model = Model()
    model.read_data("data/Sales_Data.csv")
    assert len(model.sales_data) == 150000

def test_years():
    model = Model()
    model.read_data("data/Sales_Data.csv")
    model.get_years()
    years = ["ALL", "2019", "2018", "2017"]
    assert model.years == years

def test_sort():
    model = Model()
    model.read_data("data/Sales_Data.csv")
    model.sort_sd_date()
    failures = 0
    for x in range(len(model.sales_data)):
        if x < len(model.sales_data)-1:
            if model.sales_data[x][4] > model.sales_data[x+1][4]:
                failures = failures + 1
    assert failures == 0



