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
  if "id" in request.args:
    cur.execute("SELECT * FROM presets where id=%s;", (request.args.get("id"),))
  else:
    cur.execute("SELECT * FROM presets;")
  results = cur.fetchall()
  cur.close()
  conn.close()
  lists = [{"id": r[0], "title": r[1], "contents": r[2]} for r in results]
  return jsonify(lists)

@app.route("/presets", methods=["POST"])
def add_presets():
  title = request.form.get("title")
  contents = request.form.get("contents")
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
  cur = conn.cursor()
  cur.execute("INSERT INTO presets (title, contents) VALUES (%s, %s) RETURNING id;", (title, contents))
  id = cur.fetchone()[0]
  conn.commit()
  cur.close()
  conn.close()
  return jsonify({"id": id, "title": title, "contents": contents})

@app.route("/custom", methods=["GET"])
def get_custom():
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
  cur = conn.cursor()
  if "id" in request.args:
    cur.execute("SELECT * FROM custom where id=%s;", (request.args.get("id"),))
  else:
    cur.execute("SELECT * FROM custom;")
  results = cur.fetchall()
  cur.close()
  conn.close()
  lists = [{"id": r[0], "title": r[1], "contents": r[2]} for r in results]
  return jsonify(lists)

@app.route("/custom", methods=["POST"])
def add_custom():
  title = request.form.get("title")
  contents = request.form.get("contents")
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
  cur = conn.cursor()
  cur.execute("INSERT INTO custom (title, contents) VALUES (%s, %s) RETURNING id;", (title, contents))
  id = cur.fetchone()[0]
  conn.commit()
  cur.close()
  conn.close()
  return jsonify({"id": id, "title": title, "contents": contents})
