from typing import List


def guess_lines(words: List[dict]) -> List[dict]:
    """
    lines: List[dict]
        [{start:<start-timestamp-of-text>, end:<end-timestamp-of-text>, text:<str-of-text>}, ...]
    """
    punctuation = ".,?!:;"
    lines = []
    if not words:
        return lines
    line = {
        "start": words[0]["start"],
        "end": words[0]["end"],
        "text": words[0]["text"],
    }
    words_in_line = 1
    for word in words[1:]:
        text = word["text"].rstrip()

        def concat():
            nonlocal words_in_line, line
            line["end"] = word["end"]
            if not line["text"].endswith(" ") and not text.startswith(" "):
                line["text"] += " "
            line["text"] += text
            words_in_line += 1

        def new_line():
            nonlocal words_in_line, line
            lines.append(line)
            line = {"start": word["start"], "end": word["end"], "text": text}
            words_in_line = 1


        if words_in_line >= 4 and len(line["text"]) > 0 and line["text"][-1] in punctuation:
            new_line()
        elif word["start"] - line["end"] < 2:
            concat()
        else:
            new_line()

    lines.append(line)
    return lines
