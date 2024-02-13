from Render_image import Image

class Button(Image):
    def __init__(self, canvas, x, y, image_path, command):
        """
        Initializes a Button object.

        Args:
            canvas (Canvas): The canvas on which the button will be drawn.
            x (int): The x-coordinate of the button's position.
            y (int): The y-coordinate of the button's position.
            image_path (str): The path to the image file for the button.
            command (function): The function to be executed when the button is clicked.
        """
        Image.__init__(self, canvas, x, y, image_path)  
        self.command = command


    def on_button_click(self, event):
        """
        Calls the command associated with the button.

        Args:
            event (Event): The event object passed to the callback function.
        """
        self.command()
        print("Button clicked")

    def bind(self, event, callback):
        """
        Binds an event to the button.

        Args:
            event (str): The event to bind (e.g., "<Button-1>" for left mouse button click).
            callback (function): The function to be called when the event occurs.
        """
        self.canvas.tag_bind(self.image_id, event, callback)

    def delete(self):
        """
        Deletes the button from the canvas.
        """
        Image.delete(self)  

    def get_position(self):
        """
        Returns the position of the button.

        Returns:
            tuple: The x and y coordinates of the button's position.
        """
        return Image.get_position(self) 

    def get_size(self):
        """
        Returns the size of the button.

        Returns:
            tuple: The width and height of the button.
        """
        return Image.get_size(self)
