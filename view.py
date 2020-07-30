import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt


class View(tk.Tk):
    """ A class for handling the GUI component of the application"""

    title_color = "white"
    highlight_color = "dodgerblue"
    bg_color = "whitesmoke"
    button_color = "gainsboro"
    bar_color = "dodgerblue"
    top_frame_color = "grey"
    explore = ""

    def __init__(self, controller):
        """
        Initializes the main widgets of the GUI

        :param controller: an instance of the Controller class
        """
        super().__init__()

        self.controller = controller
        self.title("")

        self._main_frame()
        self._base_frames()
        self._sub_frames()
        self._top_frm_labels()
        self._graph_buttons()
        self._set_weights()


    def main(self):
        """
        Runs the main loop of the GUI for event recognition

        :return: none
        """
        self.mainloop()


    def _main_frame(self):
        """
        Creates and places the main frame in which subsequent widgets will be placed

        :return: none
        """
        self.main_frame = tk.LabelFrame(self)
        self.main_frame.pack(fill="both", expand=True)


    def _base_frames(self):
        """
        Creates and places the base frames into the main frame

        :return: none
        """
        self.top_frame = tk.LabelFrame(self.main_frame, padx=10, pady=10, bg=self.top_frame_color,
                                       highlightthickness=10, highlightbackground=self.highlight_color,
                                       width=2300)
        self.left_frame = tk.LabelFrame(self.main_frame, padx=10, pady=10, borderwidth=0,
                                        highlightthickness=0, bg=self.bg_color)
        self.right_frame = tk.LabelFrame(self.main_frame, padx=10, pady=10, borderwidth=0,
                                         highlightthickness=0, bg=self.bg_color)
        self.top_frame.config(highlightcolor="dodgerblue")

        self.top_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.left_frame.grid(row=1, column=0, rowspan=4, padx=10, pady=10, sticky="nsew")
        self.right_frame.grid(row=1, column=1, rowspan=4, padx=10, pady=10, sticky="nsew")


    def _sub_frames(self):
        """
        Creates and places the sub-frames into the base frames

        :return: none
        """
        self.q1_right = tk.LabelFrame(self.right_frame, padx=10, pady=10, bg=self.bg_color,
                                      borderwidth=0, highlightthickness=0)
        self.q2_right = tk.LabelFrame(self.right_frame, padx=10, pady=10, bg=self.bg_color,
                                      borderwidth=0, highlightthickness=0)
        self.q3_right = tk.LabelFrame(self.right_frame, padx=10, pady=10, bg=self.bg_color,
                                      borderwidth=0, highlightthickness=0)
        self.q4_right = tk.LabelFrame(self.right_frame, padx=10, pady=10, bg=self.bg_color,
                                      borderwidth=0, highlightthickness=0)

        self.q1_right.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.q2_right.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.q3_right.grid(row=2, column=0, rowspan=2, sticky="nsew")
        self.q4_right.grid(row=2, column=1, rowspan=2, sticky="nsew")


    def _top_frm_labels(self):
        """
        Creates and places labels into the top frame

        :return: none
        """
        company_label = tk.Label(self.top_frame, text="SALYTICS DASHBOARD", relief="groove", borderwidth=0,
                                 highlightthickness=0, bg=self.top_frame_color, fg=self.title_color)
        company_font = font.Font(size=25, weight="bold")
        company_label["font"] = company_font
        company_label.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="nsew")

        year_label = tk.Label(self.top_frame, text="YEAR", borderwidth=0, highlightthickness=0,
                              bg=self.top_frame_color, fg=self.title_color)
        quarter_label = tk.Label(self.top_frame, text="QUARTER", borderwidth=0, highlightthickness=0,
                                 bg=self.top_frame_color, fg=self.title_color)
        month_label = tk.Label(self.top_frame, text="MONTH", borderwidth=0, highlightthickness=0,
                               bg=self.top_frame_color, fg=self.title_color)
        label_font = font.Font(size=12, weight="bold")
        year_label["font"] = label_font
        quarter_label["font"] = label_font
        month_label["font"] = label_font
        year_label.grid(row=0, column=2, sticky="nsew")
        quarter_label.grid(row=0, column=3, sticky="nsew")
        month_label.grid(row=0, column=4, sticky="nsew")


    def top_frame_menus(self, years):
        """
        Creates and places year, quarter, and month, menus into the top frame

        :param years: the list of years present in the data
        :return: none
        """
        quarters = ["ALL", "Q1", "Q2", "Q3", "Q4"]
        months = ["ALL", "January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]

        self.year_menu = ttk.Combobox(self.top_frame, value=years, width=4, justify="center")
        self.year_menu.current(0)
        self.year_menu.bind("<<ComboboxSelected>>", self.controller.year_selected)
        self.year_menu.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

        self.quarter_menu = ttk.Combobox(self.top_frame, value=quarters, width=4, justify="center")
        self.quarter_menu.current(0)
        self.quarter_menu.bind("<<ComboboxSelected>>", self.controller.quarter_selected)
        self.quarter_menu.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

        self.month_menu = ttk.Combobox(self.top_frame, value=months, width=4, justify="center")
        self.month_menu.current(0)
        self.month_menu.bind("<<ComboboxSelected>>", self.controller.month_selected)
        self.month_menu.grid(row=1, column=4, padx=5, pady=5, sticky="nsew")


    def update_month_menu(self, months):
        """
        Updates the month menu to the display the correct months based on the quarter menu

        :param months: the months to be displayed
        :return: none
        """
        self.month_menu["values"] = months


    def _graph_buttons(self):
        """
        Creates and places the buttons for each of the initial graphs into frames q1_right-q4_right

        :return: none
        """
        self.left_button = tk.Menubutton(self.left_frame, text="Total Sales", height=1, padx=30, pady=30,
                                         bg=self.button_color)
        q1_button = tk.Menubutton(self.q1_right, text="Salesperson", height=1, bg=self.button_color)
        q2_button = tk.Menubutton(self.q2_right, text="Item", height=1, bg=self.button_color)
        q3_button = tk.Menubutton(self.q3_right, text="Category", height=1, bg=self.button_color)
        q4_button = tk.Menubutton(self.q4_right, text="Location", height=1, bg=self.button_color)

        self.view = tk.IntVar()
        self.explore = tk.IntVar()

        self.left_button.grid()
        self.left_button.menu = tk.Menu(self.left_button, tearoff=0)
        self.left_button["menu"] = self.left_button.menu
        self.left_button.menu.add_command(label="View", command=lambda: self.controller.view_selected("left"))

        q1_button.grid()
        q1_button.menu = tk.Menu(q1_button, tearoff=0)
        q1_button["menu"] = q1_button.menu
        q1_button.menu.add_checkbutton(label="Explore", variable=self.explore)

        q2_button.grid()
        q2_button.menu = tk.Menu(q2_button, tearoff=0)
        q2_button["menu"] = q2_button.menu
        q2_button.menu.add_command(label="Explore", command=lambda: self.explore_window("Item"))

        q3_button.grid()
        q3_button.menu = tk.Menu(q3_button, tearoff=0)
        q3_button["menu"] = q3_button.menu
        q3_button.menu.add_command(label="Explore", command=lambda: self.explore_window("Category"))
        q3_button.menu.add_command(label="View", command=lambda: self.controller.view_selected("q3"))

        q4_button.grid()
        q4_button.menu = tk.Menu(q4_button, tearoff=0)
        q4_button["menu"] = q4_button.menu
        q4_button.menu.add_checkbutton(label="Explore", command=lambda: self.explore_window("Location"))
        q4_button.menu.add_command(label="View", command=lambda: self.controller.view_selected("q4"))

        self.left_button.pack(fill="both")
        q1_button.pack(fill="both")
        q2_button.pack(fill="both")
        q3_button.pack(fill="both")
        q4_button.pack(fill="both")


    def init_left_plot(self, daily_revenue):
        """
        Creates and places the total sales graph into left_frame

        :param daily_revenue: the total revenue from each day
        :return: none
        """
        total = sum(daily_revenue)
        self.left_button["text"] = "Total Sales ($" + str(f'{total:,}') + ")"

        figure = Figure(figsize=(2, 1), dpi=100)
        plot = figure.add_subplot(1, 1, 1)
        plot.axis([0, len(daily_revenue), min(daily_revenue) - 5000, max(daily_revenue) + 5000])
        x = list(range(1, len(daily_revenue) + 1))
        y = daily_revenue.copy()
        plot.bar(x, y, width=1, color="dodgerblue")
        self.canvas_left = FigureCanvasTkAgg(figure, self.left_frame)
        self.canvas_left.get_tk_widget().pack(fill="both", expand=True)


    def init_q1_plot(self, er_frame):
        """
        Creates the and places the list of employees listbox into frame q1_right

        :param er_frame: a data-frame of employees and the revenue they've generated
        :return: none
        """
        self.employee_list = tk.Listbox(self.q1_right)
        self.employee_list.pack(fill="both", expand=True)
        er_list = er_frame.values.tolist()
        for x in range(len(er_frame)):
            item = str(x + 1) + ". " + str(er_list[x][0]) + " " + str(er_list[x][1]) + "   ($" \
                   + str(f'{er_list[x][2]:,}') + ")"
            self.employee_list.insert(tk.END, item)


    def init_q2_plot(self, item_frame):
        """
        Creates and places the list of items listbox into q2_right

        :param item_frame: a data-frame of items and the revenue they've generated
        :return: none
        """
        self.item_list = tk.Listbox(self.q2_right)
        self.item_list.pack(fill="both", expand=True)
        items_list = item_frame.values.tolist()
        for x in range(len(items_list)):
            item = str(x + 1) + ". " + str(items_list[x][0]) + "  ($" + str(f'{items_list[x][1]:,}') + ")"
            self.item_list.insert(tk.END, item)


    def init_q3_plot(self, category_names, category_revenue):
        """
        Creates and places the category graph into q3_right

        :param category_names: the names of the categories
        :param category_revenue: the revenue generated in each category
        :return: none
        """
        figure = Figure(figsize=(2, 1), dpi=100)
        plot = figure.add_subplot(1, 1, 1)
        x = [None] * len(category_names)
        for z in range(len(category_names)):
            x[z] = category_names[z][:3]
        y = category_revenue.copy()
        plot.bar(x, y, width=0.9, log=False, color=self.bar_color)
        self.canvas_q3 = FigureCanvasTkAgg(figure, self.q3_right)
        self.canvas_q3.get_tk_widget().pack(fill="both", expand=True)


    def init_q4_plot(self, locations, location_sales):
        """
        Creates and places the location graph into q4_right

        :param locations: the names of the locations
        :param location_sales: the revenue generated by each location
        :return: none
        """
        figure = Figure(figsize=(2, 1), dpi=100)
        plot = figure.add_subplot(1, 1, 1)
        plot.axis([-1, len(locations), min(location_sales) - 100000, max(location_sales) + 100000])
        x = locations
        y = location_sales
        plot.bar(x, y, width=0.9, log=False, color=self.bar_color)
        self.canvas_q4 = FigureCanvasTkAgg(figure, self.q4_right)
        self.canvas_q4.get_tk_widget().pack(fill="both", expand=True)


    def show_left_plot(self, daily_revenue, year, quarter, month):
        """
        Shows the total sales graph in a new window

        :param daily_revenue: the total revenue from each day
        :param year: the selected year from the year menu
        :param quarter: the selected quarter from the quarter menu
        :param month: the selected month from the month menu
        :return: none
        """
        title = "Total Sales \n (y=" + year + ", q=" + quarter + ", m=" + month + ")"
        ratio = 0.0
        if len(daily_revenue) < 32:
            ratio = 0.001
        elif len(daily_revenue) < 93:
            ratio = 0.003
        elif len(daily_revenue) < 366:
            ratio = 0.007
        else:
            ratio = 0.02

        x = list(range(1, len(daily_revenue) + 1))
        y = daily_revenue.copy()
        plt.figure(figsize=(7, 5), dpi=200)
        plt.subplot(131)
        plt.axes().set_aspect(ratio)
        plt.axis([0, len(daily_revenue), min(daily_revenue) - 5000, max(daily_revenue) + 5000])
        plt.bar(x, y, width=1, color=self.bar_color)
        plt.title(title)
        plt.xlabel("Time")
        plt.ylabel("Revenue ($" + str(f'{sum(daily_revenue):,}') + ")")
        plt.show()


    def human_format(self, num):
        """
        Reformats num for printing

        :param num: the number to be reformatted
        :return: the reformatted number
        """
        num = float('{:.2g}'.format(num))
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])


    def show_q3_plot(self, category_names, category_revenue):
        """
        Shows the category sales plot in a new window

        :param category_names: the names of the categories
        :param category_revenue: the revenue generated by each category
        :return: none
        """
        title = "Sales by Category"

        if max(category_revenue) > 8000000:
            ratio = 0.000001
        elif max(category_revenue) > 2500000:
            ratio = 0.000003
        elif max(category_revenue) > 500000:
            ratio = 0.00001
        elif max(category_revenue) > 20000:
            ratio = 0.00002

        x = [None] * len(category_names)
        for z in range(len(category_names)):
            x[z] = category_names[z][:3] + " \n " + str(self.human_format(category_revenue[z]))
        y = category_revenue
        plt.figure(figsize=(7, 5), dpi=200)
        plt.subplot(131)
        plt.axes().set_aspect(ratio)
        plt.axis([-1, len(category_names), min(category_revenue) - 100000, max(category_revenue) + 100000])
        plt.bar(x, y, width=0.9, color=self.bar_color)
        plt.title(title)
        plt.xlabel("Category Names")
        plt.ylabel("Revenue")
        plt.show()


    def show_q4_plot(self, locations, location_sales):
        """
        Shows the location sales graph in a new window

        :param locations: the names of the locations
        :param location_sales: the revenue generated by each location
        :return: none
        """
        if max(location_sales) > 8000000:
            ratio = 0.000001
        elif max(location_sales) > 2500000:
            ratio = 0.000003
        elif max(location_sales) > 500000:
            ratio = 0.00001
        elif max(location_sales) > 20000:
            ratio = 0.00002

        x = [None] * len(locations)
        for z in range(len(locations)):
            x[z] = locations[z][:3] + " \n " + str(self.human_format(location_sales[z]))
        y = location_sales
        plt.figure(figsize=(7, 5), dpi=200)
        plt.subplot(131)
        plt.axes().set_aspect(ratio)
        plt.axis([-1, len(locations), min(location_sales) - 100000, max(location_sales) + 100000])
        plt.bar(x, y, width=0.9, log=False, color=self.bar_color)
        plt.title("Sales by Location")
        plt.xlabel("Locations")
        plt.ylabel("Revenue")
        plt.show()


    def explore_window(self, exp):
        """
        Removes the main frame and replaces it with a blank frame

        :param exp: a value to indicate which graph the user wants to explore
        :return: none
        """
        self.main_frame.pack_forget()
        self.explore_frame = tk.LabelFrame(self)
        self.explore_frame.pack(fill="both", expand=True)
        self.controller.init_explore(exp)


    def exp_window_2(self, exp):
        self.explore_frame.pack_forget()
        #self.explore_frame.destroy()
        self.exp_frame_2 = tk.LabelFrame(self)
        self.exp_frame_2.pack(fill="both", expand=True)
        self.controller.init_exp_2(exp)


    def exp_base_frames(self, exp):
        """

        :param exp:
        :return:
        """
        self.exp_top_frame = tk.LabelFrame(self.explore_frame, padx=10, pady=10, bg=self.top_frame_color,
                                           highlightthickness=10, highlightbackground=self.highlight_color,
                                           highlightcolor=self.highlight_color, width=2300)

        if exp == "Category" or exp == "Location":
            self.exp_q1 = tk.LabelFrame(self.explore_frame, padx=10, pady=10, bg=self.bg_color,
                                        borderwidth=0, highlightthickness=0)
            self.exp_q2 = tk.LabelFrame(self.explore_frame, padx=10, pady=10, bg=self.bg_color,
                                        borderwidth=0, highlightthickness=0)
            self.exp_q3 = tk.LabelFrame(self.explore_frame, padx=10, pady=10, bg=self.bg_color,
                                        borderwidth=0, highlightthickness=0)
            self.exp_q4 = tk.LabelFrame(self.explore_frame, padx=10, pady=10, bg=self.bg_color,
                                        borderwidth=0, highlightthickness=0)
            self.exp_top_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
            self.exp_q1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
            self.exp_q2.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
            self.exp_q3.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
            self.exp_q4.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        elif exp == "Item":
            self.exp_q1 = tk.LabelFrame(self.explore_frame, padx=10, pady=10, bg=self.bg_color,
                                        borderwidth=0, highlightthickness=0)
            self.exp_q2 = tk.LabelFrame(self.explore_frame, padx=10, pady=10, bg=self.bg_color,
                                        borderwidth=0, highlightthickness=0)
            self.exp_q3 = tk.LabelFrame(self.explore_frame, padx=10, pady=10, bg=self.bg_color,
                                        borderwidth=0, highlightthickness=0)
            self.exp_top_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
            self.exp_q1.grid(row=1, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")
            self.exp_q2.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
            self.exp_q3.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")


    def exp_base_frames_2(self, exp):
        if exp == "Category/Location":
            self.exp_top_frame = tk.LabelFrame(self.exp_frame_2, padx=10, pady=10, bg=self.top_frame_color,
                                               highlightthickness=10, highlightbackground=self.highlight_color,
                                               highlightcolor=self.highlight_color, width=2300)
            self.exp_q1 = tk.LabelFrame(self.exp_frame_2, padx=10, pady=10, bg=self.bg_color,
                                        borderwidth=0, highlightthickness=0)
            self.exp_q2 = tk.LabelFrame(self.exp_frame_2, padx=10, pady=10, bg=self.bg_color,
                                        borderwidth=0, highlightthickness=0)
            self.exp_q3 = tk.LabelFrame(self.exp_frame_2, padx=10, pady=10, bg=self.bg_color,
                                        borderwidth=0, highlightthickness=0)
            self.exp_top_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
            self.exp_q1.grid(row=1, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")
            self.exp_q2.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
            self.exp_q3.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")



    def home_button(self, frame):
        self.home = tk.PhotoImage(file="home.png")
        home_button = tk.Button(frame, image=self.home, command=self.controller.refresh)
        home_button.pack(side=tk.LEFT, fill="y")



    def refresh(self):
        self.explore_frame.pack_forget()
        self.explore_frame.destroy()
        self.main_frame.pack(fill="both", expand=True)


    def explore_buttons(self, exp):
        self.view = tk.StringVar()
        self.explore = tk.StringVar()
        if exp == "Category":
            q1_button = tk.Menubutton(self.exp_q1, text="Salesperson", height=1, bg=self.button_color)
            q2_button = tk.Menubutton(self.exp_q2, text="Item", height=1, bg=self.button_color)
            q3_button = tk.Menubutton(self.exp_q3, text="Total Sales", height=1, bg=self.button_color)
            q4_button = tk.Menubutton(self.exp_q4, text="Location", height=1, bg=self.button_color)

            q1_button.grid()
            q1_button.menu = tk.Menu(q1_button, tearoff=0)
            q1_button["menu"] = q1_button.menu
            q1_button.menu.add_checkbutton(label="View", variable=self.view)

            q2_button.grid()
            q2_button.menu = tk.Menu(q2_button, tearoff=0)
            q2_button["menu"] = q2_button.menu
            q2_button.menu.add_checkbutton(label="Explore", variable=self.explore)

            q3_button.grid()
            q3_button.menu = tk.Menu(q3_button, tearoff=0)
            q3_button["menu"] = q3_button.menu
            q3_button.menu.add_checkbutton(label="Explore", variable=self.explore)
            q3_button.menu.add_command(label="View", command=lambda: self.controller.exp_view_selected("q3"))

            q4_button.grid()
            q4_button.menu = tk.Menu(q4_button, tearoff=0)
            q4_button["menu"] = q4_button.menu
            q4_button.menu.add_command(label="Explore", command=lambda: self.exp_window_2("Location"))
            q4_button.menu.add_command(label="View", command=lambda: self.controller.exp_view_selected("q4"))

            q1_button.pack(fill="both")
            q2_button.pack(fill="both")
            q3_button.pack(fill="both")
            q4_button.pack(fill="both")
        elif exp == "Location":
            q1_button = tk.Menubutton(self.exp_q1, text="Salesperson", height=1, bg=self.button_color)
            q2_button = tk.Menubutton(self.exp_q2, text="Item", height=1, bg=self.button_color)
            q3_button = tk.Menubutton(self.exp_q3, text="Total Sales", height=1, bg=self.button_color)
            q4_button = tk.Menubutton(self.exp_q4, text="Category", height=1, bg=self.button_color)

            q1_button.grid()
            q1_button.menu = tk.Menu(q1_button, tearoff=0)
            q1_button["menu"] = q1_button.menu
            q1_button.menu.add_checkbutton(label="View", variable=self.view)

            q2_button.grid()
            q2_button.menu = tk.Menu(q2_button, tearoff=0)
            q2_button["menu"] = q2_button.menu
            q2_button.menu.add_checkbutton(label="Explore", variable=self.explore)

            q3_button.grid()
            q3_button.menu = tk.Menu(q3_button, tearoff=0)
            q3_button["menu"] = q3_button.menu
            q3_button.menu.add_checkbutton(label="Explore", variable=self.explore)
            q3_button.menu.add_checkbutton(label="View", variable=self.view)

            q4_button.grid()
            q4_button.menu = tk.Menu(q4_button, tearoff=0)
            q4_button["menu"] = q4_button.menu
            q4_button.menu.add_checkbutton(label="Explore", variable=self.explore)
            q4_button.menu.add_checkbutton(label="View", variable=self.view)

            q1_button.pack(fill="both")
            q2_button.pack(fill="both")
            q3_button.pack(fill="both")
            q4_button.pack(fill="both")
        elif exp == "Item":
            q1_button = tk.Menubutton(self.exp_q1, text="Total Sales", height=1, bg=self.button_color)
            q2_button = tk.Menubutton(self.exp_q2, text="Salesperson", height=1, bg=self.button_color)
            q3_button = tk.Menubutton(self.exp_q3, text="Location", height=1, bg=self.button_color)

            q1_button.grid()
            q1_button.menu = tk.Menu(q1_button, tearoff=0)
            q1_button["menu"] = q1_button.menu
            q1_button.menu.add_checkbutton(label="View", variable=self.view)

            q2_button.grid()
            q2_button.menu = tk.Menu(q2_button, tearoff=0)
            q2_button["menu"] = q2_button.menu
            q2_button.menu.add_checkbutton(label="Explore", variable=self.explore)

            q3_button.grid()
            q3_button.menu = tk.Menu(q3_button, tearoff=0)
            q3_button["menu"] = q3_button.menu
            q3_button.menu.add_checkbutton(label="Explore", variable=self.explore)
            q3_button.menu.add_checkbutton(label="View", variable=self.view)

            q1_button.pack(fill="both")
            q2_button.pack(fill="both")
            q3_button.pack(fill="both")


    def exp_buttons_2(self, exp):
        if exp == "Category/Location":
            q1_button = tk.Menubutton(self.exp_q1, text="Total Sales", height=1, bg=self.button_color)
            q2_button = tk.Menubutton(self.exp_q2, text="Salesperson", height=1, bg=self.button_color)
            q3_button = tk.Menubutton(self.exp_q3, text="Location", height=1, bg=self.button_color)
            q1_button.pack(fill="both")
            q2_button.pack(fill="both")
            q3_button.pack(fill="both")


    def blank_graphs(self, exp):
        figure = Figure(figsize=(2, 1), dpi=100)
        plot = figure.add_subplot(1, 1, 1)

        self.canvas_q1_exp = FigureCanvasTkAgg(figure, self.exp_q1)
        self.canvas_q1_exp.get_tk_widget().pack(fill="both", expand=True)
        self.canvas_q2_exp = FigureCanvasTkAgg(figure, self.exp_q2)
        self.canvas_q2_exp.get_tk_widget().pack(fill="both", expand=True)
        self.employee_list_exp = FigureCanvasTkAgg(figure, self.exp_q3)
        self.employee_list_exp.get_tk_widget().pack(fill="both", expand=True)
        if exp == "Category" or exp == "Location":
            self.item_list_exp = FigureCanvasTkAgg(figure, self.exp_q4)
            self.item_list_exp.get_tk_widget().pack(fill="both", expand=True)


    def explore_time(self, year, quarter, month):
        month_label = tk.Label(self.exp_top_frame, text="   YEAR    \n" + year, relief="groove", borderwidth=0,
                               highlightthickness=0, bg=self.top_frame_color, fg=self.title_color)
        quarter_label = tk.Label(self.exp_top_frame, text="   QUARTER    \n" + quarter, relief="groove", borderwidth=0,
                                 highlightthickness=0, bg=self.top_frame_color, fg=self.title_color)
        year_label = tk.Label(self.exp_top_frame, text="   MONTH    \n" + month , relief="groove", borderwidth=0,
                              highlightthickness=0, bg=self.top_frame_color, fg=self.title_color)
        label_font = font.Font(size=15, weight="bold")
        month_label["font"] = label_font
        quarter_label["font"] = label_font
        year_label["font"] = label_font
        year_label.pack(side=tk.RIGHT)
        quarter_label.pack(side=tk.RIGHT)
        month_label.pack(side=tk.RIGHT)


    def explore_menu(self, exp, options):
        self.exp_menu = ttk.Combobox(self.exp_top_frame, value=options, width=4, justify="center")
        self.exp_menu.current(0)
        if exp == "Category":
            self.exp_menu.bind("<<ComboboxSelected>>", self.controller.category_selected)
            self.exp_menu.set("Select a category")
        elif exp == "Location":
            self.exp_menu.bind("<<ComboboxSelected>>", self.controller.location_selected)
            self.exp_menu.set("Select a location")
        elif exp == "Item":
            self.exp_menu.bind("<<ComboboxSelected>>", self.controller.item_selected)
            self.exp_menu.set("Select an item")

        self.exp_menu.pack(fill="both", expand=True)
        menu_font = font.Font(size=15)
        self.exp_menu["font"] = menu_font


    def init_cat_q3(self, daily_revenue):
        total = sum(daily_revenue)
        self.left_button["text"] = "Total Sales ($" + str(f'{total:,}') + ")"

        figure = Figure(figsize=(2, 1), dpi=100)
        plot = figure.add_subplot(1, 1, 1)
        plot.axis([0, len(daily_revenue), min(daily_revenue), max(daily_revenue)])
        x = list(range(1, len(daily_revenue) + 1))
        y = daily_revenue.copy()
        plot.bar(x, y, width=1, color="dodgerblue")
        if self.controller.model.explore == "Category" or self.controller.model.explore == "Location":
            self.canvas_q1_exp = FigureCanvasTkAgg(figure, self.exp_q3)
            self.canvas_q1_exp.get_tk_widget().pack(fill="both", expand=True)
        elif self.controller.model.explore == "Item":
            self.canvas_q1_exp = FigureCanvasTkAgg(figure, self.exp_q1)
            self.canvas_q1_exp.get_tk_widget().pack(fill="both", expand=True)


    def init_cat_q4(self, locations, location_sales):
        figure = Figure(figsize=(2, 1), dpi=100)
        plot = figure.add_subplot(1, 1, 1)
        plot.axis([-1, len(locations), min(location_sales) - 5000, max(location_sales) + 5000])
        x = locations
        y = location_sales
        plot.bar(x, y, width=0.9, log=False, color=self.bar_color)
        if self.controller.model.explore == "Category" or self.controller.model.explore == "Location":
            self.canvas_q2_exp = FigureCanvasTkAgg(figure, self.exp_q4)
            self.canvas_q2_exp.get_tk_widget().pack(fill="both", expand=True)
        elif self.controller.model.explore == "Item":
            self.canvas_q2_exp = FigureCanvasTkAgg(figure, self.exp_q3)
            self.canvas_q2_exp.get_tk_widget().pack(fill="both", expand=True)


    def init_cat_q1(self, er_frame):
        if self.controller.model.explore == "Category" or self.controller.model.explore == "Location":
            self.employee_list_exp = tk.Listbox(self.exp_q1)
        elif self.controller.model.explore == "Item":
            self.employee_list_exp = tk.Listbox(self.exp_q2)
        self.employee_list_exp.pack(fill="both", expand=True)
        er_list = er_frame.values.tolist()
        for x in range(len(er_frame)):
            item = str(x + 1) + ". " + str(er_list[x][0]) + " " + str(er_list[x][1]) + "   ($" \
                   + str(f'{er_list[x][2]:,}') + ")"
            self.employee_list_exp.insert(tk.END, item)


    def init_cat_q2(self, item_frame):
        self.item_list_exp = tk.Listbox(self.exp_q2)
        self.item_list_exp.pack(fill="both", expand=True)
        items_list = item_frame.values.tolist()
        for x in range(len(items_list)):
            if str(items_list[x][1]) != "0":
                item = str(x + 1) + ". " + str(items_list[x][0]) + "  ($" + str(f'{items_list[x][1]:,}') + ")"
                self.item_list_exp.insert(tk.END, item)



    def _set_weights(self):
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=7)

        self.top_frame.grid_columnconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(1, weight=1)
        self.top_frame.grid_columnconfigure(2, weight=1)
        self.top_frame.grid_columnconfigure(3, weight=1)
        self.top_frame.grid_columnconfigure(4, weight=1)
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_rowconfigure(1, weight=1)

        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(1, weight=1)
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_rowconfigure(2, weight=3)
        self.right_frame.grid_rowconfigure(3, weight=3)


    def cat_set_weights(self):
        self.explore_frame.grid_columnconfigure(0, weight=1)
        self.explore_frame.grid_columnconfigure(1, weight=1)
        self.explore_frame.grid_rowconfigure(0, weight=1)
        self.explore_frame.grid_rowconfigure(1, weight=100)
        self.explore_frame.grid_rowconfigure(2, weight=100)


    def exp_set_weights(self):
        self.exp_frame_2.grid_columnconfigure(0, weight=1)
        self.exp_frame_2.grid_columnconfigure(1, weight=1)
        self.exp_frame_2.grid_rowconfigure(0, weight=1)
        self.exp_frame_2.grid_rowconfigure(1, weight=100)
        self.exp_frame_2.grid_rowconfigure(2, weight=100)


    #def cat_set_weights_1(self):
    #    self.explore_frame.grid_columnconfigure(0, weight=1)
    #    self.explore_frame.grid_columnconfigure(1, weight=1)
    #    self.explore_frame.grid_rowconfigure(0, weight=1)
    #    self.explore_frame.grid_rowconfigure(1, weight=100)
    #    self.explore_frame.grid_rowconfigure(2, weight=50)
