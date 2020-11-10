from flask import Flask, jsonify, request
from flask_cors import CORS

import os
import psycopg2

DATABASE_URL = os.environ["DATABASE_URL"]

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
  return "Index page"

@app.route("/presets", methods=["GET"])
def get_presets():
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
  cur = conn.cursor()
  cur.execute("SELECT * FROM presets;")
  results = cur.fetchall()
  cur.close()
  conn.close()
  return "\n".join([" ".join([str(col) for col in result]) for result in results])

@app.route("/presets", methods=["POST"])
def add_presets():
  title = request.form.get("title")
  contents = request.form.get("contents")
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
  cur = conn.cursor()
  cur.execute("INSERT INTO presets (title, contents) VALUES (%s, %s);", (title, description))
  conn.commit()
  cur.close()
  conn.close()
  return f"added {title} {contents}"

@app.route("/custom", methods=["GET"])
def get_custom():
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
  cur = conn.cursor()
  cur.execute("SELECT * FROM custom;")
  results = cur.fetchall()
  cur.close()
  conn.close()
  return "\n".join([" ".join([str(col) for col in result]) for result in results])

@app.route("/custom", methods=["POST"])
def add_presets():
  title = request.form.get("title")
  contents = request.form.get("contents")
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
  cur = conn.cursor()
  cur.execute("INSERT INTO custom (title, contents) VALUES (%s, %s);", (title, description))
  conn.commit()
  cur.close()
  conn.close()
  return f"added {title} {contents}"
