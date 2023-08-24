nucleoditos = {
    "A":"Adenina",
    "C":"Citosina",
    "G":"Guanina",
    "T":"Timina",
}

print len(nucleotidos)
print (nucleotidos)

print (nucleotidos ["A"])
print (nucleotidos ["C"])
print (nucleotidos ["t"])
print (nucleotidos ["G"])

nucleotidos ["A"] = "ADENINA"
nucleotidos ["C"] = "CITOSINA"
nucleotidos ["G"] = "GUANINA"
nucleotidos ["T"] = "TIMINA"

print (nucleotidos)
nucleotidos.pop ("T", non)
nucleotidos.pop ("G", non)
nucleotidos.pop ("C", non)
nucleotidos.pop ("A", non)
print (nucleotidos)
