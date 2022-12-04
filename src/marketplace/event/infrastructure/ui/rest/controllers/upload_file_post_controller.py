from typing import Tuple, Any

from flask import jsonify, request
from flask.views import View

from src.marketplace.event.application.command.upload.upload_file_command import UploadFileCommand
from src.shared.infrastructure.api_controller import ApiController


class UploadFilePostController(View, ApiController):
    methods = ["POST"]

    def dispatch_request(self) -> Tuple[Any, int]:
        file = request.files["file"]
        total_chunk_count = int(request.form["dztotalchunkcount"])
        filename = file.filename

        start_bytes = None
        is_chunk = total_chunk_count > 1
        if is_chunk:
            start_bytes = int(request.form["dzchunkbyteoffset"])

        self.command_bus.dispatch(UploadFileCommand(file.stream.read(), filename, start_bytes, is_chunk))

        return jsonify({}), 200
