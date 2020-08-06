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
    print(failures)
    assert failures == 0


def test_years():
    test = [[0, 0, 0, 0, "2012-01-14"],
            [0, 0, 0, 0, "2013-10-01"]]
    model = Model()
    model.sales_data = test
    model.get_years()
    assert model.years == ["ALL", "2013", "2012"]


def test_total():
    model = Model()
    model.sales_data = [["Wilson", "Mitchell", "Chair", 2, "2014-01-01"],
                        ["Smith", "Bob", "Table", 1, "2014-01-02"]]
    model.item_data = [["Chair", "A", 10],
                       ["Table", "B", 20]]
    model.calc_total_sales()
    assert model.daily_revenue == [20]


def test_cat():
    model = Model()
    model.sales_data = [["Bob", "Bob", "Chair", 2, "2012-01-01"],
                        ["Bob", "Bob", "Table", 2, "2012-01-02"],
                        ["Ted", "Bob", "Chair", 0, "2012-01-03"]]
    model.item_data = [["Chair", "Chairs", 10],
                       ["Table", "Tables", 20]]
    model.calc_category_sales()
    assert model.category_revenue == [40, 20, 0, 0, 0, 0, 0]


def test_emp():
    model = Model()
    model.sales_data = [["Bob", "Bob", "Chair", 2, "2012-01-01"],
                        ["Bob", "Bob", "Table", 2, "2012-01-02"],
                        ["Ted", "Bob", "Chair", 0, "2012-01-03"]]
    model.item_data = [["Chair", "Chairs", 10],
                       ["Table", "Tables", 20]]
    model.employee_data = [["Bob", "Bob", "M", "Kansas City", 60],
                           ["Ted", "Bob", "M", "Houston", 50]]
    model.calc_employee_sales()
    assert model.er_frame.values.tolist() == [["Bob", "Bob", 60],
                                              ["Ted", "Bob", 0]]


def test_item():
    model = Model()
    model.sales_data = [["Bob", "Bob", "Chair", 2, "2012-01-01"],
                        ["Bob", "Bob", "Table", 2, "2012-01-02"],
                        ["Ted", "Bob", "Chair", 0, "2012-01-03"]]
    model.item_data = [["Chair", "Chairs", 10],
                       ["Table", "Tables", 20]]
    model.employee_data = [["Bob", "Bob", "M", "Kansas City", 60],
                           ["Ted", "Bob", "M", "Houston", 50]]
    model.calc_item_sales()
    assert model.item_frame.values.tolist() == [["Table", 40],
                                                ["Chair", 20]]
