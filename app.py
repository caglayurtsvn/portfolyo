from flask import Flask, render_template

app = Flask(__name__)

# Proje verileri
projects = {
    "satis-analizi": {
        "title": "Power BI ile Satış Analizi",
        "category": "Power BI ile Analiz",
        "description": "Kaggle'dan alınan veri setiyle oluşturulmuş interaktif rapor.",
        "images": [
            "/static/images/powerbi.jpg",
            "/static/images/powerbi2.jpg"
        ],
        "github": "https://github.com/kullaniciadi/satis-analizi"
    },
    "toprak-sulama": {
        "title": "Toprak Sulama Sistemi",
        "category": "IoT Projesi",
        "description": "Nem sensörü ve ESP modülü ile akıllı sulama sistemi.",
        "images": [
            "/static/images/flutter_01.jpg"
        ],
        "github": "https://github.com/kullaniciadi/toprak-sulama"
    }
}

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/proje/<project_id>')
def project_detail(project_id):
    project = projects.get(project_id)
    if not project:
        return "Proje bulunamadı", 404
    return render_template('project_detail.html', project=project)

if __name__ == '__main__':
    app.run(debug=True)