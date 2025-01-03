import customtkinter

from vistas.inicio import VistaInicio

root = customtkinter.CTk()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("theme.json")

VistaInicio(root)
root.mainloop()