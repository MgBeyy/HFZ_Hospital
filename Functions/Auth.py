import bcrypt
from datetime import datetime


class User:
    def __init__(self, db_connection):
        self.db = db_connection

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def register_user(self, tc_number, name, surname, birthday, gender,
                      phone_number, address, email, password, user_type='H'):
        try:
            cursor = self.db.cursor()

            # Check if TC number or email already exists
            cursor.execute("SELECT UserID FROM Users WHERE TCNumber = ? OR Email = ?",
                           (tc_number, email))
            if cursor.fetchone():
                return False, "TC Number or Email already registered"

            # Hash password
            password_hash = self.hash_password(password)

            # Insert user
            sql = """
                INSERT INTO Users 
                (TCNumber, Ad, Soyad, DogumTarihi, Cinsiyet, Email, Telefon, Adres, Sifre, Rol)
                VALUES  (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(sql, (tc_number, name, surname, birthday, gender,
                                 phone_number, address, email, password_hash, user_type))

            user_id = cursor.execute("SELECT @@IDENTITY").fetchval()

            # If registering as patient, create patient record
            if user_type == 'patient':
                cursor.execute("""
                    INSERT INTO Patients (UserID, Name, Gender, Phone, Address)
                    VALUES (?, ?, ?, ?, ?)
                """, (user_id, f"{name} {surname}", gender, phone_number, address))

            self.db.commit()
            return True, user_id
        except Exception as e:
            print(f"Error registering user: {str(e)}")
            return False, str(e)

    def login(self, email, sifre):
        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT UserID, Sifre, Rol, Ad, Soyad
                FROM Users WHERE Email = ?
            """, (email,))
            kullanici = cursor.fetchone()

            if not kullanici:
                return False, "Hatalı email veya şifre"

            if not self.verify_password(sifre, kullanici.Sifre):
                return False, "Hatalı email veya şifre"

            return True, {
                'user_id': kullanici.UserID,
                'user_type': kullanici.Rol,
                'name': f"{kullanici.Ad} {kullanici.Soyad}"
            }
        except Exception as e:
            print(f"Giriş hatası: {str(e)}")
            return False, str(e)

    def verify_password(self, password, true_password):
        if bcrypt.checkpw(password.encode('utf-8'), true_password.encode('utf-8')):
            return True
        return False
