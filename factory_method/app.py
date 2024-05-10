from flask import Flask, request, url_for, render_template



"""Homepage"""



if __name__ == "__main__":
    app = Flask(__name__, template_folder="templates", static_folder="static")
    @app.route('/')
    def root():
        return render_template(
            'index.html'
    )
    @app.route('/about/')
    def about_method():
        return render_template(
            'about.html'
    )
    app.run(debug=True)