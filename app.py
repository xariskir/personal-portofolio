from flask import Flask, render_template, abort
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_projects():
    path = os.path.join(BASE_DIR, "data", "projects.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_education():
    path = os.path.join(BASE_DIR, "data", "education.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/education")
def education_page():
    data = load_education()
    return render_template(
        "education.html",
        education=data["education"],
        certifications=data["certifications"]
    )



@app.route("/projects")
def projects():
    projects = load_projects()
    return render_template("projects.html", projects=projects)


@app.route("/projects/<project_id>")
def project_detail(project_id):
    projects = load_projects()
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        abort(404)
    return render_template("project_detail.html", project=project)


@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

