import unittest
from tkinter import Tk
from LoginApp import LoginApp
import verify_login

class TestLoginUserErrato(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.app = LoginApp(self.root)

    def tearDown(self):
        try:
            if self.root:
                self.root.destroy()
        except Exception as e:
            print(f"Errore: {e}")

    def test_login_errato(self):
        self.app.entry_1.insert(0, "username_errato")
        self.app.entry_2.insert(0, "password_errata")

        self.assertEqual(verify_login.verify_login("username_errato", "password_errata"), "utente")

        self.root.after(100, self.app.login_clicked)

        self.root.mainloop()

if __name__ == "__main__":
    unittest.main()