from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           tours=data.tours,
                           title=data.title,
                           subtitle=data.subtitle,
                           description=data.description,
                           departures=data.departures)


@app.route('/departures/<dep>')
def departures(dep):
    count = 0
    pr = []
    nit = []
    for i in data.tours.values():
        if i['departure'] == dep:
            pr.append(i['price'])
            nit.append(i['nights'])
            count += 1
    len_tours = len(data.tours)
    return render_template('departure.html',
                           tours=data.tours,
                           title=data.title,
                           subtitle=data.subtitle,
                           description=data.description,
                           departures=data.departures[dep],
                           cnt=str(count),
                           ot=min(pr),
                           do=max(pr),
                           n_min=min(nit),
                           n_max=max(nit),
                           len=len_tours,
                           dep=dep)


@app.route('/tours/<tour>')
def tours(tour):
    for i in data.tours.values():
        if i['title'] == tour:
            star = i['stars']
            pic = i['picture']
            nights = i['nights']
            country = i['country']
            dep = data.departures[i['departure']]
            desc = i['description']
            price = i['price']
        else:
            continue
    return render_template('tour.html',
                           tours=data.tours,
                           title=data.title,
                           subtitle=data.subtitle,
                           description=data.description,
                           tour=tour,
                           star=star,
                           pic=pic,
                           nights=nights,
                           country=country,
                           dep=dep,
                           desc=desc,
                           price=price)


if __name__ == '__main__':
    app.run()
