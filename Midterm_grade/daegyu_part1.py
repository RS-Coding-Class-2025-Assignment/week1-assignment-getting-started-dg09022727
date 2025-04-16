import tkinter as tk
def convert_to_Fahrenheit():
    try:
        celsius = float(entry.get())
        fahrenheit = celsius * 9/5 + 32
        i=fahrenheit
        result_label.config(text=f"Result: {i}")
    except ValueError:
        return
root = tk.Tk()
root.title("celsius to fahrenheit")
root.geometry("400x200") 
lable_name=tk.Label(root, text="Enter celsius:")
lable_name.grid(row=0, column=0, padx=0, pady=5)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=5,pady=5) 
2
convert_button=tk.Button(root, text="Convert", command=convert_to_Fahrenheit)
convert_button.grid(row=1, column=1, padx=0, pady=10)

result_label = tk.Label(root, text="Result:___ °F")
result_label.grid(row=1, column=2, padx=0, pady=10) 

root.mainloop()





