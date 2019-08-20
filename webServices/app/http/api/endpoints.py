# from .middlewares import login_required
from flask import Flask, json, g, request
from app.stickynote.service import StickynoteService, PosttypeService
from app.stickynote.schema import PostdataSchema, PosttypeDataSchema
from flask_cors import CORS
from uuid import uuid4
# from ...repository.mongo_constants import *
#note

app = Flask(__name__)
CORS(app)

USER = 'name@example.com'

def json_response(payload, status=200):
    return (json.dumps(payload), status, {'content-type': 'application/json'})

def get_random_id():
    return uuid4().int & (1<<63)-1

@app.route("/stickynoteIndex", methods=["GET"])
def get_all_notes():
    return json_response(StickynoteService(USER).find_all_stickynotes())

@app.route("/stickynoteIndex", methods=["POST"])
def create_note():
    data = json.loads(request.data)
    data['note_id'] = get_random_id()
    postdata = PostdataSchema().load(data)
    if postdata.errors:
        return json_response({'error': postdata.errors}, 422)
    stickynote = StickynoteService(USER).create_stickynote_for(postdata)
    return json_response(stickynote)

@app.route("/stickynote/<int:note_id>", methods=["GET"])
def get_one_note(note_id):
    stickynote = StickynoteService(USER).find_stickynote(note_id)
    if not stickynote:
        return json_response({'error': 'stickynote not found'}, 404)
    return json_response(stickynote)

@app.route("/stickynote/<int:note_id>", methods=["PUT"])
def update_note(note_id):
   postdata  = PostdataSchema().load(json.loads(request.data))

   if postdata.errors:
       return json_response({'error': stickynote.errors}, 422)

   stickynote_found =  StickynoteService(USER).update_stickynote_with(note_id, postdata)
   if stickynote_found:
       return json_response(postdata.data)
   return json_response({'error': 'stickynote not found'}, 404)

@app.route("/stickynote/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    stickynote_found = StickynoteService(USER).delete_stickynote_for(note_id)
    if stickynote_found:
        return json_response({'note_id':note_id})
    return json_response({'error': 'stickynote not found'}, 404)

@app.route("/posttypeIndex", methods=["GET"])
def get_all_types():
    return json_response(PosttypeService(USER).find_all_posttypes())

@app.route("/posttypeIndex", methods=["POST"])
def create_type():
    data = json.loads(request.data)
    data['type_id'] = get_random_id()
    pt_data = PosttypeDataSchema().load(data)
    if pt_data.errors:
        return json_response({'error': pt_data.errors}, 422)
    posttype = PosttypeService(USER).create_posttype_for(pt_data)
    return json_response(posttype)

@app.route("/posttype/<int:type_id>", methods=["GET"])
def get_one_type(type_id):
    posttype = PosttypeService(USER).find_posttype(type_id)
    if not posttype:
        return json_response({'error': 'post type not found'}, 404)
    return json_response(posttype)
