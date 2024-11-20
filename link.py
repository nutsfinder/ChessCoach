import chess
import chess.engine


def parse_board(custom_board: str) -> str:
    """
    Convert custom board format to FEN.
    """
    rows = custom_board.splitlines()
    fen_rows = []
    for row in rows:
        fen_row = ""
        empty = 0
        for char in row:
            if char == ".":
                empty += 1
            else:
                if empty > 0:
                    fen_row += str(empty)
                    empty = 0
                fen_row += char
        if empty > 0:
            fen_row += str(empty)
        fen_rows.append(fen_row)
    return "/".join(fen_rows) + " w - - 0 1"  # Default turn, no castling info


def get_best_move(fen: str) -> str:
    """
    Get the best move from a given FEN using a chess engine.
    """
    board = chess.Board(fen)
    engine_path = "/path/to/stockfish"  # Replace with the actual path to the engine

    with chess.engine.SimpleEngine.popen_uci(engine_path) as engine:
        # Configure a time limit for the engine to calculate
        result = engine.play(board, chess.engine.Limit(time=1))  # Adjust time as needed
        move = result.move
        piece = board.piece_at(move.from_square)

        from_square = chess.square_name(move.from_square)
        to_square = chess.square_name(move.to_square)

        return f"Move {piece.symbol().upper()} from {from_square} to {to_square}"


custom_board = """
. K R . . R . .
P . P P Q . . P
. P B B . . . .
. . . . . P . .
. . b . . p . q
. p . . . . . .
p b p p . . . p
. k r . . . r .
"""

fen = parse_board(custom_board.strip())
print("FEN:", fen)

move_description = get_best_move(fen)
print("Best Move:", move_description)