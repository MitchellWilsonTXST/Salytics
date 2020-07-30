from model import Model
import pandas as pd


class Category(Model):
    category = ""

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

        item_categories = []
        for x in self.item_data:
            item_names.append(x[0])
            item_categories.append(x[1])

        sd = []
        category_names = ["Tables", "Chairs", "Mirrors", "Dressers", "Nightstands", "Cabinet Knobs", "Miscellaneous"]
        for x in self.sales_data_initial:
            location_item = item_names.index(x[2])
            category = item_categories[location_item]
            if category == self.category:
                sd.append(x)
        self.sales_data = sd.copy()

        self.calc_total_sales()
        self.calc_category_sales()
        self.calc_employee_sales()
        self.calc_item_sales()
        self.calc_location_sales()
