from app import create_app, db
from app.Model.models import Post, Tag, progLang, researchFieldTags 

app = create_app()
print("----------------------------------Outside")
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

    if researchFieldTags.query.count() == 0:
        researchFields = ['DataBases ', 'AI', 'System Security']
        for researchField in researchFields:
            db.session.add(researchFieldTags(name = researchField))
        db.session.commit()
# ----------------------------------

if __name__ == "__main__":
    app.run(debug=True)