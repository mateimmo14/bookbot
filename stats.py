from curses import nl
from traceback import print_exc


def count_words(book_text):
    book_words = book_text.split()
    num_words = 0
    for word in book_words:
        num_words += 1
    print(f"Found {num_words} total words")


def count_characters(book_text):
    book_text = book_text.lower()  # <-- This is the missing part

    a = b = c = d = e = f = g = h = i = j = k = l = m = n = o = p = q = r = s = t = (
        u
    ) = v = w = x = y = z = 0

    book_words = book_text.split()
    for word in book_words:
        for letter in word:
            if letter.isalpha():  # simpler way to ignore punctuation
                if letter == "a":
                    a += 1
                elif letter == "b":
                    b += 1
                elif letter == "c":
                    c += 1
                elif letter == "d":
                    d += 1
                elif letter == "e":
                    e += 1
                elif letter == "f":
                    f += 1
                elif letter == "g":
                    g += 1
                elif letter == "h":
                    h += 1
                elif letter == "i":
                    i += 1
                elif letter == "j":
                    j += 1
                elif letter == "k":
                    k += 1
                elif letter == "l":
                    l += 1
                elif letter == "m":
                    m += 1
                elif letter == "n":
                    n += 1
                elif letter == "o":
                    o += 1
                elif letter == "p":
                    p += 1
                elif letter == "q":
                    q += 1
                elif letter == "r":
                    r += 1
                elif letter == "s":
                    s += 1
                elif letter == "t":
                    t += 1
                elif letter == "u":
                    u += 1
                elif letter == "v":
                    v += 1
                elif letter == "w":
                    w += 1
                elif letter == "x":
                    x += 1
                elif letter == "y":
                    y += 1
                elif letter == "z":
                    z += 1

    return {
        "a": a,
        "b": b,
        "c": c,
        "d": d,
        "e": e,
        "f": f,
        "g": g,
        "h": h,
        "i": i,
        "j": j,
        "k": k,
        "l": l,
        "m": m,
        "n": n,
        "o": o,
        "p": p,
        "q": q,
        "r": r,
        "s": s,
        "t": t,
        "u": u,
        "v": v,
        "w": w,
        "x": x,
        "y": y,
        "z": z,
    }
