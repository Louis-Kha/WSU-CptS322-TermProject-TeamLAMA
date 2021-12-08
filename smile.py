from app import create_app, db
from app.Model.models import progLang, researchFieldTags, majorT, researchPostFieldTags, technicalCourses

app = create_app()

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

    if researchFieldTags.query.count() == 0 or researchPostFieldTags.query.count == 0:
        researchFields = ['DataBases ', 'AI', 'System Security']
        for researchField in researchFields:
            db.session.add(researchFieldTags(name = researchField))
            db.session.add(researchPostFieldTags(name = researchField))
        db.session.commit()

    if majorT.query.count() == 0: 
        majors = ['Computer Science', 'Electrical Engineering']
        for major in majors:
            db.session.add(majorT(name = major))
        db.session.commit()

    if technicalCourses.query.count() == 0: 
        tCourses = ['CptS 111', 'CptS 121', 'CptS 122', 'CptS 302']
        for course in tCourses:
            db.session.add(technicalCourses(name = course))
        db.session.commit()

    
# ----------------------------------

if __name__ == "__main__":
    app.run(debug=True)