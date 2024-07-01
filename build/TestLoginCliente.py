import unittest
from tkinter import Tk
from LoginApp import LoginApp
import verify_login

class TestLoginUser(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.app = LoginApp(self.root)

    def tearDown(self):
        try:
            if self.root:
                self.root.destroy()
        except Exception as e:
            print(f"Errore: {e}")

    def test_login_user(self):
        self.app.entry_1.insert(0, "Ciao")
        self.app.entry_2.insert(0, "Ciao")

        self.assertEqual(verify_login.verify_login("Ciao", "Ciao"), "utente")

        self.root.after(100, self.app.login_clicked)

        self.root.mainloop()

if __name__ == "__main__":
    unittest.main()