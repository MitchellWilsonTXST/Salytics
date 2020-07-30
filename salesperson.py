from model import Model
import pandas as pd


class Salesperson(Model):
    salesperson = []

    def __init__(self, sales_data, item_data, employee_data):
        super().__init__()
        self.sales_data_initial = sales_data.copy()
        self.sales_data = sales_data.copy()
        self.item_data = item_data.copy()
        self.employee_data = employee_data.copy()


    def clean_data(self):
        sd = []
        for x in self.sales_data_initial:
            x2 = str(x[0]) + " " + str(x[1])
            if x2 == self.salesperson:
                sd.append(x)
        self.sales_data = sd.copy()

        self.calc_total_sales()
        self.calc_category_sales()
        self.calc_employee_sales()
        self.calc_item_sales()
        self.calc_location_sales()