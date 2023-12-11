import pynput
import tkinter as tk

# Fungsi untuk memperbarui koordinat yang ditampilkan
def update_coords(x, y):
    coords.config(text=f"({x}, {y})")
    coords.pack()

# Membuat window GUI
root = tk.Tk()
root.geometry("200x50")
root.overrideredirect(True)

# Menampilkan koordinat
coords = tk.Label(root)
coords.pack()

# Fungsi yang akan dijalankan setiap kali kursor dipindahkan
def on_move(x, y):
    update_coords(x, y)

# Membuat listener untuk mouse move event
listener = pynput.mouse.Listener(on_move=on_move)
listener.start()

# Menjalankan window GUI
root.mainloop()
