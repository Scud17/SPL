import tkinter as tk


class SPL_View:

    root = tk.Tk()
    control_frame = tk.Frame(root)
    control_frame.pack(fill=tk.X, side=tk.BOTTOM)
    print("GUI initialized...")
    image_view = tk.Label(master=root)
    image_view.pack()
    # Controls
    scan_button = tk.Button(master=control_frame, text='Scan Lot', command=lambda: quit_(root, p))
    webApp_button = tk.Button(master=control_frame, text='Website', command=lambda: quit_(root, p))
    quit_button = tk.Button(master=control_frame, text='Quit', command=lambda: quit_(root, p))

    control_frame.columnconfigure(0, weight=1)
    control_frame.columnconfigure(1, weight=1)
    control_frame.columnconfigure(2, weight=1)

    scan_button.grid(row=0, column=0, sticky=tk.W + tk.E)
    webApp_button.grid(row=0, column=1, sticky=tk.W + tk.E)
    quit_button.grid(row=0, column=2, sticky=tk.W + tk.E)
    print("GUI image label initialized...")