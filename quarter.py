from model import Model
import pandas as pd


class Quarter(Model):
    def __init__(self, quarter, sales_data, item_data, employee_data):
        super().__init__()
        self.quarter = quarter
        self.sales_data = sales_data.copy()
        self.item_data = item_data.copy()
        self.employee_data = employee_data.copy()
        if self.quarter != "ALL":
            self.clean_data()
        self.calc_total_sales()
        self.calc_category_sales()
        self.calc_employee_sales()
        self.calc_item_sales()
        self.calc_location_sales()


    def clean_data(self):
        months = []
        if self.quarter == "Q1":
            months = ["01", "02", "03"]
        elif self.quarter == "Q2":
            months = ["04", "05", "06"]
        elif self.quarter == "Q3":
            months = ["07", "08", "09"]
        elif self.quarter == "Q4":
            months = ["10", "11", "12"]

        sd_frame = pd.DataFrame(self.sales_data, columns=["First Name", "Last Name", "Item", "Quantity", "Date"])
        sd_frame = sd_frame.sort_values("Date")
        sd_list = sd_frame.values.tolist()
        sd_quarter = []

        if self.quarter != "ALL":
            for x in range(len(sd_list)):
                if sd_list[x][4][5:7] == months[0] or sd_list[x][4][5:7] == months[1] or sd_list[x][4][5:7] == months[2]:
                    sd_quarter.append(sd_list[x])
            self.sales_data = sd_quarter.copy()