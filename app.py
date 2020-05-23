from flask import Flask, render_template, request
import json
app = Flask(__name__)


@app.route('/')
def get():
    with open('db.json') as f:
        movies = json.load(f)
    return render_template('index.html', movies=movies)


@app.route('/hello')
def hello():
    with open('db.json') as f:
        movies = json.load(f)
    theatres = {}
    for movie in movies:
        theatre = movie['theatre']
        if theatre not in theatres:
            theatres[theatre] = []
        theatres[theatre].append(
            {
                'name': movie['name'],
                'time': movie['time']
            }
        )
    return render_template("hello.html",  theatres=theatres)


@app.route('/cinema/<cinema_id>')
def cinema(cinema_id):
    with open('db.json') as f:
        movies = json.load(f)
    with open('theatres.json') as f:
        theatres = json.load(f)
        theatre = theatres[cinema_id]
        result = [movie for movie in movies if movie["theatre"] == theatre]
        # result = []
        # for movie in movies:
        #     if movie["theatre"] == theatre:
        #         result.append(movie)
    return render_template("cinema.html", theatre=theatre, movies=result)


schedule = {
    "Bekmambetov cinema":
    [
        {
            "name": "Девятое",
            "time": "11:40"
        }
    ]
}
@app.route('/hell')
def hell():
    with open('theatres.json') as f:
        theatres = json.load(f)
        theatre_to_id = {}
    for theatre_id, name in theatres.items():
        theatre_to_id[name] = theatre_id
    with open('db.json') as f:
        movies = json.load(f)
    schedule = {}
    for movie in movies:
        theatre = movie['theatre']
        if theatre not in schedule:
            schedule[theatre] = {
                "movies": [],
                "id": theatre_to_id[theatre]
            }
        schedule[theatre]['movies'].append(
            {
                'name': movie['name'],
                'time': movie['time']
            }
        )
    return render_template("hell.html", schedule=schedule)


@app.route('/cinemaa')
def open_cinema():
    with open('db.json') as f:
        movies = json.load(f)
    return render_template("cinema_incl.html")


@app.route('/movies/')
def movie():
    name = request.args.get('name')
    with open('db.json') as f:
        movies = json.load(f)
        movies = [movie for movie in movies if movie['name'] == name]
    return render_template("movies.html", name=name, movies=movies)
