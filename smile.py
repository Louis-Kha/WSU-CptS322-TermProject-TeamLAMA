from app import create_app, db
from app.Model.models import Post, Tag, progLang

# ijk = False

# def change_global():
#     global ijk
#     ijk = True

# choice = ""
# if ijk == False:
#     print("Test1")
#     print("1: Student Regisration Automation")
#     print("2: Faculty Registration Automation")
#     print("3: Student Login")
#     print("4: Faculty Login")
#     choice = input("Please input the choice of the automation you would like to run: ")
#     change_global()
# else:
#    pass
app = create_app()
# print("test test test")
# ijk = False

# def change_global():
#     global ijk
#     ijk = True

# choice = ""
# if ijk == False:
#     print("Test1")
#     print("1: Student Regisration Automation")
#     print("2: Faculty Registration Automation")
#     print("3: Student Login")
#     print("4: Faculty Login")
#     choice = input("Please input the choice of the automation you would like to run: ")
#     change_global()
# else:
#     pass
# print("----------------------------------Outside")
# done here
@app.before_first_request
def initDB(*args, **kwargs):
    db.create_all()
    print("----------------------------------We In Here")
# -------- Added By Alex -----------
    if progLang.query.count() == 0:
        print("----------------------------------Inside ProgLang")
        languages = ['C ', 'C# ', 'C++ ', 'Java ', 'JavaScript ', 'R ', 'Swift ', 'Python ', 'PHP ', 'Swift ', 'Dart ','Kotlin ','MATLAB ','Perl ','Ruby ','Rust ', 'Scala ']
        for language in languages:
            db.session.add(progLang(name = language))
        db.session.commit()
# ----------------------------------

if __name__ == "__main__":
    app.run(debug=True)