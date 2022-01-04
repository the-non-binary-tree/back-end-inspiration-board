from flask import Blueprint, jsonify, make_response, request, abort
from flask.helpers import make_response
from app.models.board import Board
from app import db
from app.common_functions.check_request_body import check_request_body

board_bp = Blueprint("board", __name__, url_prefix="/boards")

@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()

    request_body_parameters = ["title", "owner"]
    check_request_body(request_body_parameters)

    new_board = Board(
        title = request_body["title"],
        owner = request_body["owner"]
    )

    db.session.add(new_board)
    db.session.commit()

    return make_response(new_board.to_dict(),200)

