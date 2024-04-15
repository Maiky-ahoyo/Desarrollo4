from flask import Flask

app = Flask(__name__)
@app.route('/') #home
def index():
    return '''
            <html>
                <head>
                    <title>HELLO</title>
                </head>
                <body>
                    <h1>Hello, World!</h1>
                    <a href="/about">
                    About</a>
                </body>
            </html>
            '''
@app.route('/about') #about
def about():
    return '''
            <html>
                <head>
                    <title>ABOUT</title>
                </head>
                <body>
                    <h1>About</h1>
                    <p>Everything about Hello World!</p>
                    Back to <a href="/">Hello World</a>
                </body>
            </html>
            '''

if __name__ == '__main__':
    app.run(debug=True)