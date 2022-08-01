from countries import countries,link
import tkinter
import customtkinter
import requests

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{600}x{500}")
        self.title("Currency convertor")

        label = customtkinter.CTkLabel(master=self,
                                       text="Currency convertor",
                                       width=500,
                                       height=50,
                                       corner_radius=8, text_font=('Papyrus', 50))
        label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        def optionmenu_callback(choice):
            print("optionmenu dropdown clicked:", choice)

        combobox1 = customtkinter.CTkOptionMenu(master=self,
                                                values=countries,
                                                command=optionmenu_callback)
        combobox1.place(relx=0.4, rely=0.3, anchor=tkinter.CENTER)
        combobox1.set("USD")  # set initial value

        combobox2 = customtkinter.CTkOptionMenu(master=self,
                                                values=countries,
                                                command=optionmenu_callback)
        combobox2.place(relx=0.8, rely=0.3, anchor=tkinter.CENTER)
        combobox2.set("INR")  # set initial value

        entry = customtkinter.CTkEntry(master=self,
                                       placeholder_text="1",
                                       width=60,
                                       height=32)
        entry.place(relx=0.20, rely=0.3, anchor=tkinter.CENTER)

        def button_event():
            amount = tkinter.IntVar()
            country1 = tkinter.StringVar()
            country2 = tkinter.StringVar()
            amount = entry.get()
            print(amount)
            country1 = combobox1.get()
            country2 = combobox2.get()
            url = f"{link}/{country1}/{country2}/{amount}"
            result = requests.get(url).json()['conversion_result']
            text_var = f"{amount} {country1} = {result} {country2}"
            label1 = customtkinter.CTkLabel(master=self,
                                            text=text_var,
                                            width=120,
                                            height=25,
                                            text_color="#F4A355",
                                            corner_radius=8, text_font=('Didot', 20))
            label1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        button = customtkinter.CTkButton(master=self,
                                         width=120,
                                         height=32,
                                         border_width=0,
                                         corner_radius=8,
                                         text="Convert",
                                         command=button_event)
        button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
