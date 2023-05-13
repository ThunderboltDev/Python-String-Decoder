import tkinter as tk
from tkinter import messagebox

def decode_string():
    encoded_str = entry.get()
    
    encoded_bytes = bytes(encoded_str, 'utf-8')
    
    decoded_str = encoded_bytes.decode('unicode_escape')
    with open("Decoded String.txt", "w")as f:
        f.write(f"THUNDER STRING DEOBFUSCATOR\n\n{decoded_str}")
        messagebox.showinfo("Success", f"Success! The string has been encoded! \nDecoded String: {decoded_str} \n")
    
    label.config(text=decoded_str)

window = tk.Tk()
window.title("String Decoder")

input_label = tk.Label(window, text="Enter the encoded string:")
input_label.pack()

entry = tk.Entry(window)
entry.pack()

decode_button = tk.Button(window, text="Decode", command=decode_string)
decode_button.pack()

output_label = tk.Label(window, text="Decoded string:")
output_label.pack()

label = tk.Label(window, text="")
label.pack()

-window.mainloop()
