from model import Model
import pandas as pd


class Location(Model):
    location = ""

    def __init__(self, sales_data, item_data, employee_data):
        super().__init__()
        self.sales_data_initial = sales_data.copy()
        self.sales_data = sales_data.copy()
        self.item_data = item_data.copy()
        self.employee_data = employee_data.copy()


    def clean_data(self):
        item_names = []
        for x in self.item_data:
            item_names.append(x[0])

        locations = []
        employee_names = []
        for x in self.employee_data:
            locations.append(x[3])
            employee_names.append(x[:2])
        locations = list(dict.fromkeys(locations))

        sd = []
        for x in self.sales_data_initial:
            employee_name = x[:2]
            branch_index_ed = employee_names.index(employee_name)
            branch_name = self.employee_data[branch_index_ed][3]
            if branch_name == self.location:
                sd.append(x)
        self.sales_data = sd.copy()

        self.calc_total_sales()
        self.calc_category_sales()
        self.calc_employee_sales()
        self.calc_item_sales()
        self.calc_location_sales()