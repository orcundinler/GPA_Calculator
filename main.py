import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from tkinter import messagebox

class GPA_Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("GPA Calculator")
        self.geometry("400x400")
        self.resizable(False, False)

        # GPA variables
        self.courses = []
        self.grades = []
        self.credits = []

        # Style
        self.style = Style(theme='superhero')

        # Language
        self.languages = ["English", "Türkçe"]
        self.language_var = tk.StringVar(value="English")

        # GUI components
        self.label_course = ttk.Label(self, text=self.get_text("Course Name"))
        self.label_course.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_course = ttk.Entry(self)
        self.entry_course.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.label_grade = ttk.Label(self, text=self.get_text("Grade"))
        self.label_grade.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_grade = ttk.Combobox(self, values=["AA", "BA", "BA+", "BB", "BB+", "CB", "CB+", "CC", "CC+", "DC", "DC+", "DD", "DD+", "FF"])
        self.entry_grade.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label_credit = ttk.Label(self, text=self.get_text("Credit"))
        self.label_credit.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_credit = ttk.Entry(self)
        self.entry_credit.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.button_add = ttk.Button(self, text=self.get_text("Add Course"), command=self.add_course)
        self.button_add.grid(row=3, column=1, columnspan=2, pady=10)

        self.button_calculate = ttk.Button(self, text=self.get_text("Calculate GPA"), command=self.calculate_gpa)
        self.button_calculate.grid(row=4, column=1, columnspan=2, pady=10)

        self.result_label = ttk.Label(self, text="")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

        self.label_change_language = ttk.Label(self, text=self.get_text("Change Language:"))
        self.label_change_language.grid(row=6, column=0, padx=10, pady=10, sticky="e")

        self.language_combobox = ttk.Combobox(self, values=self.languages, textvariable=self.language_var)
        self.language_combobox.grid(row=6, column=1, padx=10, pady=10, sticky="w")
        self.language_combobox.set(self.language_var.get())
        self.language_combobox.bind("<<ComboboxSelected>>", self.change_language)

    def get_text(self, key):
        translations = {
            "English": {
                "Course Name": "Course Name:",
                "Grade": "Grade:",
                "Credit": "Credit:",
                "Add Course": "Add Course",
                "Calculate GPA": "Calculate GPA",
                "Change Language:": "Change Language:",
                "Course added successfully.": "Course added successfully.",
                "Please enter valid information.": "Please enter valid information.",
                "Please enter valid grade (AA, BA, BA+, BB, BB+, CB, CB+, CC, CC+, DC, DC+, DD, DD+, FF).": "Please enter valid grade (AA, BA, BA+, BB, BB+, CB, CB+, CC, CC+, DC, DC+, DD, DD+, FF).",
                "Please enter course and grade.": "Please enter course and grade.",
                "GPA:": "GPA:"
            },
            "Türkçe": {
                "Course Name": "Ders Adı:",
                "Grade": "Not:",
                "Credit": "Kredi:",
                "Add Course": "Ders Ekle",
                "Calculate GPA": "GPA Hesapla",
                "Change Language:": "Dili Değiştir:",
                "Course added successfully.": "Ders başarıyla eklendi.",
                "Please enter valid information.": "Lütfen geçerli bilgileri girin.",
                "Please enter valid grade (AA, BA, BA+, BB, BB+, CB, CB+, CC, CC+, DC, DC+, DD, DD+, FF).": "Lütfen geçerli bir not girin (AA, BA, BA+, BB, BB+, CB, CB+, CC, CC+, DC, DC+, DD, DD+, FF).",
                "Please enter course and grade.": "Lütfen ders ve notu girin.",
                "GPA:": "GPA:"
            }
        }
        language = self.language_var.get()
        return translations[language][key]

    def add_course(self):
        course = self.entry_course.get()
        grade = self.entry_grade.get()
        credit = self.entry_credit.get()

        if course and isinstance(course, str) and grade and credit.isdigit():
            if grade in ["AA", "BA", "BA+", "BB", "BB+", "CB", "CB+", "CC", "CC+", "DC", "DC+", "DD", "DD+", "FF"]:
                self.courses.append(course)
                self.grades.append(grade)
                self.credits.append(int(credit))
                self.entry_course.delete(0, tk.END)
                self.entry_grade.set("")
                self.entry_credit.delete(0, tk.END)
                messagebox.showinfo(self.get_text("Course added successfully."), self.get_text("Course added successfully."))
            else:
                messagebox.showerror("Error", self.get_text("Please enter valid grade (AA, BA, BA+, BB, BB+, CB, CB+, CC, CC+, DC, DC+, DD, DD+, FF)."))
        else:
            messagebox.showerror("Error", self.get_text("Please enter valid information."))

    def calculate_gpa(self):
        if not self.courses:
            messagebox.showerror("Error", self.get_text("Please enter course and grade."))
            return

        total_weighted_grade = sum(self.grade_to_numeric(grade) * credit for grade, credit in zip(self.grades, self.credits))
        total_credits = sum(self.credits)
        gpa = total_weighted_grade / total_credits

        result_text = f"{self.get_text('GPA:')} {gpa:.2f}"
        self.result_label["text"] = result_text

    def grade_to_numeric(self, grade):
        grade_dict = {'AA': 4.0, 'BA': 3.5, 'BA+': 3.7, 'BB': 3.0, 'BB+': 3.3, 'CB': 2.5, 'CB+': 2.7, 'CC': 2.0, 'CC+': 2.3, 'DC': 1.5, 'DC+': 1.7, 'DD': 1.0, 'DD+': 1.3, 'FF': 0.0}
        return grade_dict.get(grade, 0.0)

    def change_language(self, event=None):
        # Update GUI components
        self.label_course["text"] = self.get_text("Course Name")
        self.label_grade["text"] = self.get_text("Grade")
        self.label_credit["text"] = self.get_text("Credit")
        self.button_add["text"] = self.get_text("Add Course")
        self.button_calculate["text"] = self.get_text("Calculate GPA")
        self.result_label["text"] = ""
        self.label_change_language["text"] = self.get_text("Change Language:")
        self.language_combobox.set(self.language_var.get())

if __name__ == "__main__":
    app = GPA_Calculator()
    app.mainloop()