import cv2
import json
import logging
import pytesseract
import numpy as np
import pandas as pd
from io import StringIO
from typing import Optional
from resources import definitions as defn


class OCRPipeline(object):
    """
    OCRPipeline constructor takes an image as a BytesIO<bytes> buffered object
    initialized:
        - self.image
        - self.output_type
    runtime instantiated/assigned
        - self.ocr_result_tsv
        - self.ocr_result_string
        - self.output_response_json
        - ocr_document
    class functions:
        - apply_ocr() -> None
        - apply_preprocess_pipe() -> None
        - write_message() -> None
    """
    image: Optional[bytes]
    output_type: Optional[str]
    ocr_result_string: Optional[str]
    ocr_result_tsv: Optional[pd.DataFrame]
    ocr_document: Optional[dict]
    output_response_json: Optional[dict]

    def __init__(self, image: bytes, output_type: str) -> None:
        self.image = cv2.imdecode(np.frombuffer(image,dtype=np.uint8),1)
        self.output_type = output_type
        self.ocr_result_tsv = None
        self.ocr_result_string = None
        self.output_response_json = None
        self.ocr_document = None
    
    def apply_preprocess_pipe(self,preprocess_args: [] = None) -> None:
        pass
    

    def apply_ocr(self,ocr_config_options: str = defn.DEFAULT_TESSERACT_CONFIG) -> None:
        """
        OCRPipelinefunction.apply_ocr()

        """
        if self.output_type == 'tsv':
            tmp_results = pytesseract.image_to_data(image=self.image, config=ocr_config_options)
            try:
                tmp_results = pd.read_csv(StringIO(tmp_results), sep='\t', header=0)
            except pd.errors.ParserError:
                tmp_results = pd.read_csv(StringIO(tmp_results), sep='\t', header=0, engine="python", error_bad_lines=False)
            
            self.ocr_result_tsv = tmp_results
            self.ocr_document = json.loads(self.ocr_result_tsv.to_json(orient='records'))

        elif self.output_type == 'string':
            tmp_results = pytesseract.image_to_string(image=self.image, config=ocr_config_options)
            self.ocr_result_string = tmp_results
            self.ocr_document = self.ocr_result_string


    

    def write_message(self) -> None:
        pass