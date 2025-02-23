def wrap_text(text, font, max_width, draw):
    # Helps to wrap text to not overlap edge
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        text_width = draw.textbbox((0, 0), test_line, font=font)[2] - draw.textbbox((0, 0), test_line, font=font)[0]

        if text_width <= max_width:
            current_line = test_line
        else:
            if current_line:  # Only append if current_line is not empty
                lines.append(current_line)
            current_line = word  # Start a new line with this word

    if current_line:  # Add the last line if it exists
        lines.append(current_line)

    return lines