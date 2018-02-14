from multiprocessing import Process, Queue
import cv2
from PIL import Image, ImageTk
import tkinter as tk


def quit_(root, process):
    process.terminate()
    root.destroy()


def update_image(image_view, queue):
    frame = queue.get()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    a = Image.fromarray(img)
    b = ImageTk.PhotoImage(image=a)
    image_view.configure(image=b)
    image_view._image_cache = b  # avoid garbage collection
    root.update()


def update_all(root, image_view, queue):
    update_image(image_view, queue)
    root.after(0, func=lambda: update_all(root, image_view, queue))


def image_capture(queue):
    cap = cv2.VideoCapture(0)
    while True:
        try:
            flag, frame = cap.read()
            if flag == 0:
                break
            queue.put(frame)
            cv2.waitKey(20)
        except:
            continue


if __name__ == '__main__':
    queue = Queue()
    print("queue initialized...")
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
    p = Process(target=image_capture, args=(queue,))
    p.start()
    print("image capture process has started...")
    # setup the update callback
    root.after(0, func=lambda: update_all(root, image_view, queue))
    print("root.after was called...")
    root.mainloop()
    print("mainloop exit")
    p.join()
    print("image capture process exit")