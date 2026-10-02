from win11toast import toast
from pathlib import Path

def NotifyUser(fp, imagePath="Images\\News.png"):
    """Displays a windows notification that the file has been created and lets me open it."""    
    image = {
    "src": str(Path(imagePath).resolve()),
    "placement": "hero"
    }
    
    toast("News Grabber Execution Completed", 
          f"A new daily news file has been created, click this notification to view the day's news!", 
          audio='ms-winsoundevent:Notification.Mail', 
          image=image,
          on_click=str(Path(fp).resolve()),
          duration="long")
    