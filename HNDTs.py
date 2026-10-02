import datetime

class Story:
    """A single story from the hacker news website"""
    def __init__(self, Title, Url, Author, Score, CreationTime):
        self.Title = Title
        self.Url = Url
        self.Author = Author
        self.Score = Score
        self.CreationTime = datetime.datetime.fromtimestamp(CreationTime).strftime("%d/%m/%Y, %H:%M:%S")

    def PrintStory(self):
        """Prints the attributes of a story type object to the console"""
        print(f"\n**{self.Title}**")
        print(f"Created: \t{self.CreationTime}")
        print(f"Posted by: \t{self.Author}")
        print(f"Point score: \t{self.Score}")
        print(f"URL: \t\t{self.Url}\n")

    def ToString(self):
        """Converts a story's attributes to a single string"""
        return f"\n**{self.Title}**\nCreated:\t{self.CreationTime}\nPosted by:\t{self.Author}\nPoint score:\t{self.Score}\nURL:\t\t{self.Url}\n"
    