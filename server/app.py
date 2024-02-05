from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin


app = Flask(__name__)
# Followed https://flask-cors.readthedocs.io/en/3.0.7/
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

username = "user"
password = "password"
database = "images"
hostname = "db"

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"mysql+pymysql://{username}:{password}@{hostname}/{database}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), unique=True, nullable=False)
    thumbs_up = db.Column(db.Integer, default=0)
    thumbs_down = db.Column(db.Integer, default=0)


@app.route("/api/images", methods=["GET"])
def get_images():
    page = request.args.get("page", 1, type=int)
    PER_PAGE = 25
    images = Image.query.paginate(page=page, per_page=PER_PAGE)
    data = [
        {
            "id": image.id,
            "url": image.url,
            "thumbs_up": image.thumbs_up,
            "thumbs_down": image.thumbs_down,
        }
        for image in images.items
    ]
    return jsonify(data)

@app.route("/api/react", methods=["POST"])
def react_to_image():
    data = request.json
    image_id = data.get("image_id")
    thumbs_up = data.get("thumbs_up")
    thumbs_down = data.get("thumbs_down")

    # Followed https://stackoverflow.com/questions/6699360/flask-sqlalchemy-update-a-rows-information
    image = db.session.query(Image).get(image_id)
    image.thumbs_up = thumbs_up
    image.thumbs_down = thumbs_down
    db.session.commit()

    return jsonify({'message': 'Reaction recorded successfully'}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5015)


