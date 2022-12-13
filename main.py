from bottle import Bottle, run

app = Bottle()


@app.route('/')
def start():
    return "Welcome!!!"


if __name__ == '__main__':
    run(app, host='localhost', port=8080)
