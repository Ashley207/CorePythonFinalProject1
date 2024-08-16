import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import threading

def read_data(file):
    try:
        data = pd.read_csv(file)
        return data
    except FileNotFoundError:
        print("Dosya bulunamadı.")
        return None

data = read_data("imdb_top_1000.csv")

if data is None:
    print("Veri yüklenemedi, lütfen dosya yolunu kontrol edin.")
else:
    print("Veri başarıyla yüklendi.")
    print("Sütunlar:", data.columns.tolist())

df = pd.DataFrame(data)

class Film:
    def __init__(self, Poster_Link, Series_Title, Released_Year, Runtime, Genre, Director, IMDB_Rating):
        self.Poster_Link = Poster_Link
        self.Series_Title = Series_Title
        self.Released_Year = Released_Year
        self.Runtime = Runtime
        self.Genre = Genre
        self.Director = Director
        self.IMDB_Rating = IMDB_Rating

    def __str__(self):
        return f"{self.Series_Title} - {self.Released_Year} - directed by {self.Director}, Rating: {self.IMDB_Rating}, Runtime: {self.Runtime}"

film_list = []
if not df.empty:
    for index, row in df.iterrows():
        film = Film(row["Poster_Link"], row["Series_Title"], row["Released_Year"], row["Runtime"], row["Genre"], row["Director"], row["IMDB_Rating"])
        film_list.append(film)

    print(df.head())

for film in film_list:
    print(film)

def reminder_message():
    print("Karar veremedin mi?\n Ruh haline göre aşağıdaki emojilerden birini seç, sana film önerelim.")
    print("1. 😶")
    print("2. 😭")
    print("3. 🥰")
    print("4. 😡")
    print("5. 😞")
    print("6. 🧐")

    emoji_genres = {
        1: ["Comedy", "Musical", "Animation"],
        2: ["Comedy", "Fantasy", "Musical"],
        3: ["Romance", "Family", "Adventure"],
        4: ["Comedy", "Animation"],
        5: ["Fantasy", "Comedy", "Animation"],
        6: ["Crime", "Mystery", "Thriller"]
    }

    while True:
        try:
            emoji_choice = int(input("Emojilerden birini seç (1-6): "))
            if 1 <= emoji_choice <= 6:
                return emoji_genres[emoji_choice]
            else:
                print("Lütfen 1 ile 6 arasında bir sayı girin.")
        except ValueError:
            print("Hata. Lütfen bir sayı girin.")

def get_input():
    print("Hangi türde film izlemek istersiniz?")
    print("1: Crime")
    print("2: Drama")
    print("3: Comedy")
    print("4: Action")
    print("5: Adventure")
    print("6: Sci-fi")
    print("7: Romance")
    print("8: History")
    print("9: Biography")
    print("10: Western")
    print("11: Fantasy")
    print("12: Thriller")
    print("13: Animation")
    print("14: Family")
    print("15: War")
    print("16: Mystery")
    print("17: Musical")
    print("18: Horror")
             
    genres = {
        1: "Crime",
        2: "Drama",
        3: "Comedy",
        4: "Action",
        5: "Adventure",
        6: "Sci-fi",
        7: "Romance",
        8: "History",
        9: "Biography",
        10: "Western",
        11: "Fantasy",
        12: "Thriller",
        13: "Animation",
        14: "Family",
        15: "War",
        16: "Mystery",
        17: "Musical",
        18: "Horror"
    }

    timer = threading.Timer(13, reminder_message)
    timer.start()
    
    while True:
        try:
            genre_choice = int(input("Film türünü seçmek için lütfen 1 ve 18 arasında bir sayı girin: "))
            if 1 <= genre_choice <= 18:
                timer.cancel()
                return genres[genre_choice]
            else:
                print("Lütfen 1 ile 18 arasında bir sayı girin.")
        except ValueError:
            print("Hatalı giriş. Lütfen bir sayı girin.")
    
def filter_movie(df):
    print("Filmleri film sürelerine (dk) göre filtrelemek ister misiniz?")
    print("1: Runtime <= 100 (dk)")
    print("2: Runtime >= 120 (dk)")
    print("3: Filtreleme yapma")
    
    while True:
        try:
            runtime_choice = int(input("Seçiminizi 1, 2 veya 3 olarak giriniz: "))
            if runtime_choice == 1:
                df = df[df["Runtime"].str.extract(r'(\d+)').astype(int) <= 100]
                break
            elif runtime_choice == 2:
                df = df[df["Runtime"].str.extract(r'(\d+)').astype(int) >= 120]
                break
            elif runtime_choice == 3:
                break
            else:
                print("Geçersiz seçim. Lütfen 1, 2 veya 3 girin.")
        except ValueError:
            print("Hatalı giriş. Lütfen bir sayı girin.")

    print("Filmleri yayınlanma yıllarına göre filtrelemek ister misiniz?")
    print("1: 1930 <= Released_Year < 1940")
    print("2: 1940 <= Released_Year < 1950")
    print("3: 1950 <= Released_Year < 1960")
    print("4: 1960 <= Released_Year < 1970")
    print("5: 1970 <= Released_Year < 1980")
    print("6: 1980 <= Released_Year < 1990")
    print("7: 1990 <= Released_Year < 2000")
    print("8: 2000 <= Released_Year < 2010")
    print("9: 2010 <= Released_Year < 2020")

    while True:
        try:
            year_choice = int(input("(1-9) arasında bir değer seçiniz: "))

            if year_choice == 1:
                df = df[(df["Released_Year"] >= 1930) & (df["Released_Year"] < 1940)]
            elif year_choice == 2:
                df = df[(df["Released_Year"] >= 1940) & (df["Released_Year"] < 1950)]
            elif year_choice == 3:
                df = df[(df["Released_Year"] >= 1950) & (df["Released_Year"] < 1960)]
            elif year_choice == 4:
                df = df[(df["Released_Year"] >= 1960) & (df["Released_Year"] < 1970)]
            elif year_choice == 5:
                df = df[(df["Released_Year"] >= 1970) & (df["Released_Year"] < 1980)]
            elif year_choice == 6:
                df = df[(df["Released_Year"] >= 1980) & (df["Released_Year"] < 1990)]
            elif year_choice == 7:
                df = df[(df["Released_Year"] >= 1990) & (df["Released_Year"] < 2000)]
            elif year_choice == 8:
                df = df[(df["Released_Year"] >= 2000) & (df["Released_Year"] < 2010)]
            elif year_choice == 9:
                df = df[(df["Released_Year"] >= 2010) & (df["Released_Year"] < 2020)]
            else:
                print("Geçersiz seçim.")
                continue  # Döngü devam etmeli
            break  # Geçerli bir seçim yapıldığında döngüden çıkılır
        except ValueError:
            print("Hatalı giriş. Lütfen bir sayı girin.")
    
    print("Filmleri IMDB Rating'lerine göre filtrelemek ister misiniz?")
    imdb_rating_choice = float(input("Lütfen 0 ile 10 arasında bir değer girin (8.6 ya da 5 gibi): "))

    if 0 <= imdb_rating_choice <= 10:
        df = df[df["IMDB_Rating"] >= imdb_rating_choice]
    else:
        print("Geçersiz giriş. IMDB Rating 0 ile 10 arasında olmalıdır.")

    return df

genre_input = get_input()

filtered_df = filter_movie(df)

df["Selected"] = df["Genre"].str.contains(genre_input)

selected_films = df[df["Selected"]]

if not selected_films.empty:
    print("Önerilen filmler:")
    print(selected_films)
else:
    print("Bu türde bir film bulunamadı.")

