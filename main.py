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
        "dpu": "I wear the same clothes all the time, no matter the occasion, forgetting to do laundry between wearings.",
        "s+++": "I usually have to duck through doors.",
        "s++": "I'm a basketball candidate.",
        "s+": "I'm a little taller than most.",
        "s": "I'm a geek of average height.",
        "s-": "I look up to most people.",
        "s--": "I look up to damn near everybody.",
        "s---": "I take a phone book with me when I go out so I can see to eat dinner.",
        "+++": "I take up three movie seats.",
        "++": "I'm a linebacker candidate.",
        "+": "I'm a little rounder than most.",
        " ": "I'm a geek of average roundness.",
        "-": "Everyone tells me to gain a few pounds.",
        "--": "I tend to have to fight against a strong breeze.",
        "---": "My bones are poking through my skin.",
        "a+++": "60 and up",
        "a++": "50-59",
        "a+": "40-49",
        "a": "30-39",
        "a-": "25-29",
        "a--": "20-24",
        "a---": "15-19",
        "a----": "10-14",
        "a-----": "9 and under (Geek is training?)",
        "a?": "immortal",
        "!a": "it's none of your business how old I am",
        "C++++": "I'll be first in line to get the new cybernetic interface installed into my skull.",
        "C+++": "You mean there is life outside of Internet? You're shittin' me! I haven't dragged myself to class in weeks.",
        "C++": "Computers are a large part of my existence. When I get up in the morning, the first thing I do is log myself in. I play games or mud on weekends, but still manage to stay off of academic probation.",
        "C+": "Computers are fun and I enjoy using them. I play a mean game of DOOM! and can use a word processor without resorting to the manual too often. I know that a 3.5\" disk is not a hard disk. I also know that when it says 'press any key to continue', I don't have to look for a key labeled 'ANY'.",
        "C": "Computers are a tool, nothing more. I use it when it serves my purpose.",
        "C-": "Anything more complicated than my calculator and I'm screwed.",
        "C--": "Where's the on switch?",
        "C---": "If you even mention computers, I will rip your head off!",
        "B": "BSD",
        "L": "Linux",
        "U": "Ultrix",
        "A": "AIX",
        "V": "SysV",
        "H": "HPUX",
        "I": "IRIX",
        "O": "OSF/1",
        "S": "Sun OS/Solaris",
        "C": "SCO Unix",
        "X": "NeXT",
        "*": "Some other not listed",
        "U++++": "I am the sysadmin. If you try and crack my machine don't be surprised if the municipal works department gets an "accidental" computer-generated order to put start a new landfill on your front lawn or your quota is reduced to 4K.",
        "U+++": "I don't need to crack /etc/passwd because I just modified su so that it doesn't prompt me. The admin staff doesn't even know I'm here. If you don't understand what I just said, this category does NOT apply to you!",
        "U++": "I've get the entire admin ticked off at me because I am always using all of the CPU time and trying to run programs that I don't have access to. I'm going to try cracking /etc/passwd next week, just don't tell anyone.",
        "U+": "I not only have a Unix account, but I slam VMS any chance get.",
        "U": "I have a Unix account to do my stuff in",
        "U-": "I have a VMS account.",
        "U--": "I've seen Unix and didn't like it. DEC rules!",
        "U---": "Unix geeks are actually nerds in disguise."
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

