geek_code = input("Input geek code: ")

geek_code = geek_code.split()

flags = {
        "GB": "Geek of Business",
        "GC": "Geek of Classics",
        "GCA": "Geek of Commercial Arts",
        "GCM": "Geek of Computer Management",
        "GCS": "Geek of Computer Science",
        "GCC": "Geek of Communications",
        "GE": "Geek of Engineering",
        "GED": "Geek of Education",
        "GFA": "Geek of Fine Arts",
        "GG": "Geek of Government",
        "GH": "Geek of Humanities",
        "GIT": "Geek of Information Technology",
        "GJ": "Geek of Jurisprudence (Law)",
        "GLS": "Geek of Library Science",
        "GL": "Geek of Literature",
        "GMC": "Geek of Mass Communications",
        "GM": "Geek of Math",
        "GMD": "Geek of Medicine",
        "GMU": "Geek of Music",
        "GPA": "Geek of Performing Arts",
        "GP": "Geek of Philosophy",
        "GS": "Geek of Science (Physics, Chemistry, Biology, etc.)",
        "GSS": "Geek of Social Science (Psychology, Sociology, etc.)",
        "GTW": "Geek of Technical Writing"}

dec = []
for i in geek_code:
    if len(i.split("/")) == 1:
        dec.append(flags[i])
    else:
        for j in i.split("/"):
            if j.startswith("G"):
                dec.append(flags[j])
            else:
                dec.append(flags["G"+j])


print(";".join(dec))

