import tkinter as tk
from tkinter import messagebox

import mysql.connector
from PIL import Image, ImageTk


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="quwex"
)

table_name = None
data_view = None



root = tk.Tk()
root.geometry("600x600")
root.configure(bg='blue')
root.title("Personal Girişi")

# Hocam giriş kısmında istediğinz hakkında bölümü.
def hakkinda():
    messagebox.showinfo("Hakkında", "Bu program veri tabanını yönetmek için tasarlanmış, bir ara yüz programıdır.\nOluşturan kişi: Osman Eren Somuncular")

def login():
    username = username_entry.get()
    password = password_entry.get()

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Personal WHERE personalKullanıcıAdı = %s AND personalSifre = %s", (username, password))
    result = cursor.fetchone()



    if result:

        root.destroy()
        show_main_menu()

    else:

        error_label = tk.Label(root, text="Kullanıcı bulunamadı!", fg="black")
        error_label.pack()

def register():
    register_window = tk.Toplevel(root)
    register_window.geometry("400x300")
    register_window.configure(bg='blue')
    register_window.title("Personal Kayıt")


    personalAdı_label = tk.Label(register_window, text="Adı:", fg="black")
    personalAdı_label.pack()
    personalAdı_entry = tk.Entry(register_window)
    personalAdı_entry.pack()

    personalSoyad_label = tk.Label(register_window, text="Soyadı:", fg="black")
    personalSoyad_label.pack()
    personalSoyad_entry = tk.Entry(register_window)
    personalSoyad_entry.pack()

    personalKullanıcıAdı_label = tk.Label(register_window, text="Kullanıcı Adı:", fg="black")
    personalKullanıcıAdı_label.pack()
    personalKullanıcıAdı_entry = tk.Entry(register_window)
    personalKullanıcıAdı_entry.pack()

    personalEmail_label = tk.Label(register_window, text="Email:", fg="black")
    personalEmail_label.pack()
    personalEmail_entry = tk.Entry(register_window)
    personalEmail_entry.pack()

    personalSifre_label = tk.Label(register_window, text="Şifre:", fg="black")
    personalSifre_label.pack()
    personalSifre_entry = tk.Entry(register_window, show="*")
    personalSifre_entry.pack()

    def add_to_database():

        ad = personalAdı_entry.get()
        soyad = personalSoyad_entry.get()
        kullanıcıAdı = personalKullanıcıAdı_entry.get()
        email = personalEmail_entry.get()
        sifre = personalSifre_entry.get()

        cursor = mydb.cursor()
        insert_query = "INSERT INTO Personal (personalAdı, personalSoyad, personalKullanıcıAdı, personalEmail, personalSifre) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (ad, soyad, kullanıcıAdı, email, sifre))
        mydb.commit()

        register_window.destroy()

    register_button = tk.Button(register_window, text="Kayıt Ol", command=add_to_database, bg="black", fg="white")
    register_button.pack()


username_label = tk.Label(root, text="Kullanıcı Adı:", fg="black")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Şifre:", fg="black")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Giriş Yap", command=login, bg="black", fg="white")
login_button.pack()

register_button = tk.Button(root, text="Kayıt Ol", command=register, bg="black", fg="white")
register_button.pack()

about_button = tk.Button(root, text="Hakkında", command=hakkinda, bg="black", fg="white")
about_button.pack()


def add_image():

    image = Image.open("C:/PycharmProjects/pythonProject2/venv/Resimler/logo.jpg")
    image = image.resize((200, 200))


    tk_image = ImageTk.PhotoImage(image)


    image_label = tk.Label(root, image=tk_image)
    image_label.pack()
    image_label.place(x=200, y=200)


    image_label.image = tk_image


add_image()


def show_section_data(section_name):
    section_window = tk.Toplevel()
    section_window.geometry("800x800")
    section_window.title(f"{section_name} Veri Sayfası")
    section_window.configure(bg='lightblue')


    data_view = tk.Text(section_window, height=20, width=100, bg='black', fg='white')
    data_view.pack()


    if section_name == "Influencer":
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM influencer")
        result = cursor.fetchall()

        for row in result:
            data_view.insert(tk.END, f"{row}\n")

    if section_name == "Videolar":
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM videolar")
        result = cursor.fetchall()

        for row in result:
            data_view.insert(tk.END, f"{row}\n")

    if section_name == "İzlenmeler":
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM izlenmeler")
        result = cursor.fetchall()

        for row in result:
            data_view.insert(tk.END, f"{row}\n")

    if section_name == "Beğeniler":
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM begeniler")
        result = cursor.fetchall()

        for row in result:
            data_view.insert(tk.END, f"{row}\n")

    if section_name == "Yorumlar":
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM yorumlar")
        result = cursor.fetchall()

        for row in result:
            data_view.insert(tk.END, f"{row}\n")

    if section_name == "Abone":
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM abone")
        result = cursor.fetchall()

        for row in result:
            data_view.insert(tk.END, f"{row}\n")

    if section_name == "Kategori":
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM kategori")
        result = cursor.fetchall()

        for row in result:
            data_view.insert(tk.END, f"{row}\n")

    if section_name == "KriptoParaOdemeleri":
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM 	kriptoparaodemeleri")
        result = cursor.fetchall()

        for row in result:
            data_view.insert(tk.END, f"{row}\n")

    def add_data_to_influencer_table():

        add_data_window = tk.Toplevel()
        add_data_window.geometry("400x300")
        add_data_window.title("Influencer Veri Ekle")
        add_data_window.configure(bg='lightblue')


        influencer_id_label = tk.Label(add_data_window, text="Influencer ID:", fg="black")
        influencer_id_label.pack()
        influencer_id_entry = tk.Entry(add_data_window)
        influencer_id_entry.pack()

        kullanici_adi_label = tk.Label(add_data_window, text="Kullanıcı Adı:", fg="black")
        kullanici_adi_label.pack()
        kullanici_adi_entry = tk.Entry(add_data_window)
        kullanici_adi_entry.pack()

        influencer_ad_label = tk.Label(add_data_window, text="Influencer Adı:", fg="black")
        influencer_ad_label.pack()
        influencer_ad_entry = tk.Entry(add_data_window)
        influencer_ad_entry.pack()

        influencer_soyad_label = tk.Label(add_data_window, text="Influencer Soyadı:", fg="black")
        influencer_soyad_label.pack()
        influencer_soyad_entry = tk.Entry(add_data_window)
        influencer_soyad_entry.pack()

        email_label = tk.Label(add_data_window, text="Email:", fg="black")
        email_label.pack()
        email_entry = tk.Entry(add_data_window)
        email_entry.pack()

        sifre_label = tk.Label(add_data_window, text="Şifre:", fg="black")
        sifre_label.pack()
        sifre_entry = tk.Entry(add_data_window, show="*")
        sifre_entry.pack()
# hocam influencerlar tablosuna veri ekle hatasını çözdüm, isterseniz deneyebilirsiniz,
        def insert_data_to_table():
            influencer_id = influencer_id_entry.get()
            kullanici_adi = kullanici_adi_entry.get()
            influencer_ad = influencer_ad_entry.get()
            influencer_soyad = influencer_soyad_entry.get()
            email = email_entry.get()
            sifre = sifre_entry.get()


            if influencer_id and influencer_id.isdigit():

                cursor = mydb.cursor()
                insert_query = "INSERT INTO Influencer (InfluencerID, KullanıcıAdı, InfluencerAd, InfluencerSoyad, Email, Sifre) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(insert_query,
                               (influencer_id, kullanici_adi, influencer_ad, influencer_soyad, email, sifre))
                mydb.commit()

                add_data_window.destroy()
            else:

                error_label = tk.Label(add_data_window, text="Geçersiz Influencer ID!", fg="black")
                error_label.pack()

            add_data_window.destroy()




        insert_button = tk.Button(add_data_window, text="Veri Ekle", command=insert_data_to_table, bg="green",
                                      fg="white")
        insert_button.pack()

        def delete_data_from_influencer_table():

            delete_data_window = tk.Toplevel()
            delete_data_window.geometry("400x200")
            delete_data_window.title("Influencer Veri Sil")
            delete_data_window.configure(bg='lightblue')


            influencer_id_label = tk.Label(delete_data_window, text="Influencer ID:", fg="black")
            influencer_id_label.pack()
            influencer_id_entry = tk.Entry(delete_data_window)
            influencer_id_entry.pack()

            def delete_data_from_table():

                influencer_id = influencer_id_entry.get()


                cursor = mydb.cursor()
                delete_query = "DELETE FROM Influencer WHERE InfluencerID = %s"
                cursor.execute(delete_query, (influencer_id,))
                mydb.commit()


                delete_data_window.destroy()


            delete_button = tk.Button(delete_data_window, text="Veri Sil", command=delete_data_from_table, bg="red",
                                      fg="white")
            delete_button.pack()


        delete_button = tk.Button(section_window, text="Veri Sil (Influencerlar)",
                                  command=delete_data_from_influencer_table,
                                  bg="red", fg="white")
        delete_button.pack(pady=5)


    add_button = tk.Button(section_window, text="Veri Ekle (Influencerlar)", command=add_data_to_influencer_table,
                               bg="green",
                               fg="white")
    add_button.pack(pady=5)

    def add_data_to_videos_table():

        add_data_window = tk.Toplevel()
        add_data_window.geometry("400x300")
        add_data_window.title("Video Veri Ekle")
        add_data_window.configure(bg='lightblue')


        video_id_label = tk.Label(add_data_window, text="Video ID:", fg="black")
        video_id_label.pack()
        video_id_entry = tk.Entry(add_data_window)
        video_id_entry.pack()

        influencer_id_label = tk.Label(add_data_window, text="Influencer ID:", fg="black")
        influencer_id_label.pack()
        influencer_id_entry = tk.Entry(add_data_window)
        influencer_id_entry.pack()

        video_basligi_label = tk.Label(add_data_window, text="Video Başlığı:", fg="black")
        video_basligi_label.pack()
        video_basligi_entry = tk.Entry(add_data_window)
        video_basligi_entry.pack()

        olusturma_tarihi_label = tk.Label(add_data_window, text="Oluşturma Tarihi:", fg="black")
        olusturma_tarihi_label.pack()
        olusturma_tarihi_entry = tk.Entry(add_data_window)
        olusturma_tarihi_entry.pack()

        def insert_data_to_videos_table():

            video_id = video_id_entry.get()
            influencer_id = influencer_id_entry.get()
            video_basligi = video_basligi_entry.get()
            olusturma_tarihi = olusturma_tarihi_entry.get()


            cursor = mydb.cursor()
            insert_query = "INSERT INTO Videolar (VideoID, InfluencerID, VideoBaslıgı, OlusturmaTarihi) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (video_id, influencer_id, video_basligi, olusturma_tarihi))
            mydb.commit()


            add_data_window.destroy()


        insert_button = tk.Button(add_data_window, text="Veri Ekle", command=insert_data_to_videos_table, bg="green",
                                  fg="white")
        insert_button.pack()

        def delete_data_from_videos_table():

            delete_data_window = tk.Toplevel()
            delete_data_window.geometry("400x200")
            delete_data_window.title("Video Veri Sil")
            delete_data_window.configure(bg='lightblue')


            video_id_label = tk.Label(delete_data_window, text="Video ID:", fg="black")
            video_id_label.pack()
            video_id_entry = tk.Entry(delete_data_window)
            video_id_entry.pack()

            def delete_data_from_table():

                video_id = video_id_entry.get()


                cursor = mydb.cursor()
                delete_query = "DELETE FROM Videolar WHERE VideoID = %s"
                cursor.execute(delete_query, (video_id,))
                mydb.commit()


                delete_data_window.destroy()


            delete_button = tk.Button(delete_data_window, text="Veri Sil", command=delete_data_from_table, bg="red",
                                      fg="white")
            delete_button.pack()


        delete_button = tk.Button(section_window, text="Veri Sil (Videolar)", command=delete_data_from_videos_table,
                                  bg="red", fg="white")
        delete_button.pack(pady=5)


    add_button = tk.Button(section_window, text="Veri Ekle (Videolar)", command=add_data_to_videos_table, bg="green",
                               fg="white")
    add_button.pack(pady=5)

    def add_data_to_izlenmeler_table():

        add_data_window = tk.Toplevel()
        add_data_window.geometry("400x300")
        add_data_window.title("İzlenme Veri Ekle")
        add_data_window.configure(bg='lightblue')


        izlenme_id_label = tk.Label(add_data_window, text="İzlenme ID:", fg="black")
        izlenme_id_label.pack()
        izlenme_id_entry = tk.Entry(add_data_window)
        izlenme_id_entry.pack()

        video_id_label = tk.Label(add_data_window, text="Video ID:", fg="black")
        video_id_label.pack()
        video_id_entry = tk.Entry(add_data_window)
        video_id_entry.pack()

        izlenme_sayisi_label = tk.Label(add_data_window, text="İzlenme Sayısı:", fg="black")
        izlenme_sayisi_label.pack()
        izlenme_sayisi_entry = tk.Entry(add_data_window)
        izlenme_sayisi_entry.pack()

        def insert_data_to_izlenmeler_table():

            izlenme_id = izlenme_id_entry.get()
            video_id = video_id_entry.get()
            izlenme_sayisi = izlenme_sayisi_entry.get()


            cursor = mydb.cursor()
            insert_query = "INSERT INTO Izlenmeler (IzlenmeID, VideoID, IzlenmeSayısı) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (izlenme_id, video_id, izlenme_sayisi))
            mydb.commit()


            add_data_window.destroy()


        insert_button = tk.Button(add_data_window, text="Veri Ekle", command=insert_data_to_izlenmeler_table,
                                  bg="green", fg="white")
        insert_button.pack()

        def delete_data_from_izlenmeler_table():

            delete_data_window = tk.Toplevel()
            delete_data_window.geometry("400x200")
            delete_data_window.title("İzlenme Veri Sil")
            delete_data_window.configure(bg='lightblue')


            izlenme_id_label = tk.Label(delete_data_window, text="İzlenme ID:", fg="black")
            izlenme_id_label.pack()
            izlenme_id_entry = tk.Entry(delete_data_window)
            izlenme_id_entry.pack()

            def delete_data_from_table():

                izlenme_id = izlenme_id_entry.get()


                cursor = mydb.cursor()
                delete_query = "DELETE FROM Izlenmeler WHERE IzlenmeID = %s"
                cursor.execute(delete_query, (izlenme_id,))
                mydb.commit()


                delete_data_window.destroy()


            delete_button = tk.Button(delete_data_window, text="Veri Sil", command=delete_data_from_table, bg="red",
                                      fg="white")
            delete_button.pack()


        delete_button = tk.Button(section_window, text="Veri Sil (İzlenmeler)",
                                  command=delete_data_from_izlenmeler_table,
                                  bg="red", fg="white")
        delete_button.pack(pady=5)

    add_button = tk.Button(section_window, text="Veri Ekle (İzlenmeler)", command=add_data_to_izlenmeler_table,
                               bg="green", fg="white")
    add_button.pack(pady=5)

    def add_data_to_begeniler_table():

        add_data_window = tk.Toplevel()
        add_data_window.geometry("400x300")
        add_data_window.title("Beğeni Veri Ekle")
        add_data_window.configure(bg='lightblue')


        begeni_id_label = tk.Label(add_data_window, text="Beğeni ID:", fg="black")
        begeni_id_label.pack()
        begeni_id_entry = tk.Entry(add_data_window)
        begeni_id_entry.pack()

        video_id_label = tk.Label(add_data_window, text="Video ID:", fg="black")
        video_id_label.pack()
        video_id_entry = tk.Entry(add_data_window)
        video_id_entry.pack()

        begeni_sayisi_label = tk.Label(add_data_window, text="Beğeni Sayısı:", fg="black")
        begeni_sayisi_label.pack()
        begeni_sayisi_entry = tk.Entry(add_data_window)
        begeni_sayisi_entry.pack()

        def insert_data_to_begeniler_table():

            begeni_id = begeni_id_entry.get()
            video_id = video_id_entry.get()
            begeni_sayisi = begeni_sayisi_entry.get()


            cursor = mydb.cursor()
            insert_query = "INSERT INTO Begeniler (BegeniID, VideoID, BegeniSayısı) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (begeni_id, video_id, begeni_sayisi))
            mydb.commit()


            add_data_window.destroy()


        insert_button = tk.Button(add_data_window, text="Veri Ekle", command=insert_data_to_begeniler_table, bg="green",
                                  fg="white")
        insert_button.pack()

        def delete_data_from_begeniler_table():

            delete_data_window = tk.Toplevel()
            delete_data_window.geometry("400x200")
            delete_data_window.title("Beğeni Veri Sil")
            delete_data_window.configure(bg='lightblue')


            begeni_id_label = tk.Label(delete_data_window, text="Beğeni ID:", fg="black")
            begeni_id_label.pack()
            begeni_id_entry = tk.Entry(delete_data_window)
            begeni_id_entry.pack()

            def delete_data_from_table():

                begeni_id = begeni_id_entry.get()


                cursor = mydb.cursor()
                delete_query = "DELETE FROM Begeniler WHERE BegeniID = %s"
                cursor.execute(delete_query, (begeni_id,))
                mydb.commit()


                delete_data_window.destroy()


            delete_button = tk.Button(delete_data_window, text="Veri Sil", command=delete_data_from_table, bg="red",
                                      fg="white")
            delete_button.pack()


        delete_button = tk.Button(section_window, text="Veri Sil (Beğeniler)", command=delete_data_from_begeniler_table,
                                  bg="red", fg="white")
        delete_button.pack(pady=5)



    add_button = tk.Button(section_window, text="Veri Ekle (Beğeniler)", command=add_data_to_begeniler_table,
                               bg="green", fg="white")
    add_button.pack(pady=5)

    def add_data_to_yorumlar_table():

        add_data_window = tk.Toplevel()
        add_data_window.geometry("400x300")
        add_data_window.title("Yorum Veri Ekle")
        add_data_window.configure(bg='lightblue')


        yorum_id_label = tk.Label(add_data_window, text="Yorum ID:", fg="black")
        yorum_id_label.pack()
        yorum_id_entry = tk.Entry(add_data_window)
        yorum_id_entry.pack()

        video_id_label = tk.Label(add_data_window, text="Video ID:", fg="black")
        video_id_label.pack()
        video_id_entry = tk.Entry(add_data_window)
        video_id_entry.pack()

        yorum_sayisi_label = tk.Label(add_data_window, text="Yorum Sayısı:", fg="black")
        yorum_sayisi_label.pack()
        yorum_sayisi_entry = tk.Entry(add_data_window)
        yorum_sayisi_entry.pack()

        def insert_data_to_yorumlar_table():

            yorum_id = yorum_id_entry.get()
            video_id = video_id_entry.get()
            yorum_sayisi = yorum_sayisi_entry.get()

            cursor = mydb.cursor()
            insert_query = "INSERT INTO Yorumlar (YorumID, VideoID, YorumSayısı) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (yorum_id, video_id, yorum_sayisi))
            mydb.commit()


            add_data_window.destroy()


        insert_button = tk.Button(add_data_window, text="Veri Ekle", command=insert_data_to_yorumlar_table, bg="green",
                                  fg="white")
        insert_button.pack()

        def delete_data_from_yorumlar_table():

            delete_data_window = tk.Toplevel()
            delete_data_window.geometry("400x200")
            delete_data_window.title("Yorum Veri Sil")
            delete_data_window.configure(bg='lightblue')


            yorum_id_label = tk.Label(delete_data_window, text="Yorum ID:", fg="black")
            yorum_id_label.pack()
            yorum_id_entry = tk.Entry(delete_data_window)
            yorum_id_entry.pack()

            def delete_data_from_table():

                yorum_id = yorum_id_entry.get()


                cursor = mydb.cursor()
                delete_query = "DELETE FROM Yorumlar WHERE YorumID = %s"
                cursor.execute(delete_query, (yorum_id,))
                mydb.commit()


                delete_data_window.destroy()


            delete_button = tk.Button(delete_data_window, text="Veri Sil", command=delete_data_from_table, bg="red",
                                      fg="white")
            delete_button.pack()


        delete_button = tk.Button(section_window, text="Veri Sil (Yorumlar)", command=delete_data_from_yorumlar_table,
                                  bg="red", fg="white")
        delete_button.pack(pady=5)


    add_button = tk.Button(section_window, text="Veri Ekle (Yorumlar)", command=add_data_to_yorumlar_table, bg="green",
                               fg="white")
    add_button.pack(pady=5)

    def add_data_to_abone_table():

        add_data_window = tk.Toplevel()
        add_data_window.geometry("400x300")
        add_data_window.title("Abone Veri Ekle")
        add_data_window.configure(bg='lightblue')


        abone_id_label = tk.Label(add_data_window, text="Abone ID:", fg="black")
        abone_id_label.pack()
        abone_id_entry = tk.Entry(add_data_window)
        abone_id_entry.pack()

        influencer_id_label = tk.Label(add_data_window, text="Influencer ID:", fg="black")
        influencer_id_label.pack()
        influencer_id_entry = tk.Entry(add_data_window)
        influencer_id_entry.pack()

        abone_sayisi_label = tk.Label(add_data_window, text="Abone Sayısı:", fg="black")
        abone_sayisi_label.pack()
        abone_sayisi_entry = tk.Entry(add_data_window)
        abone_sayisi_entry.pack()

        def insert_data_to_abone_table():

            abone_id = abone_id_entry.get()
            influencer_id = influencer_id_entry.get()
            abone_sayisi = abone_sayisi_entry.get()


            cursor = mydb.cursor()
            insert_query = "INSERT INTO Abone (AboneID, InfluencerID, AboneSayısı) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (abone_id, influencer_id, abone_sayisi))
            mydb.commit()


            add_data_window.destroy()


        insert_button = tk.Button(add_data_window, text="Veri Ekle", command=insert_data_to_abone_table, bg="green",
                                  fg="white")
        insert_button.pack()

        def delete_data_from_abone_table():

            delete_data_window = tk.Toplevel()
            delete_data_window.geometry("400x200")
            delete_data_window.title("Abone Veri Sil")
            delete_data_window.configure(bg='lightblue')


            abone_id_label = tk.Label(delete_data_window, text="Abone ID:", fg="black")
            abone_id_label.pack()
            abone_id_entry = tk.Entry(delete_data_window)
            abone_id_entry.pack()

            def delete_data_from_table():

                abone_id = abone_id_entry.get()


                cursor = mydb.cursor()
                delete_query = "DELETE FROM Abone WHERE AboneID = %s"
                cursor.execute(delete_query, (abone_id,))
                mydb.commit()


                delete_data_window.destroy()


            delete_button = tk.Button(delete_data_window, text="Veri Sil", command=delete_data_from_table, bg="red",
                                      fg="white")
            delete_button.pack()

        delete_button = tk.Button(section_window, text="Veri Sil (Abone)", command=delete_data_from_abone_table,
                                  bg="red", fg="white")
        delete_button.pack(pady=5)


    add_button = tk.Button(section_window, text="Veri Ekle (Abone)", command=add_data_to_abone_table, bg="green",
                               fg="white")
    add_button.pack(pady=5)

    def add_data_to_kategori_table():

        add_data_window = tk.Toplevel()
        add_data_window.geometry("400x300")
        add_data_window.title("Kategori Veri Ekle")
        add_data_window.configure(bg='lightblue')


        kategori_id_label = tk.Label(add_data_window, text="Kategori ID:", fg="black")
        kategori_id_label.pack()
        kategori_id_entry = tk.Entry(add_data_window)
        kategori_id_entry.pack()

        video_id_label = tk.Label(add_data_window, text="Video ID:", fg="black")
        video_id_label.pack()
        video_id_entry = tk.Entry(add_data_window)
        video_id_entry.pack()

        video_kategorisi_label = tk.Label(add_data_window, text="Video Kategorisi:", fg="black")
        video_kategorisi_label.pack()
        video_kategorisi_entry = tk.Entry(add_data_window)
        video_kategorisi_entry.pack()

        def insert_data_to_kategori_table():

            kategori_id = kategori_id_entry.get()
            video_id = video_id_entry.get()
            video_kategorisi = video_kategorisi_entry.get()


            cursor = mydb.cursor()
            insert_query = "INSERT INTO Kategori (KategoriID, VideoID, VideoKategorisi) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (kategori_id, video_id, video_kategorisi))
            mydb.commit()


            add_data_window.destroy()


        insert_button = tk.Button(add_data_window, text="Veri Ekle", command=insert_data_to_kategori_table, bg="green",
                                  fg="white")
        insert_button.pack()

        def delete_data_from_kategori_table():

            delete_data_window = tk.Toplevel()
            delete_data_window.geometry("400x200")
            delete_data_window.title("Kategori Veri Sil")
            delete_data_window.configure(bg='lightblue')


            kategori_id_label = tk.Label(delete_data_window, text="Kategori ID:", fg="black")
            kategori_id_label.pack()
            kategori_id_entry = tk.Entry(delete_data_window)
            kategori_id_entry.pack()

            def delete_data_from_table():

                kategori_id = kategori_id_entry.get()


                cursor = mydb.cursor()
                delete_query = "DELETE FROM Kategori WHERE KategoriID = %s"
                cursor.execute(delete_query, (kategori_id,))
                mydb.commit()


                delete_data_window.destroy()


            delete_button = tk.Button(delete_data_window, text="Veri Sil", command=delete_data_from_table, bg="red",
                                      fg="white")
            delete_button.pack()


        delete_button = tk.Button(section_window, text="Veri Sil (Kategori)", command=delete_data_from_kategori_table,
                                  bg="red", fg="white")
        delete_button.pack(pady=5)


    add_button = tk.Button(section_window, text="Veri Ekle (Kategori)", command=add_data_to_kategori_table, bg="green",
                               fg="white")
    add_button.pack(pady=5)

    def add_data_to_kripto_para_odemeleri_table():

        add_data_window = tk.Toplevel()
        add_data_window.geometry("400x300")
        add_data_window.title("Kripto Para Ödemeleri Veri Ekle")
        add_data_window.configure(bg='lightblue')


        odeme_id_label = tk.Label(add_data_window, text="Ödeme ID:", fg="black")
        odeme_id_label.pack()
        odeme_id_entry = tk.Entry(add_data_window)
        odeme_id_entry.pack()

        influencer_id_label = tk.Label(add_data_window, text="Influencer ID:", fg="black")
        influencer_id_label.pack()
        influencer_id_entry = tk.Entry(add_data_window)
        influencer_id_entry.pack()

        kripto_cuzdan_adresi_label = tk.Label(add_data_window, text="Kripto Cüzdan Adresi:", fg="black")
        kripto_cuzdan_adresi_label.pack()
        kripto_cuzdan_adresi_entry = tk.Entry(add_data_window)
        kripto_cuzdan_adresi_entry.pack()

        miktar_label = tk.Label(add_data_window, text="Miktar (Para):", fg="black")
        miktar_label.pack()
        miktar_entry = tk.Entry(add_data_window)
        miktar_entry.pack()

        odeme_tarihi_label = tk.Label(add_data_window, text="Ödeme Tarihi:", fg="black")
        odeme_tarihi_label.pack()
        odeme_tarihi_entry = tk.Entry(add_data_window)
        odeme_tarihi_entry.pack()

        def insert_data_to_kripto_para_odemeleri_table():

            odeme_id = odeme_id_entry.get()
            influencer_id = influencer_id_entry.get()
            kripto_cuzdan_adresi = kripto_cuzdan_adresi_entry.get()
            miktar = miktar_entry.get()
            odeme_tarihi = odeme_tarihi_entry.get()


            cursor = mydb.cursor()
            insert_query = "INSERT INTO KriptoParaOdemeleri (OdemeID, InfluencerID, KriptoCuzdanAdresi, Miktar, OdemeTarihi) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (odeme_id, influencer_id, kripto_cuzdan_adresi, miktar, odeme_tarihi))
            mydb.commit()


            add_data_window.destroy()


        insert_button = tk.Button(add_data_window, text="Veri Ekle", command=insert_data_to_kripto_para_odemeleri_table,
                                  bg="green", fg="white")
        insert_button.pack()

        def delete_data_from_kripto_para_odemeleri_table():

            delete_data_window = tk.Toplevel()
            delete_data_window.geometry("400x200")
            delete_data_window.title("Kripto Para Ödemeleri Veri Sil")
            delete_data_window.configure(bg='lightblue')


            odeme_id_label = tk.Label(delete_data_window, text="Ödeme ID:", fg="black")
            odeme_id_label.pack()
            odeme_id_entry = tk.Entry(delete_data_window)
            odeme_id_entry.pack()

            def delete_data_from_table():

                odeme_id = odeme_id_entry.get()


                cursor = mydb.cursor()
                delete_query = "DELETE FROM KriptoParaOdemeleri WHERE OdemeID = %s"
                cursor.execute(delete_query, (odeme_id,))
                mydb.commit()


                delete_data_window.destroy()


            delete_button = tk.Button(delete_data_window, text="Veri Sil", command=delete_data_from_table, bg="red",
                                      fg="white")
            delete_button.pack()


        delete_button = tk.Button(section_window, text="Veri Sil (Kripto Para Ödemeleri)",
                                  command=delete_data_from_kripto_para_odemeleri_table,
                                  bg="red", fg="white")
        delete_button.pack(pady=5)


    add_button = tk.Button(section_window, text="Veri Ekle (Kripto Para Ödemeleri)",
                               command=add_data_to_kripto_para_odemeleri_table, bg="green", fg="white")
    add_button.pack(pady=5)


def show_main_menu():
    main_menu = tk.Tk()
    main_menu.geometry("1000x400")
    main_menu.configure(bg='blue')
    main_menu.title("Ana Menü")

    sections = ["Influencer", "Videolar", "İzlenmeler", "Beğeniler", "Yorumlar", "Abone", "Kategori",
                "KriptoParaOdemeleri"]

    for section in sections:
        section_button = tk.Button(main_menu, text=f"{section} Bölümü", bg="yellow", fg="black",
                                   command=lambda sec=section: show_section_data(sec))
        section_button.pack(side=tk.LEFT, padx=5, pady=5)


    main_menu.mainloop()

root.mainloop()









