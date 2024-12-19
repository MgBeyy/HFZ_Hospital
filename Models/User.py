import bcrypt
from datetime import datetime


class User:
    def __init__(self, db_connection):
        self.db = db_connection

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def verify_password(self, password, hashed):
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

    def register_user(self, tc_number, name, surname, birthday, gender,
                      phone_number, address, email, password, user_type='patient'):
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
                (TCNumber, Name, Surname, Birthday, Gender, PhoneNumber, 
                 Address, Email, PasswordHash, UserType)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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

    def login(self, email, password):
        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT UserID, PasswordHash, UserType, Name, Surname
                FROM Users WHERE Email = ?
            """, (email,))
            user = cursor.fetchone()

            if not user:
                return False, "Invalid email or password"

            if not self.verify_password(password, user.PasswordHash):
                return False, "Invalid email or password"

            return True, {
                'user_id': user.UserID,
                'user_type': user.UserType,
                'name': f"{user.Name} {user.Surname}"
            }
        except Exception as e:
            print(f"Error during login: {str(e)}")
            return False, str(e)

    def get_user_details(self, user_id):
        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT UserID, TCNumber, Name, Surname, Birthday, Gender,
                       PhoneNumber, Address, Email, UserType
                FROM Users WHERE UserID = ?
            """, (user_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error fetching user details: {str(e)}")
            return None