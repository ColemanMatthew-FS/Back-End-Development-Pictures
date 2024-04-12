from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))

######################################################################
# RETURN HEALTH OF THE APP
######################################################################


@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################


@app.route("/count")
def count():
    """return length of data"""
    if data:
        return jsonify(length=len(data)), 200

    return {"message": "Internal server error"}, 500


######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    if data:
        return jsonify(data)
    return {"message": "data not found"}, 404

######################################################################
# GET A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    if data:
        for picture in data:
            if picture["id"] == id:
                return picture
    return {"message": "picture not found"}, 404


######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    req = request.json
    if not req:
        return {"message": "Invalid input parameter"}, 422
    
    try:
        for picture in data:
            if picture["id"] == req["id"]:
                return {"Message": f"picture with id {req['id']} already present"}, 302
        data.append(req)
    except NameError:
        return {"message": "data not defined"}, 500
    return req, 201

######################################################################
# UPDATE A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    req = request.json
    if not req:
        return {"message": "Invalid input parameter"}, 422
    try:
        #i have to enumerate here
        #if i perform an operation on the picture itself
        #id est, "picture = req",
        #it doesnt get written to the data list
        #i need to modify by index
        for index, picture in enumerate(data):
            if picture["id"] == req["id"]:
                data[index] = req
                return picture, 200
        return {"message": "picture not found"}, 404
    except NameError:
        return {"message": "data not defined"}, 500
    

######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    try:
        for picture in data:
            if picture["id"] == id:
                data.remove(picture)
                return {}, 204
        return {"message": "picture not found"}, 404
    except NameError:
        return {"message": "data not defined"}, 500
