from pynput import mouse

# Small script to get designated number (mouse clicks) of cords on screen

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        return False

num_of_clicks = 3
for _ in range(num_of_clicks):
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
