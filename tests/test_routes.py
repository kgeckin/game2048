"""Basic Flask game session tests."""

import app as game


def test_home_starts_game():
    game.app.config["TESTING"] = True
    with game.app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        with client.session_transaction() as session:
            assert len(session["mat"]) == 4
            assert session["score"] == 0


def test_state_changing_routes_reject_get():
    with game.app.test_client() as client:
        assert client.get("/reset").status_code == 405
        assert client.get("/undo").status_code == 405


def test_reset_uses_post_and_preserves_best():
    with game.app.test_client() as client:
        with client.session_transaction() as session:
            session["mat"] = [[4, 0, 0, 0]] + [[0] * 4 for _ in range(3)]
            session["score"] = 4
            session["best"] = 128
        response = client.post("/reset")
        assert response.status_code == 302
        client.get("/")
        with client.session_transaction() as session:
            assert session["score"] == 0
            assert session["best"] == 128


def test_move_and_undo_restore_score():
    with game.app.test_client() as client:
        with client.session_transaction() as session:
            session["mat"] = [
                [2, 2, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
            session["score"] = 0
            session["best"] = 0
        response = client.post("/move", data={"direction": "a"})
        assert response.status_code == 302
        with client.session_transaction() as session:
            assert session["score"] == 4
            assert session["best"] == 4
        assert client.post("/undo").status_code == 302
        with client.session_transaction() as session:
            assert session["score"] == 0


def test_unknown_direction_does_not_mutate_state():
    with game.app.test_client() as client:
        client.get("/")
        with client.session_transaction() as session:
            before = list(map(list, session["mat"]))
        client.post("/move", data={"direction": "invalid"})
        with client.session_transaction() as session:
            assert session["mat"] == before
