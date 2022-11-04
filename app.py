import json
from flask import Flask, request, jsonify
import os
from services.PdfService import PdfService

app = Flask(__name__)

@app.route('/v1/api/pdf/rotate', methods=["POST"])
def index():
    try: 
        # make sure angle of rotation is provided in request body
        angle_of_rotation = request.get_json().get("angle_of_rotation")
        if(angle_of_rotation is None):
            raise Exception("angle_of_rotation is required")
        
        # make sure page_number is provided in request body
        page_number = request.get_json().get("page_number")
        if(page_number is None):
            raise Exception("page_number is required")
        
        # get upload file from request
        file_path = request.get_json().get("file_path")
        if(file_path is None):
            raise Exception("file_path is required")
        
        # rotate pdf
        PdfService.rotate_page_in_pdf(file_path, page_number, angle_of_rotation)
        
        return jsonify({
            "status": "success"
        }), 200
        
    except Exception as e:
        return jsonify({
                "status": "error",
                "message": str(e)
            }), 400

if __name__ == '__main__':
    app.debug = True
    app.run() #go to http://localhost:5000/ to view the page.