# pip install fastapi uvicorn

# import library
from fastapi import FastAPI

# Bikin instance FastAPI
# PERHATIKAN NAMA VARIABELNYA!
app = FastAPI()


# Tentukan dulu URLnya itu (Endpointnya) itu yang mana?
# http://localhost"/"
# GET /
@app.get("/")
def fetch_slash():
    """Fetch data from Root Endpoint

    Returns:
        dict: Return Hello World
    """
    return {"hello": "world"}


# GET /albums
@app.get("/albums")
def fetch_albums():
    return {"data": {"albums": [{"id": 1, "name": "Album A"}]}}


# GET /albums/"name" (name adalah variabel yang dinamis)
@app.get("/albums/{name}")
def fetch_albums_by_name(name):  # name HARUS sama dengan yang ada di CURLY BRACKET
    return {
        "data": {
            "album_name": name,
            "id": "Id belum ada nih, kamu nanti bisa tambahin yah!",
        }
    }


# Ini list kosongan
albums = []


# Ini sekarang gw punya endpoint /albums TAPI PAKE POST
# POST /albums
@app.post("/albums")
# PERHATIKAN BAIK BAIK DI SINI ADA PARAMETER YANG KAMU DEFINISIKAN
# DI SINI GW KASIH namanya adalah "album_baru"
# tipe data dari parameter "album_baru" adalah suatu dictionary
def add_album_baru(album_baru: dict):
    # Di sini tuh bagian logic, pengen diapain pun OKE
    print(f"Album baru yang ditambakan adalah: {album_baru}")
    print(f"type data dari album baru adalah {type(album_baru)}")

    albums.append(album_baru)

    print(f"Isi dari album sekarang adalah {albums}")

    # YANG PENTING JANGAN LUPA RETURN!
    # Ceritanya ini palsu, ga ditambahin apa-apa
    return {"result": "Data berhasil ditambahkan"}


# Convention:
# untuk nama Endpoint, itu biasanya JANGAN ADA KATA KATA PERINTAHNYA
# GET  /albums
# GET  /albums/{id}
# POST /albums

# GET  /fetch-albums
# POST /add-albums

# GET /albums_top_10/ <-- kurang tepat, karena biasanya adalah -
# GET /albums-top-10

# Biasanya resourcenya itu di GROUPING
# GET /albums/
# GET /albums/top-ten


# Kalau udah tinggal "JALANIN"
# uvicorn nama_file_tanpa_py:nama_variabe_fast_api --reload
