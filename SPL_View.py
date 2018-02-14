import tkinter as tk
from multiprocessing import Process, Queue
import SPL_Model as model


def app_view(root):
    queue = Queue()
    print("queue initialized...")
    root = tk.Tk()
    control_frame = tk.Frame(root)
    control_frame.pack(fill=tk.X, side=tk.BOTTOM)
    print("GUI initialized...")
    image_view = tk.Label(master=root)
    image_view.pack()
    # Controls
    scan_button = tk.Button(master=control_frame, text='Scan Lot', command=lambda: model.quit_app(root, p))
    web_app_button = tk.Button(master=control_frame, text='Website', command=lambda: model.quit_app(root, p))
    quit_button = tk.Button(master=control_frame, text='Quit', command=lambda: model.quit_app(root, p))

    control_frame.columnconfigure(0, weight=1)
    control_frame.columnconfigure(1, weight=1)
    control_frame.columnconfigure(2, weight=1)

    scan_button.grid(row=0, column=0, sticky=tk.W + tk.E)
    web_app_button.grid(row=0, column=1, sticky=tk.W + tk.E)
    quit_button.grid(row=0, column=2, sticky=tk.W + tk.E)
    print("GUI image label initialized...")

    p = Process(target=model.image_capture, args=(queue,))
    p.start()
    print("image capture process has started...")
    # setup the update callback
    root.after(0, func=lambda: model.update_all(root, image_view, queue))
    print("root.after was called...")
    root.mainloop()
    print("mainloop exit")
    p.join()
    print("image capture process exit")

