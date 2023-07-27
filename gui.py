import customtkinter as ctk
import main


def call_download():
    main.download()



ctk.set_appearance_mode("System")  # theme select as system settings
ctk.set_default_color_theme("green")  # colour to green

root = ctk.CTk()
root.geometry('500x200')  # Width x Height

frame = ctk.CTkFrame(master=root)
frame.pack(padx=60, fill='both', expand=True)

topic = ctk.CTkLabel(master=frame, text='Enter The Link', font=('Roboto', 30))
topic.pack(pady=12, padx=10)

link_area = ctk.CTkEntry(master=frame, placeholder_text='Paste the Link here')
link_area.pack(pady=12, padx=10)

download_button = ctk.CTkButton(master=frame, text='Download', command=call_download())
download_button.pack(pady=12, padx=10)

root.mainloop()
