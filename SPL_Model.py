import cv2
from PIL import Image, ImageTk


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
