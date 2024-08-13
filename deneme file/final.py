# class yapısı olmalı en az bir tane
# en az bir tane karar kontrol yapısı- film önerirken kullanılacak.
# en az bir tane döngü kullanılmalı
# kullanıcıdan input alınmalı
# hata kontrolü sağlanmalı, try-except bloğu
# en az bir tane değişken tanımlanmalı
# fonksiyon kullanılmalı
# import ile başlanacak. 
# pandas yüklenecek.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import threading

def read_data(file):
    try:
        data = pd.read_csv(file)
        return data
    
    except FileNotFoundError:
        print("Dosya bulunamadi.")
        return None

data = read_data(r"c:\Users\Aslı\Downloads\imdb_top_1000.csv")
df = pd.DataFrame(data)
df = df.drop(columns=['Overwiev', 'Meta_Score','Star1','Star2','Star3','Star4','No_of_Votes','Gross'])
print(data.head())

class Film:
    def __init__(self,Poster_Link, Series_Title, Released_Year, Runtime, Genre, Director, IMBD_Rating):
        self.Poster_Link = Poster_Link
        self.Series_Title = Series_Title
        self.Released_Year= Released_Year
        self.Runtime = Runtime
        self.Genre = Genre
        self.Director = Director
        self.IMBD_Rating = IMBD_Rating

    def __str__(self):    # __str__ metodu film nesnesi yazdırıldığında nasıl görünüceğini tanımlar
        return f"{self.Series_Title} -{self.Released_Year}- directed by {self.Director}, Rating:{self.IMBD_Rating}, Runtime:{self.Runtime}"
    

df = pd.DataFrame(data)  # bu satır ham veriyi DataFrame yapısına dönüştürür.
if isinstance(data, pd.DataFrame):
    print("Data doğru bir şekilde yüklendi.")
else:
    print("Data yüklenemedi veya yanlış formatta.")


film_list = []
for index, row in df.iterrows(): # iterrows metodu, pandas DataFrame'in satırlarını bir döngü içinde gezmek için kullanılır.
    film = Film(row["Series_Title"], row["Released_Year"], row["Director"], row["IMBD_Rating"], row["Runtime"],row["Genre"])
    film_list.append(film)

print(df.shape)
print(df.head())


for film in film_list:
    print(film)





def reminder_message():
    print("Karar veremedin mi?\n Ruh haline göre aşağıdaki emojilerden birini seç, sana film önerelim.")
    print("1.😶")
    print("2.😭")
    print("3.🥰")
    print("4.😡")
    print("5.😞")
    print("6.🧐")

    try:
        emoji_choice = int(input("Emojilerden birini seç (1-6)."))

        emoji_genres = {
            1:["Comedy","Musical", "Animation"],
            2:["Comedy", "Fantasy", "Musical"],
            3:["Romance", "Family", "Advanture"],
            4:["Comedy","Animation"],
            5:["Fantasy", "Comedy", "Animation"],
            6:["Crime", " Mystery", "Thriller"]

        }

    except ValueError:
        print("Hata. Lütfen girdiğiniz sayıyı kontrol ediniz.(1-6)")

    



def get_input():
    print("Hangi türde film izlemek istersiniz?")
    print("1: Crime")
    print("2: Drama")
    print("3: Comedy")
    print("4: Action")
    print("5: Advanture")
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
          5: "Advanture",
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
    
    genre_choice = input("Film türünü seçmek için lütfen 0 ve 19 arasinda bir sayi girin: ")
    timer.cancel()

    try:
        genre_choice = int(genre_choice)
        if not 1 <= genre_choice <= 18:
            raise ValueError
    except ValueError:
        print("Hatali sayi girildi. Lütfen 0 ve 19 arasindan bir sayi giriniz.")
    
    
    else:
      secilen_film_turu = genres[genre_choice]
      print(f"Seçtiğiniz film türü: {secilen_film_turu}")

    return get_input





def filter_movie(df):
    print("Filmleri film sürelerine(dk) göre filtrelemek ister misiniz?")
    print("1: Runtime <=100 (dk)")
    print("2: Runtime >= 120 (dk)")
    runtime_choice = input("Seçiminizi 1 veya 2 olarak giriniz.")

    if runtime_choice == 1:
        df = df[df["Runtime"] <= 100]    # df['Runtime'] <= 100 ifadesi, df DataFrame'inde bulunan Runtime sütunundaki değerlerin 100'e eşit veya 100'den küçük olup olmadığını kontrol eder.
    elif runtime_choice == 2:
        df = df[df["Runtime"] <= 120]    # Bu koşulu sağlayan satırlar filtrelenir ve sadece bu satırlardan oluşan yeni bir DataFrame oluşturulur.
    else:
        print("Geçersiz seçim.")


    print("Filmleri yayınlanma yıllarına göre filtrelemek ister misiniz?")
    print("1: <= Released_Year <= ")
    print("2: <= Released_Year <= ")
    print("3: <= Released_Year <= ")
    print("4: <= Released_Year <= ")
    print("5: <= Released_Year <= ")
    print("6: <= Released_Year <= ")
    year_choice = input("")

    if year_choice ==1:
        pass
    elif year_choice == 2:
        pass
    elif year_choice == 3:
        pass
    elif year_choice == 4:
        pass
    elif year_choice == 5:
        pass
    elif year_choice == 6:
        pass
    else:
        print("Geçersiz seçim.")



    print("Filmleri IMBD Rating lerine göre filtrelemek ister misiniz? ")
    imbd_rating_choice = float(input("Lütfen 0 ile 10 arasında bir değer girin.(8.6 ya da 5 gibi)"))

    if 1 <= imbd_rating_choice <= 10:
        df = df[df["IMBD_Rating"] >= imbd_rating_choice]
    else:
        print("Geçersiz seçim.")

    return df

filtered_df = filter_movie(df)
print(filtered_df.head(10))

print
    







    


    














        




        