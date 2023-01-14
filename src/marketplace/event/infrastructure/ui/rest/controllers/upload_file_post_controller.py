from typing import Tuple, Any

from flask import jsonify, request
from flask.views import View

from src.marketplace.event.application.command.upload.upload_file_command import UploadFileCommand
from src.shared.infrastructure.api_controller import ApiController


class UploadFilePostController(View, ApiController):
    methods = ["POST"]

    def dispatch_request(self) -> Tuple[Any, int]:
        """
        Upload file related events
        ---
        consumes:
            - multipart/form-data
        parameters:
          - name: body
            in: body
            required: true
            schema:
              id: Upload file
              required:
                - file
                - dztotalchunkcount
                - dzchunkbyteoffset
              properties:
                file:
                  type: file
                  description: The file to upload
                dztotalchunkcount:
                  type: number
                  description: Total chunk count
                dzchunkbyteoffset:
                  type: number
                  description: Total chunk offset
        responses:
          200:
            description: Empty json
          500:
            description: Unexpected error.
        """
        file = request.files["file"]
        total_chunk_count = int(request.form["dztotalchunkcount"])
        filename = file.filename

        start_bytes = None
        is_chunk = total_chunk_count > 1
        if is_chunk:
            start_bytes = int(request.form["dzchunkbyteoffset"])

        try:
            self.command_bus.dispatch(UploadFileCommand(file.stream.read(), filename, start_bytes, is_chunk))
            code = 200
            response = jsonify({})
        except Exception as e:
            code = 500
            response = jsonify({"data": None, "error": {"code": code, "message": str(e)}})

        return response, code
