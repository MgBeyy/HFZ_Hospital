import bcrypt


class User:
    def __init__(self, db_connection):
        self.db = db_connection

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def register_user(self, tc_number, name, surname, birthday, gender,
                      phone_number, address, email, password, user_type='P'):
        try:
            cursor = self.db.cursor()

            # Check if TC number or email already exists
            cursor.execute("SELECT UserID FROM Users WHERE TC = ? OR Email = ?",
                           (tc_number, email))
            if cursor.fetchone():
                return False, "TC Number or Email already registered"

            # Hash password
            password_hash = self.hash_password(password)

            # Insert user
            sql = """
                INSERT INTO Users 
                (TC, Name, Surname, Birthdate, Gender, Email, PhoneNumber, Address, Password, Role)
                VALUES  (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(sql, (tc_number, name, surname, birthday, gender,
                                 email, phone_number, address, password_hash, user_type))

            user_id = cursor.execute("SELECT @@IDENTITY").fetchval()
            print(user_id)

            # If registering as patient, create patient record
            if user_type == 'P':
                cursor.execute("""
                    INSERT INTO Patient (UserID)
                    VALUES (?)
                """, user_id)

            self.db.commit()
            return True, user_id
        except Exception as e:
            print(f"Error registering user: {str(e)}")
            return False, str(e)

    def login(self, tc_number, password):
        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT UserID, Password, Role, Name, Surname
                FROM Users WHERE TC = ?
            """, (tc_number,))
            user = cursor.fetchone()

            if not user:
                return False, "Hatalı email veya şifre"

            if not self.verify_password(password, user.Password):
                return False, "Hatalı email veya şifre"

            return True, {
                'user_id': user.UserID,
                'user_type': user.Role,
                'name': f"{user.Name} {user.Surname}"
            }
        except Exception as e:
            print(f"Giriş hatası: {str(e)}")
            return False, str(e)

    def verify_password(self, password, true_password):
        return bcrypt.checkpw(password.encode('utf-8'), true_password.encode('utf-8'))
