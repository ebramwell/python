class Television:
    """Class representing a simple TV"""
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        """Initializes the TV with default settings"""
        self.status = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL
    def power(self):
        """Changes the power status of the TV"""
        self.status = not self.status
    def mute(self):
        """Mutes or unmutes the TV"""
        if self.status:
            self.muted = not self.muted
    def channel_up(self):
        """Changes the channel up"""
        if self.status:
            if self.channel < Television.MAX_CHANNEL:
                self.channel += 1
            else:
                self.channel = Television.MIN_CHANNEL
    def channel_down(self):
        """Changes the channel down"""
        if self.status:
            if self.channel > Television.MIN_CHANNEL:
                self.channel -= 1
            else:
                self.channel = Television.MAX_CHANNEL
    def volume_up(self):
        """Increases the volume"""
        if self.status and not self.muted:
            if self.volume < Television.MAX_VOLUME:
                self.volume += 1
    def volume_down(self):
        """Decreases the volume"""
        if self.status and not self.muted:
            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1
    def __str__(self):
        """Returns the status of the TV as a string"""
        if self.status:
            if self.muted:
                return f"Power = {self.status}, Channel = {self.channel}, Volume = Muted"
            else:
                return f"Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}"

