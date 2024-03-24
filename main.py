from flask import Flask,render_template
import os


app = Flask(__name__,static_folder='static/assets')

class event:
    def __init__(self,name,inf,images):
        self.name = name
        self.info = inf
        self.images = images

events = [event('BIG PICTURE','Participants showcased creativity and sustainability prowess in crafting pictures using eco-friendly materials. The event, held on September 30, 2023, highlighted the fusion of artistry and environmental consciousness, setting a commendable example for sustainable practices. ','bigpicture.jpeg'),
event('STONE PAINTING','Participants demonstrated their artistic talents on stones, incorporating the theme of sustainable engineering. Held on September 30, 2023, the event showcased innovative interpretations of sustainability, merging artistry with environmental consciousness on a unique canvas.','WhatsApp Image 2024-03-24 at 10.41.08.jpeg'),
event('Relay Quiz','On September 30, 2023, a captivating Relay Quiz Challenge unfolded, featuring five participants from each class. Positioned on one side, participants dashed towards questions on the opposite end, solving them before passing the baton to their teammates, fostering teamwork and quick thinking amidst an exhilarating atmosphere.','WhatsApp Image 2024-03-24 at 10.29.34.jpeg'),
event('TREASURE HUNT','Participants embarked on an exciting Treasure Hunt on September 30, 2023. Armed with clues and a spirit of adventure, teams navigated through challenges, solving puzzles, and unraveling mysteries to discover hidden treasures. The event fostered teamwork, problem-solving skills, and an exhilarating sense of exploration among all involved.','WhatsApp Image 2024-03-23 at 08.37.19.jpeg'),
event('OPEN MIC','an engaging Daytime Open Mic Showcase unfolded, featuring a diverse array of talents. From poetry readings to musical performances, participants illuminated the stage with their creativity and passion. The event provided a welcoming platform for individuals to share their talents and connect with the community under the bright daylight.','WhatsApp Image 2024-03-24 at 10.32.02.jpeg')]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inaugration')
def inaugration():
    return render_template('404.html')

@app.route('/events')
def eve():
    return render_template('events.html',events=events)

@app.route('/contacts')
def ss():

    return render_template('contacts.html')

app.run(host='0.0.0.0',port=os.getenv("PORT", default=5000),debug=True)