from scale_engine import allNotes, findScale, seqTempo, generateScale, intersecNotesScales
from config import api
from flask_restful import Resource
from flask import request

# Request comes with standard: {notes: []}

class Initial(Resource):
    def get(self):
        return  {'init': 'Hello World',
                'endpoints':[
                    {'link': '/find', 'description': 'Find scales wich contains the notes passed as param', 
                     'param': "list of notes", 
                     'example': { 'notes': ['C', 'E', 'G']}},
                    {'link': '/scales/<note>', 'description': 'Show all the scales with the note passed', 'param': "note", 'example': 'C'},
                    {'link': '/scales-sequence', 
                     'description': 'Return a scale based on a matrix that consist in a group of diferent scales. The scale contains the notes in comun with the scales on the matrix.', 
                     'param': "matrix of scales", 
                     'example': {
	                    "matrix":  [
	                        ["D", "E", "F#", "G", "A", "B", "C#"],
	                        ["B", "C#", "D", "E", "F#", "G", "A"],
	                        ["E", "F#", "G", "A", "B", "C", "D"],
	                        ["A", "B", "C#", "D", "E", "F#", "G#"]
                        ]}
                    },
                ]}

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