import Grabbing as Grb
import datetime
import Notifications as NT
from jinja2 import Environment, FileSystemLoader


# Run the thing
if __name__ == '__main__':
    #initialize stuff
    fp = f"Papers/{datetime.date.today()}.html"
    Stories = []
    
    #Jinja template nonsense
    environment = Environment(loader=FileSystemLoader("Templates/"))
    template = environment.get_template("NewsLetterTemplate.html.jinja")

    #Load endoints
    EPs = Grb.LoadEndpoints("Endpoints.json")

    #Get Stories
    for [Key, value] in EPs.items():
                print(f"Grabbing {Key}")
                IDs = Grb.GetStoryIDs(value)
                for ID in IDs:
                    S = Grb.GetStory(ID)
                    if S:
                        Stories.append(S)
                    
    #Render template
    Text = template.render({"Stories":Stories,
                            "Date":datetime.date.today()})

    #Write file
    with open(fp, "w", encoding="utf-8") as f:
        f.write(Text)
        

    print(f"\nnews file created at {fp}")

    #Send windows notification to user
    NT.NotifyUser(fp)
