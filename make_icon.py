from PIL import Image, ImageDraw, ImageFont

def create_text_icon(output="jobbot_text.ico"):
    size = (256, 256)
    img = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Hintergrund-Kreis
    draw.ellipse((20, 20, 236, 236), fill=(0, 123, 255), outline=(0, 0, 80), width=6)

    # Schrift (JB)
    try:
        font = ImageFont.truetype("arial.ttf", 120)
    except:
        font = ImageFont.load_default()

    text = "JB"
    bbox = draw.textbbox((0, 0), text, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x, y = (size[0] - w) // 2, (size[1] - h) // 2

    draw.text((x, y), text, font=font, fill="white")

    img.save(output, format="ICO", sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
    print(f"✅ Icon mit Text gespeichert als {output}")


def create_lupe_icon(output="jobbot_lupe.ico"):
    size = (256, 256)
    img = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Hintergrund-Kreis
    draw.ellipse((20, 20, 236, 236), fill=(40, 100, 200), outline=(0, 0, 80), width=6)

    # Lupe: Glas
    draw.ellipse((80, 80, 160, 160), outline="white", width=10)

    # Griff
    draw.line((150, 150, 200, 200), fill="white", width=12)

    img.save(output, format="ICO", sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
    print(f"✅ Icon mit Lupe gespeichert als {output}")


if __name__ == "__main__":
    create_text_icon()
    create_lupe_icon()
    print("🎉 Beide Icons fertig!")
