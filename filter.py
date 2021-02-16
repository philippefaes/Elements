import re

def filter(name):
    text = open(name).readlines()
    newtext=[]
    while text:
        line = text.pop(0)
        # if "\\begin{Parallel}{}{}" in line:
            # while not("\ParallelRText{" in line):
                # #print (line)
                # line = text.pop(0)
            # line = text.pop(0)
        # if "\\end{Parallel}" in line:
            # newtext[-1] = newtext[-1].strip()[:-1]
            # newtext.append('~\\nline\n') # add vertical space after paragraph
        
        if "pdfbookmark[0]" in line:
            chaptername = line.split('{')[1][:-1]
            line = ( f"\\cleardoublepage \n"
                     f"{line}"
                     f"\\addcontentsline{{toc}}{{chapter}}{{{chaptername}}}\n"
                     )
        if "\\lhead" in line: line = "" #skip
        # line = line.replace("\\begin{Parallel}{}{}", "\\begin{Parallel}{0pt}{}")
        line = line.replace("\\rhead{", "\\chead{")
        line = line.replace("{\\Huge\\sf EUCLID'S ELEMENTS OF GEOMETRY}\\\\",
                            "{\\Huge\\sf EUCLID'S \\\\ \\spa ELEMENTS OF GEOMETRY}\\\\")
        # clean up chapter 10 Corollary to proposition 111
        vs="\\vspace*{-7pt}"
        xs= ["Medial,",
             "Binomial,",
             "First bimedial,",
             "Second bimedial,",
             "Major,",
             "Square-root of a rational plus a medial (area),",
             "Square-root of (the sum of) two medial (areas),",
             "Apotome,",
             "First apotome of a medial,",
             "Second apotome of a medial,",
             "Minor,",
             "That which with a rational (area) produces a medial whole,"]
        for x in xs:
            line = line.replace(x+vs, x) 

        line = line.replace("[Prop.~","[Prop. ")
        line = line.replace("{\\footnotesize","\n\n\\vspace{7pt}{\\footnotesize")
        
        line = line.replace("[Def.~","[Def. ")
        newtext.append(line)
    
    
    target = name.replace(".tex", "_en.tex")
    open(target,'w').writelines(newtext)
    
for i in range(1,14):
    name = f"book{i:02}/book{i}.tex"
    filter(name)
