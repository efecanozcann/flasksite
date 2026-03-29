from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

veriler = {
    "promosyon": [],
    "maddi": [],
    "malzeme": []
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        marka = request.form.get("marka")
        tur = request.form.get("tur")

        if not marka or not tur:
            return "Tüm alanları doldur!"

        veriler[tur].append(marka)
        return redirect(url_for("panel"))

    return render_template("index.html")


@app.route("/panel")
def panel():
    return render_template("panel.html", veriler=veriler)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))