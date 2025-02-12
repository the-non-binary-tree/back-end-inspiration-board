from flask import Blueprint, jsonify, make_response, request, abort
from flask.helpers import make_response
from app.models.board import Board
from app import db
from app.common_functions.check_request_body import check_request_body
from app.common_functions.check_for_id import get_id
from app.models.board import Board

board_bp = Blueprint("board", __name__, url_prefix="/boards")

# CREATE A BOARD
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

# READ ALL BOARDS
@board_bp.route("", methods=["GET"])
def get_all_boards():
    boards = Board.query.all()

    board_response = []
    for board in boards:
        board_response.append(
            board.to_dict()
        )
    
    return make_response(jsonify(board_response), 200)

# READ ALL CARDS BY BOARD
@board_bp.route("/<board_id>/cards", methods=["GET"])
def get_cards_by_board_id(board_id):
    board = get_id(board_id, Board, str_repr="Board")
    return make_response(jsonify(board.to_dict_with_cards()), 200)

