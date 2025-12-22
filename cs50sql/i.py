from fpdf import FPDF


def main():
    name = input("Name: ").strip()

    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()

    # Titre
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 20, "CS50 Shirtificate", align="C")
    pdf.ln(20)

    # Image du t-shirt (centrée)
    pdf.image("shirtificate.png", x=10, y=40, w=190)

    # Texte du nom (blanc, sur le t-shirt)
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=55, y=140, text=f"{name} took CS50")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
