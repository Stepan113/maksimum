import webbrowser


class Spamer:
    def __init__(self):
        self.url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    def brauser(self):
        # pos = 0
        while True:
            webbrowser.open(self.url, new=2)
            # pos += 1

# c=Spamer()
# c.brauser()
