from model import Model
import pandas as pd


class Year(Model):
    def __init__(self, year, sales_data, item_data, employee_data):
        super().__init__()
        self.year = year
        self.sales_data = sales_data.copy()
        self.item_data = item_data.copy()
        self.employee_data = employee_data.copy()
        if self.year != "ALL":
            self.clean_data()
        self.calc_total_sales()
        self.calc_category_sales()
        self.calc_employee_sales()
        self.calc_item_sales()
        self.calc_location_sales()


    def clean_data(self):
        sd_frame = pd.DataFrame(self.sales_data, columns=["First Name", "Last Name", "Item", "Quantity", "Date"])
        sd_frame = sd_frame.sort_values("Date")
        sd_list = sd_frame.values.tolist()
        sd_year = []

        for x in range(len(sd_list)):
            if sd_list[x][4][:4] == self.year:
                sd_year.append(sd_list[x])
        self.sales_data = sd_year.copy()
