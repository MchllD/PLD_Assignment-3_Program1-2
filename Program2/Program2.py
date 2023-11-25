import tkinter as tk
from PIL import Image, ImageTk

def calculate_fruits():
    try:
        money = float(entry_money.get())
        apple_price = float(entry_apple_price.get())
        orange_price = float(entry_orange_price.get())
        mango_price = float(entry_mango_price.get())

        max_apples = money // apple_price
        max_oranges = money // orange_price
        max_mangoes = money // mango_price

        remaining_money = money % min(apple_price, orange_price, mango_price)

        result_text = f"With ₱{money:.2f} you can buy:\n"
        result_text += f"{int(max_apples)} piece of apples, or {int(max_oranges)} piece of oranges, and or {int(max_mangoes)} piece of mangoes.\n"
        result_text += f"You will have ₱{remaining_money:.2f} remaining."

        result_label.config(text=result_text, fg="green")
    except ValueError:
        result_label.config(text="Please enter valid numbers for prices and money.", fg="red")

root = tk.Tk()
root.title("Michies Fruit Shop")
root.geometry("600x400")
root.configure(bg="#f8f7f9")


background_img = Image.open("beji.png")
background_photo = ImageTk.PhotoImage(background_img)
bg_label = tk.Label(root, image=background_photo)
bg_label.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg="#ddeeff", bd=2)
frame.place(relx=0.5, rely=0.5, anchor="center")

label_money = tk.Label(frame, text="Enter the amount of money:", bg="#ddeeff", font=("Arial", 12))
label_money.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_money = tk.Entry(frame, font=("Arial", 12))
entry_money.grid(row=0, column=1, padx=10, pady=5)

label_apple_price = tk.Label(frame, text="Enter the price of an apple:", bg="#ddeeff", font=("Arial", 12))
label_apple_price.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_apple_price = tk.Entry(frame, font=("Arial", 12))
entry_apple_price.grid(row=1, column=1, padx=10, pady=5)

label_orange_price = tk.Label(frame, text="Enter the price of an orange:", bg="#ddeeff", font=("Arial", 12))
label_orange_price.grid(row=2, column=0, padx=10, pady=5, sticky="w")

entry_orange_price = tk.Entry(frame, font=("Arial", 12))
entry_orange_price.grid(row=2, column=1, padx=10, pady=5)

label_mango_price = tk.Label(frame, text="Enter the price of a mango:", bg="#ddeeff", font=("Arial", 12))
label_mango_price.grid(row=3, column=0, padx=10, pady=5, sticky="w")

entry_mango_price = tk.Entry(frame, font=("Arial", 12))
entry_mango_price.grid(row=3, column=1, padx=10, pady=5)

calculate_button = tk.Button(frame, text="Calculate", command=calculate_fruits, bg="#ff9800", fg="white", font=("Arial", 12))
calculate_button.grid(row=4, columnspan=2, padx=10, pady=15)

result_label = tk.Label(frame, text="", bg="#ddeeff", font=("Arial", 12))
result_label.grid(row=5, columnspan=2, padx=10, pady=5)

root.mainloop()
