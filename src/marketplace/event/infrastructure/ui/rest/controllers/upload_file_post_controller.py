from http import HTTPStatus
from typing import Tuple, Any

from flask import request
from flask.views import View

from src.marketplace.event.application.command.upload.upload_event_file_command import UploadEventFileCommand
from src.marketplace.event.domain.exceptions.file_already_exists_exception import FileAlreadyExistsException
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
              required:
                - id
                - event_id
                - file
                - dztotalchunkcount
                - dzchunkbyteoffset
              properties:
                id:
                  type: string
                  description: Event file id
                event_id:
                  type: string
                  description: Event id
                file:
                  type: file
                  description: The file to upload
                dztotalchunkcount:
                  type: number
                  description: Total chunk count
                dzchunkbyteoffset:
                  type: number
                  description: Total chunk offset
        response:
          201:
            description: Empty json
          400:
            description: Bad request
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
            self.command_bus.dispatch(
                UploadEventFileCommand(
                    request.form["id"], request.form["event_id"], file.stream.read(), filename, start_bytes, is_chunk
                )
            )
            response = {}, HTTPStatus.CREATED
        except FileAlreadyExistsException as e:
            response = {
                "error": {"code": "FILE_ALREADY_EXISTS", "message": str(e)},
                "data": None,
            }, HTTPStatus.BAD_REQUEST

        return response
