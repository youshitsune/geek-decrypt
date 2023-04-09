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
        "GTW": "Geek of Technical Writing",
        "GO": "Geek of Other. Some types of geeks deviate from the normal geek activities. This is encouraged as true geeks come from all walks of life.",
        "GU": "Geek of 'Undecided'. This is a popular vocation with incoming freshmen.",
        "G!": "Geek of no qualifications. A rather miserable existence, you would think.",
        "GAT": "Geek of All Trades. For those geeks that can do anything and everything. GAT usually precludes the use of other vocational descriptors.",
        "d++": "I tend to wear conservative dress such as a business suit or worse, a tie.",
        "d+": "Good leisure-wear. Slacks, button-shirt, etc. No jeans, tennis shoes, or t-shirts.",
        "d": "I dress a lot like those found in catalog ads. Bland, boring, without life or meaning.",
        "d-": "I'm usually in jeans and a t-shirt.",
        "d--": "My t-shirts go a step further and have a trendy political message on them.",
        "d---": "Punk dresser, including, but not limited to, torn jeans and shirts, body piercings, and prominent tattoos.",
        "dx": "Cross Dresser",
        "d?": "I have no idea what I am wearing right now, let alone what I wore yesterday.",
        "!d": "No clothing. Quite a fashion statement, don't you think?",
        "dpu": "I wear the same clothes all the time, no matter the occasion, forgetting to do laundry between wearings."
        }

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

