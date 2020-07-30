from model import Model
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
