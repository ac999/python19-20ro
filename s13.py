import sqlite3, zipfile, os

def search_for_zip(path):
    for root, dir, file in os.walk(path):
        for name in file:
            if zipfile.is_zipfile(os.path.join(root,name)):
                return os.path.join(root,name)


def problema1(path, low, high, file_name="sample.sqlite"):
    try:
        low = int(low)
        high = int(high)
        f_path = search_for_zip(path)
        if not f_path:
            raise Exception("Archive not found.")
        z = zipfile.ZipFile(f_path)
        found = False
        for _file in z.namelist():
            if _file.rfind(file_name)!=-1:
                db_file = _file
                found = True
                break

        if not found:
            raise Exception("No db file found.")

        z.extract(db_file)

        data = list()

        with sqlite3.connect(db_file) as conn:
            c = conn.cursor()

            query = '''SELECT AlbumId, Name, GenreId
            FROM tracks
            WHERE Milliseconds BETWEEN {0} and {1}'''.format(low, high)

            c.execute(query)

            while(True):
                result = c.fetchone()
                if not result:
                    break
                data.append(result)


            genre_dict=dict()
            album_dict=dict()

            new_data = list()

            for song in data:
                album_id = song[0]
                genre_id = song[2]

                if album_id not in album_dict.keys():
                    query_albums = '''SELECT title FROM albums
                    WHERE AlbumId == {}'''.format(album_id)
                    c.execute(query_albums)
                    album_dict[album_id] = c.fetchone()[0]
                album = album_dict[album_id]

                if genre_id not in genre_dict.keys():
                    query_genres = '''SELECT name FROM genres
                    WHERE GenreId == {}'''.format(genre_id)
                    c.execute(query_genres)
                    genre_dict[genre_id] = c.fetchone()[0]
                genre = genre_dict[genre_id]

                new_data.append((album, song[1], genre))

        return list(sorted(new_data))

    except Exception as e:
        print("Error->", e)
