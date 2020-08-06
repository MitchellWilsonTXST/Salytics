from model import Model
from view import View
from year import Year
from quarter import Quarter
from month import Month
from category import Category
from location import Location
from item import Item
from salesperson import Salesperson
import time


class Controller:
    def __init__(self):
        self.model = Model()
        self.model.read_data("data/Sales_Data.csv")
        self.model.read_data("data/Item_Data.csv")
        self.model.read_data("data/Employee_Data.csv")
        self.model.sort_sd_date()
        self.model.get_years()
        self.model.calc_total_sales()
        self.model.calc_category_sales()
        self.model.calc_employee_sales()
        self.model.calc_item_sales()
        self.model.calc_location_sales()

        self.view = View(self)
        self.view.top_frame_menus(self.model.years)
        self.year = Year(self.model.year, self.model.sales_data, self.model.item_data, self.model.employee_data)


        self.quarter = Quarter(self.model.quarter, self.year.sales_data, self.year.item_data, self.year.employee_data)
        self.month = Month(self.model.month, self.quarter.sales_data,
                           self.quarter.item_data, self.quarter.employee_data)

        self.view.init_left_plot(self.model.daily_revenue)
        self.view.init_q1_plot(self.model.er_frame)
        self.view.init_q2_plot(self.model.item_frame)
        self.view.init_q3_plot(self.model.category_names, self.model.category_revenue)
        self.view.init_q4_plot(self.model.locations, self.model.location_sales)


    def main(self):
        self.view.main()


    def year_selected(self, event):
        self.model.year = self.view.year_menu.get()
        self.year.year = self.view.year_menu.get()
        self.year.sales_data = self.model.sales_data.copy()

        if self.model.year != "ALL":
            self.year.clean_data()
            self.year.calc_total_sales()
            self.year.calc_employee_sales()
            self.year.calc_item_sales()
            self.year.calc_category_sales()
            self.year.calc_location_sales()

            self.view.canvas_left.get_tk_widget().destroy()
            self.view.init_left_plot(self.year.daily_revenue)
            self.view.employee_list.destroy()
            self.view.init_q1_plot(self.year.er_frame)
            self.view.item_list.destroy()
            self.view.init_q2_plot(self.year.item_frame)
            self.view.canvas_q3.get_tk_widget().destroy()
            self.view.init_q3_plot(self.year.category_names, self.year.category_revenue)
            self.view.canvas_q4.get_tk_widget().destroy()
            self.view.init_q4_plot(self.year.locations, self.year.location_sales)
        else:
            self.view.canvas_left.get_tk_widget().destroy()
            self.view.init_left_plot(self.model.daily_revenue)
            self.view.employee_list.destroy()
            self.view.init_q1_plot(self.model.er_frame)
            self.view.item_list.destroy()
            self.view.init_q2_plot(self.model.item_frame)
            self.view.canvas_q3.get_tk_widget().destroy()
            self.view.init_q3_plot(self.model.category_names, self.model.category_revenue)
            self.view.canvas_q4.get_tk_widget().destroy()
            self.view.init_q4_plot(self.model.locations, self.model.location_sales)

        self.model.quarter = "ALL"
        self.model.month = "ALL"
        self.view.quarter_menu.current(0)
        self.view.month_menu.current(0)

        if self.model.quarter == "Q1":
            months = ["ALL", "January", "February", "March"]
        elif self.model.quarter == "Q2":
            months = ["ALL", "April", "May", "June"]
        elif self.model.quarter == "Q3":
            months = ["ALL", "July", "August", "September"]
        elif self.model.quarter == "Q4":
            months = ["ALL", "October", "November", "December"]
        else:
            months = ["ALL", "January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"]

        self.model.month = "ALL"
        self.view.update_month_menu(months)
        self.view.month_menu.current(0)


    def quarter_selected(self, event):
        self.model.quarter = self.view.quarter_menu.get()
        self.quarter.quarter = self.view.quarter_menu.get()
        self.quarter.sales_data = self.year.sales_data.copy()

        if self.model.quarter != "ALL":
            self.quarter.clean_data()
            self.quarter.calc_total_sales()
            self.quarter.calc_employee_sales()
            self.quarter.calc_item_sales()
            self.quarter.calc_category_sales()
            self.quarter.calc_location_sales()

            self.view.canvas_left.get_tk_widget().destroy()
            self.view.init_left_plot(self.quarter.daily_revenue)
            self.view.employee_list.destroy()
            self.view.init_q1_plot(self.quarter.er_frame)
            self.view.item_list.destroy()
            self.view.init_q2_plot(self.quarter.item_frame)
            self.view.canvas_q3.get_tk_widget().destroy()
            self.view.init_q3_plot(self.quarter.category_names, self.quarter.category_revenue)
            self.view.canvas_q4.get_tk_widget().destroy()
            self.view.init_q4_plot(self.quarter.locations, self.quarter.location_sales)
        else:
            self.view.canvas_left.get_tk_widget().destroy()
            self.view.init_left_plot(self.year.daily_revenue)
            self.view.employee_list.destroy()
            self.view.init_q1_plot(self.year.er_frame)
            self.view.item_list.destroy()
            self.view.init_q2_plot(self.year.item_frame)
            self.view.canvas_q3.get_tk_widget().destroy()
            self.view.init_q3_plot(self.year.category_names, self.year.category_revenue)
            self.view.canvas_q4.get_tk_widget().destroy()
            self.view.init_q4_plot(self.year.locations, self.year.location_sales)

        if self.model.quarter == "Q1":
            months = ["ALL", "January", "February", "March"]
        elif self.model.quarter == "Q2":
            months = ["ALL", "April", "May", "June"]
        elif self.model.quarter == "Q3":
            months = ["ALL", "July", "August", "September"]
        elif self.model.quarter == "Q4":
            months = ["ALL", "October", "November", "December"]
        else:
            months = ["ALL", "January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"]

        self.model.month = "ALL"
        self.view.update_month_menu(months)
        self.view.month_menu.current(0)


    def month_selected(self, event):
        self.model.month = self.view.month_menu.get()
        self.month.month = self.view.month_menu.get()
        self.quarter.sales_data = self.year.sales_data
        self.month.sales_data = self.quarter.sales_data

        if self.model.month != "ALL":
            self.month.clean_data()
            self.month.calc_total_sales()
            self.month.calc_employee_sales()
            self.month.calc_item_sales()
            self.month.calc_category_sales()
            self.month.calc_location_sales()

            self.view.canvas_left.get_tk_widget().destroy()
            self.view.init_left_plot(self.month.daily_revenue)
            self.view.employee_list.destroy()
            self.view.init_q1_plot(self.month.er_frame)
            self.view.item_list.destroy()
            self.view.init_q2_plot(self.month.item_frame)
            self.view.canvas_q3.get_tk_widget().destroy()
            self.view.init_q3_plot(self.month.category_names, self.month.category_revenue)
            self.view.canvas_q4.get_tk_widget().destroy()
            self.view.init_q4_plot(self.month.locations, self.month.location_sales)
        else:
            self.view.canvas_left.get_tk_widget().destroy()
            self.view.init_left_plot(self.quarter.daily_revenue)
            self.view.employee_list.destroy()
            self.view.init_q1_plot(self.quarter.er_frame)
            self.view.item_list.destroy()
            self.view.init_q2_plot(self.quarter.item_frame)
            self.view.canvas_q3.get_tk_widget().destroy()
            self.view.init_q3_plot(self.quarter.category_names, self.quarter.category_revenue)
            self.view.canvas_q4.get_tk_widget().destroy()
            self.view.init_q4_plot(self.quarter.locations, self.quarter.location_sales)


    def view_selected(self, frame):
        if self.model.month != "ALL":
            if frame == "left":
                self.view.show_left_plot(self.month.daily_revenue, self.model.year, self.model.quarter, self.model.month)
            elif frame == "q3":
                self.view.show_q3_plot(self.month.category_names, self.month.category_revenue)
            elif frame == "q4":
                self.view.show_q4_plot(self.month.locations, self.month.location_sales)
        elif self.model.quarter != "ALL":
            if frame == "left":
                self.view.show_left_plot(self.quarter.daily_revenue, self.model.year, self.model.quarter, self.model.month)
            elif frame == "q3":
                self.view.show_q3_plot(self.quarter.category_names, self.quarter.category_revenue)
            elif frame == "q4":
                self.view.show_q4_plot(self.quarter.locations, self.quarter.location_sales)
        elif self.model.year != "ALL":
            if frame == "left":
                self.view.show_left_plot(self.year.daily_revenue, self.model.year, self.model.quarter, self.model.month)
            elif frame == "q3":
                self.view.show_q3_plot(self.year.category_names, self.year.category_revenue)
            elif frame == "q4":
                self.view.show_q4_plot(self.year.locations, self.year.location_sales)
        else:
            if frame == "left":
                self.view.show_left_plot(self.model.daily_revenue, self.model.year, self.model.quarter, self.model.month)
            elif frame == "q3":
                self.view.show_q3_plot(self.model.category_names, self.model.category_revenue)
            elif frame == "q4":
                self.view.show_q4_plot(self.model.locations, self.model.location_sales)


    def init_explore(self, exp):
        self.model.explore = exp
        self.view.exp_base_frames(self.model.explore)
        self.view.home_button(self.view.exp_top_frame)
        self.view.explore_buttons(self.model.explore)
        self.view.blank_graphs(self.model.explore)
        self.view.explore_time(self.model.year, self.model.quarter, self.model.month)
        if exp == "Category":
            self.view.cat_set_weights()
            self.view.explore_menu(self.model.explore, self.model.category_names)
            self.init_category()
        elif exp == "Location":
            self.view.cat_set_weights()
            self.view.explore_menu(self.model.explore, self.model.locations)
            self.init_location()
        elif exp == "Item":
            self.view.cat_set_weights()
            self.view.explore_menu(self.model.explore, self.model.item_names)
            self.init_item()
        elif exp == "Salesperson":
            print(self.model.employee_names[0][0] + " " + self.model.employee_names[0][1])
            names = []
            for x in self.model.employee_names:
                names.append(x[0] + " " + x[1])
            self.view.cat_set_weights()
            self.view.explore_menu(self.model.explore, names)
            self.init_employee()


    def init_exp_2(self, exp):
        self.model.explore = self.model.explore + "/" + exp
        self.view.exp_base_frames_2(self.model.explore)
        self.view.home_button(self.view.exp_top_frame)
        self.view.exp_buttons_2(self.model.explore)
        self.view.blank_graphs(self.model.explore)
        self.view.exp_set_weights()
        self.view.explore_time(self.model.year, self.model.quarter, self.model.month)
        if self.model.explore == "Category/Location":
            self.view.explore_menu(self.model.explore, self.model.locations)
            self.init_cat_loc()
        elif self.model.explore == "Category/Item":
            names = []
            for x in self.model.item_data:
                if x[1] == self.category.category:
                    names.append(x[0])
            self.view.explore_menu(self.model.explore, names)
            self.init_cat_item()
        elif self.model.explore == "Location/Category":
            self.view.explore_menu(self.model.explore, self.model.category_names)
            self.init_loc_cat()


    def init_exp_3(self, exp):
        self.model.explore = self.model.explore + "/" + exp
        self.view.exp_base_frames_3(self.model.explore)
        self.view.home_button(self.view.exp_top_frame)
        self.view.exp_buttons_3(self.model.explore)
        self.view.blank_graphs_2(self.model.explore)
        self.view.exp_set_weights_2()
        self.view.explore_time(self.model.year, self.model.quarter, self.model.month)
        if self.model.explore == "Category/Location/Item":
            names = []
            for x in self.model.item_data:
                if x[1] == self.category.category:
                    names.append(x[0])
            self.view.explore_menu(self.model.explore, names)
            self.init_cat_loc_item()
        elif self.model.explore == "Category/Item/Location":
            self.view.explore_menu(self.model.explore, self.model.locations)
            self.init_cat_item_loc()
        elif self.model.explore == "Location/Category/Item":
            names = []
            for x in self.model.item_data:
                if x[1] == self.category.category:
                    names.append(x[0])
            self.view.explore_menu(self.model.explore, names)
            self.init_loc_cat_item()


    def refresh(self):
        self.model.first = True
        if self.model.explore == "Category" or self.model.explore == "Location"\
            or self.model.explore == "Item" or self.model.explore == "Salesperson":
            self.view.explore_frame.pack_forget()
            self.view.explore_frame.destroy()
            self.view.main_frame.pack(fill="both", expand=True)
        elif self.model.explore == "Category/Location" or self.model.explore == "Category/Item":
            self.view.exp_frame_2.pack_forget()
            self.view.exp_frame_2.destroy()
            self.view.main_frame.pack(fill="both", expand=True)
        elif self.model.explore == "Category/Location/Item" or self.model.explore == "Category/Item/Location":
            self.view.exp_frame_3.pack_forget()
            self.view.exp_frame_3.destroy()
            self.view.main_frame.pack(fill="both", expand=True)
        self.year = Year(self.model.year, self.model.sales_data, self.model.item_data, self.model.employee_data)
        self.quarter = Quarter(self.model.quarter, self.year.sales_data, self.year.item_data, self.year.employee_data)
        self.month = Month(self.model.month, self.quarter.sales_data,
                           self.quarter.item_data, self.quarter.employee_data)
        self.view.canvas_left.get_tk_widget().destroy()
        self.view.init_left_plot(self.year.daily_revenue)
        self.view.employee_list.destroy()
        self.view.init_q1_plot(self.year.er_frame)
        self.view.item_list.destroy()
        self.view.init_q2_plot(self.year.item_frame)
        self.view.canvas_q3.get_tk_widget().destroy()
        self.view.init_q3_plot(self.year.category_names, self.year.category_revenue)
        self.view.canvas_q4.get_tk_widget().destroy()
        self.view.init_q4_plot(self.year.locations, self.year.location_sales)



    def all_children(window):
        _list = window.winfo_children()

        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())

        return _list


    def init_category(self):
        sd = []
        id = []
        ed = []
        if self.model.month != "ALL":
            sd = self.month.sales_data.copy()
            id = self.month.item_data.copy()
            ed = self.month.employee_data.copy()
        elif self.model.quarter != "ALL":
            sd = self.quarter.sales_data.copy()
            id = self.quarter.item_data.copy()
            ed = self.quarter.employee_data.copy()
        elif self.model.year != "ALL":
            sd = self.year.sales_data.copy()
            id = self.year.item_data.copy()
            ed = self.year.employee_data.copy()
        else:
            sd = self.model.sales_data.copy()
            id = self.model.item_data.copy()
            ed = self.model.employee_data.copy()
        self.category = Category(sd, id, ed)


    def init_location(self):
        sd = []
        id = []
        ed = []
        if self.model.month != "ALL":
            sd = self.month.sales_data.copy()
            id = self.month.item_data.copy()
            ed = self.month.employee_data.copy()
        elif self.model.quarter != "ALL":
            sd = self.quarter.sales_data.copy()
            id = self.quarter.item_data.copy()
            ed = self.quarter.employee_data.copy()
        elif self.model.year != "ALL":
            sd = self.year.sales_data.copy()
            id = self.year.item_data.copy()
            ed = self.year.employee_data.copy()
        else:
            sd = self.model.sales_data.copy()
            id = self.model.item_data.copy()
            ed = self.model.employee_data.copy()
        self.location = Location(sd, id, ed)


    def init_item(self):
        sd = []
        id = []
        ed = []
        if self.model.month != "ALL":
            sd = self.month.sales_data.copy()
            id = self.month.item_data.copy()
            ed = self.month.employee_data.copy()
        elif self.model.quarter != "ALL":
            sd = self.quarter.sales_data.copy()
            id = self.quarter.item_data.copy()
            ed = self.quarter.employee_data.copy()
        elif self.model.year != "ALL":
            sd = self.year.sales_data.copy()
            id = self.year.item_data.copy()
            ed = self.year.employee_data.copy()
        else:
            sd = self.model.sales_data.copy()
            id = self.model.item_data.copy()
            ed = self.model.employee_data.copy()
        self.item = Item(sd, id, ed)


    def init_employee(self):
        sd = []
        id = []
        ed = []
        if self.model.month != "ALL":
            sd = self.month.sales_data.copy()
            id = self.month.item_data.copy()
            ed = self.month.employee_data.copy()
        elif self.model.quarter != "ALL":
            sd = self.quarter.sales_data.copy()
            id = self.quarter.item_data.copy()
            ed = self.quarter.employee_data.copy()
        elif self.model.year != "ALL":
            sd = self.year.sales_data.copy()
            id = self.year.item_data.copy()
            ed = self.year.employee_data.copy()
        else:
            sd = self.model.sales_data.copy()
            id = self.model.item_data.copy()
            ed = self.model.employee_data.copy()
        self.salesperson = Salesperson(sd, id, ed)


    def init_cat_loc(self):
        sd = []
        id = []
        ed = []
        sd = self.category.sales_data.copy()
        id = self.category.item_data.copy()
        ed = self.category.employee_data.copy()
        self.model.first = True
        self.location = Location(sd, id, ed)


    def init_cat_item(self):
        sd = []
        id = []
        ed = []
        sd = self.category.sales_data.copy()
        id = self.category.item_data.copy()
        ed = self.category.employee_data.copy()
        self.model.first = True
        self.item = Item(sd, id, ed)


    def init_cat_loc_item(self):
        sd = []
        id = []
        ed = []
        sd = self.location.sales_data.copy()
        id = self.location.item_data.copy()
        ed = self.location.employee_data.copy()
        self.model.first = True
        self.item = Item(sd, id, ed)


    def init_cat_item_loc(self):
        sd = []
        id = []
        ed = []
        sd = self.item.sales_data.copy()
        id = self.item.item_data.copy()
        ed = self.item.employee_data.copy()
        self.model.first = True
        self.location = Location(sd, id, ed)


    def init_loc_cat_item(self):
        sd = []
        id = []
        ed = []
        sd = self.category.sales_data.copy()
        id = self.category.item_data.copy()
        ed = self.category.employee_data.copy()
        self.model.first = True
        self.item = Item(sd, id, ed)


    def init_loc_cat(self):
        sd = []
        id = []
        ed = []
        sd = self.location.sales_data.copy()
        id = self.location.item_data.copy()
        ed = self.location.employee_data.copy()
        self.model.first = True
        self.category = Category(sd, id, ed)


    def category_selected(self, event):
        self.category.category = self.view.exp_menu.get()
        self.category.clean_data()
        self.view.canvas_q1_exp.get_tk_widget().destroy()
        self.view.canvas_q2_exp.get_tk_widget().destroy()
        if not self.model.first:
            self.view.employee_list_exp.destroy()
            self.view.item_list_exp.destroy()
        else:
            self.model.first = False
            self.view.employee_list_exp.get_tk_widget().destroy()
            self.view.item_list_exp.get_tk_widget().destroy()
        self.view.init_cat_q3(self.category.daily_revenue)
        self.view.init_cat_q4(self.category.locations, self.category.location_sales)
        self.view.init_cat_q1(self.category.er_frame)
        self.view.init_cat_q2(self.category.item_frame)
        self.view.explore_frame.grid_rowconfigure(1, weight=1)


    def location_selected(self, event):
        self.location.location = self.view.exp_menu.get()
        self.location.clean_data()
        self.view.canvas_q1_exp.get_tk_widget().destroy()
        self.view.canvas_q2_exp.get_tk_widget().destroy()
        if not self.model.first:
            self.view.employee_list_exp.destroy()
            self.view.item_list_exp.destroy()
        else:
            self.model.first = False
            self.view.employee_list_exp.get_tk_widget().destroy()
            self.view.item_list_exp.get_tk_widget().destroy()
        self.view.init_cat_q3(self.location.daily_revenue)
        self.view.init_cat_q4(self.location.category_names, self.location.category_revenue)
        self.view.init_cat_q1(self.location.er_frame)
        self.view.init_cat_q2(self.location.item_frame)
        self.view.explore_frame.grid_rowconfigure(1, weight=1)


    def item_selected(self, event):
        self.item.item = self.view.exp_menu.get()
        self.item.clean_data()
        self.view.canvas_q1_exp.get_tk_widget().destroy()
        self.view.canvas_q2_exp.get_tk_widget().destroy()
        if not self.model.first:
            self.view.employee_list_exp.destroy()
        else:
            self.model.first = False
            self.view.employee_list_exp.get_tk_widget().destroy()
        self.view.init_cat_q3(self.item.daily_revenue)
        self.view.init_cat_q1(self.item.er_frame)
        self.view.init_cat_q4(self.item.locations, self.item.location_sales)
        self.view.explore_frame.grid_rowconfigure(1, weight=1)


    def employee_selected(self, event):
        self.salesperson.salesperson = self.view.exp_menu.get()
        self.salesperson.clean_data()
        self.view.canvas_q1_exp.get_tk_widget().destroy()
        self.view.canvas_q2_exp.get_tk_widget().destroy()
        #if not self.model.first:
        #    self.view.employee_list_exp.destroy()
        #else:
        #    self.model.first = False
        #    self.view.employee_list_exp.get_tk_widget().destroy()
        if not self.model.first:
            self.view.item_list_exp.destroy()
        else:
            self.model.first = False
        self.view.employee_list_exp.get_tk_widget().destroy()
        self.view.init_cat_q3(self.salesperson.daily_revenue)
        self.view.init_cat_q2(self.salesperson.item_frame)
        self.view.init_cat_q4(self.salesperson.category_names, self.salesperson.category_revenue)
        self.view.explore_frame.grid_rowconfigure(1, weight=1)


    def cat_loc_selected(self, event):
        self.location.location = self.view.exp_menu.get()
        self.location.clean_data()
        self.view.canvas_q1_exp.get_tk_widget().destroy()
        self.view.canvas_q2_exp.get_tk_widget().destroy()
        self.view.item_list_exp.destroy()
        if self.model.first:
            self.view.employee_list_exp.get_tk_widget().destroy()
            self.model.first = False
        else:
            self.view.employee_list_exp.destroy()
        self.view.init_cat_q3(self.location.daily_revenue)
        self.view.init_cat_q1(self.location.er_frame)
        self.view.init_cat_q2(self.location.item_frame)


    def cat_item_selected(self, event):
        self.item.item = self.view.exp_menu.get()
        self.item.clean_data()
        self.view.canvas_q1_exp.get_tk_widget().destroy()
        self.view.canvas_q2_exp.get_tk_widget().destroy()
        self.view.item_list_exp.destroy()
        if self.model.first:
            self.view.employee_list_exp.get_tk_widget().destroy()
            self.model.first = False
        else:
            self.view.employee_list_exp.destroy()
        self.view.init_cat_q3(self.item.daily_revenue)
        self.view.init_cat_q1(self.item.er_frame)
        self.view.init_cat_q4(self.item.locations, self.item.location_sales)


    def cat_loc_item_selected(self, event):
        self.item.item = self.view.exp_menu.get()
        self.item.clean_data()
        self.view.canvas_q1_exp.get_tk_widget().destroy()
        self.view.canvas_q2_exp.get_tk_widget().destroy()
        #self.view.item_list_exp.destroy()
        self.view.employee_list_exp.destroy()
        self.view.init_cat_q3(self.item.daily_revenue)
        self.view.init_cat_q1(self.item.er_frame)


    def cat_item_loc_selected(self, event):
        self.location.location = self.view.exp_menu.get()
        self.location.clean_data()
        self.view.canvas_q1_exp.get_tk_widget().destroy()
        self.view.canvas_q2_exp.get_tk_widget().destroy()
        # self.view.item_list_exp.destroy()
        self.view.employee_list_exp.destroy()
        self.view.init_cat_q3(self.location.daily_revenue)
        self.view.init_cat_q1(self.location.er_frame)


    def loc_cat_selected(self, event):
        self.category.category = self.view.exp_menu.get()
        self.category.clean_data()
        self.view.canvas_q1_exp.get_tk_widget().destroy()
        self.view.canvas_q2_exp.get_tk_widget().destroy()
        self.view.item_list_exp.destroy()
        if self.model.first:
            self.view.employee_list_exp.get_tk_widget().destroy()
            self.model.first = False
        else:
            self.view.employee_list_exp.destroy()
        self.view.init_cat_q3(self.category.daily_revenue)
        self.view.init_cat_q1(self.category.er_frame)
        self.view.init_cat_q2(self.category.item_frame)


    def loc_cat_item_selected(self, event):
        self.item.item = self.view.exp_menu.get()
        self.item.clean_data()
        self.view.canvas_q1_exp.get_tk_widget().destroy()
        self.view.canvas_q2_exp.get_tk_widget().destroy()
        # self.view.item_list_exp.destroy()
        self.view.employee_list_exp.destroy()
        self.view.init_cat_q3(self.item.daily_revenue)
        self.view.init_cat_q1(self.item.er_frame)


    def exp_view_selected(self, frame):
        if self.model.explore == "Category":
            if frame == "q3":
                self.view.show_left_plot(self.category.daily_revenue, self.model.year, self.model.quarter, self.model.month)
            elif frame == "q4":
                self.view.show_q4_plot(self.category.locations, self.category.location_sales)


    def exp_view_selected_2(self, frame):
        if self.model.explore == "Category/Location":
            if frame == "q1":
                self.view.show_left_plot(self.location.daily_revenue, self.model.year, self.model.quarter, self.model.month)


if __name__ == "__main__":
    dashboard = Controller()
    dashboard.main()
