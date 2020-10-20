import application
import flask

@application.app.route("/login", methods=["GET","POST"])
def login():
    if flask.request.method == "GET":
        if "username" in flask.request.cookies:
            return flask.render_template("cpanel.html", title="Welcome Back!", name=flask.request.cookies["username"])
        else:
            return flask.render_template("form.html", title="Login Now!")
    else:
        response = application.app.make_response(flask.redirect("/login"))
        response.set_cookie("username", value=flask.request.form["username"])
        return response

@application.app.route("/logout")
def logout():
    response = application.app.make_response(flask.redirect("/login"))
    response.set_cookie("username", expires=0)
    return response