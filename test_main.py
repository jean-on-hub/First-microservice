from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call /search or /wiki"}


def test_read_phrase():
    response = client.get("/phrase/Barack Obama")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "Barack Hussein Obama II ( (listen) bə-RAHK hoo-SAYN oh-BAH-mə; "
            "born August 4, 1961) is an American politician who served as the "
            "44th president of the United States from 2009 to 2017."
        ]
    }


# def test_read_search():
#     response = client.get("/search/jean-eudes")
#     assert response.status_code == 200
#     assert response.json() == {
#         "result": [
#             'John Eudes',           'Jean-Eudes Maurice',           'Eudes',            'Collège Jean-Eudes',            'Jean-Eudes Aholou',            'Jean-Eudes Dubé',            'Jean Eudes Demaret',            'August 19',
#          'Mariology of the saints',            'Jean-Eudes Lauristin'
#         ]
#     }


def test_read_wiki():
    response = client.get("/wiki/jean-eudes")
    assert response.status_code == 200
    assert response.json() == {
        "result": "John Eudes (French: Jean Eudes; 14 November 1601 – 19 August 1680) was a French Roman Catholic priest and the founder of both the Order of Our Lady of Charity in 1641 and Congregation of Jesus and Mary also known as The Eudists in 1643."
    }
