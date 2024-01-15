from wsgi import app 


def test_dice_roll_int():
    app.testing = True 
    client = app.test_client()
    response = client.get("/").json["roll"]
    assert type(response) == int 
    assert response > 0 
    assert response < 7 