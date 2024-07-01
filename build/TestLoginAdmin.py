import unittest
from tkinter import Tk
from LoginApp import LoginApp
import verify_login
import threading


class TestLoginAdmin(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.app = LoginApp(self.root)

    def tearDown(self):
        try:
            if self.root:
                self.root.destroy()
        except Exception as e:
            print(f"Errore: {e}")

    def test_login_admin(self):
        self.app.entry_1.insert(0, "admin")
        self.app.entry_2.insert(0, "admin123")

        self.assertEqual(verify_login.verify_login("admin", "admin123"), "admin")

        self.root.after(100, self.app.login_clicked)

        self.root.mainloop()


if __name__ == "__main__":
    unittest.main()
