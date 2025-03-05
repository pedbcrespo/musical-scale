from scale_engine import allNotes, findScale, seqTempo, generateScale, intersecNotesScales
from config import api
from flask_restful import Resource
from flask import request

# Request comes with standard: {notes: []}

class Initial(Resource):
    def get(self):
        return  {'init': 'Hello World'}

class FindScaleByNotes(Resource):
    def post(self):
        req = request.get_json()
        if not req or 'notes' not in req:
            return {'error': 'Invalid request, expected JSON with "notes"'}, 400
        res = findScale(seqTempo, allNotes, req['notes'])
        return {'notes': res[0]}

class GetScales(Resource):
    def get(self, note=None):
        if not note:
            return {'error': 'Note parameter is required'}, 400
        scales = [generateScale(allNotes, note, seq) for seq in seqTempo]
        return {'scales': scales}

class PostScales(Resource):
    def post(self):
        req = request.get_json()
        if not req or 'matrix' not in req:
            return {'error': 'Invalid request, expected JSON with "matrix"'}, 400
        res = intersecNotesScales(req['matrix'])
        return {'scale': res}



api.add_resource(Initial, "/")
api.add_resource(FindScaleByNotes, "/find")
api.add_resource(GetScales, "/scales/<note>")
api.add_resource(PostScales, "/scales-sequence")