from model import Model
import pandas as pd


class Month(Model):
    def __init__(self, month, sales_data, item_data, employee_data):
        super().__init__()
        self.month = month
        self.sales_data = sales_data
        self.item_data = item_data
        self.employee_data = employee_data
        self.clean_data()
        self.calc_total_sales()
        self.calc_category_sales()
        self.calc_employee_sales()
        self.calc_item_sales()
        self.calc_location_sales()


    def clean_data(self):
        month_code = ""
        if self.month == "January":
            month_code = "01"
        elif self.month == "February":
            month_code = "02"
        elif self.month == "March":
            month_code = "03"
        elif self.month == "April":
            month_code = "04"
        elif self.month == "May":
            month_code = "05"
        elif self.month == "June":
            month_code = "06"
        elif self.month == "July":
            month_code = "07"
        elif self.month == "August":
            month_code = "08"
        elif self.month == "September":
            month_code = "09"
        elif self.month == "October":
            month_code = "10"
        elif self.month == "November":
            month_code = "11"
        elif self.month == "December":
            month_code = "12"

        sd_frame = pd.DataFrame(self.sales_data, columns=["First Name", "Last Name", "Item", "Quantity", "Date"])
        sd_frame = sd_frame.sort_values("Date")
        sd_list = sd_frame.values.tolist()
        sd_month = []

        if self.month != "ALL":
            for x in range(len(sd_list)):
                if sd_list[x][4][5:7] == month_code:
                    sd_month.append(sd_list[x])
            self.sales_data = sd_month.copy()
