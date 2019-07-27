import connexion
from io import BytesIO
from typing import Optional
from flask import Flask, jsonify, make_response, send_file

from resources import definitions as defn
from ocr.ocr import OCRPipeline


def response_builder(status_code: int, **kwargs):
    return make_response(jsonify(kwargs), status_code)

def ocr_to_data_handler() -> make_response:
    document = connexion.request.files['document']
    output_type = connexion.request.args['output_type']
    if not defn.valid_mimetype(document):
        return response_builder(415,
            error='Unsupported Media Type',
            expected_filetype='image/png',
            received_filetype=str(document.mimetype))
    with BytesIO() as input_stream:
                document.save(input_stream)
                buffer_document = input_stream.getvalue()
    ocr_cli = OCRPipeline(buffer_document, output_type)
    ocr_cli.apply_ocr()
    print(ocr_cli.__dict__)
    return make_response(jsonify({'message': 'hello from your application!'}), 200)

