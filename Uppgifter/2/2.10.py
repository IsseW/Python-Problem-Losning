"""
Övning 2.10 - Hitta och ersätt
Skriv en funktion find_and_replace(find_str, replace_str, infile, outfile) som söker igenom filen infile och ersätter alla förekomster av find_str med replace_str.
Resultat-texten ska sparas i filen outfile.
"""


def find_and_replace(find_str, replace_str, infile, outfile):
    infile = open(infile, "r")
    in_text = infile.read()
    infile.close()

    out_text = ""
    i = 0
    while i < len(in_text):
        if (
            i + len(find_str) <= len(in_text)
            and in_text[i : i + len(find_str)] == find_str
        ):
            out_text += replace_str
            i += len(find_str)
        else:
            out_text += in_text[i]
            i += 1
    outfile = open(outfile, "w")
    outfile.write(out_text)
    outfile.close()


infile = "Alice.txt"
outfile = "test-2.10.txt"

find_and_replace("Rabbit", "Cat", infile, outfile)