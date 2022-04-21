def get_vowels(text: str) -> int:
    vowels = 'aeiouáàãâéêíóõôúü'
    text = text.lower()
    vs = 0

    for c in text:
        if c in vowels:
            vs += 1

    return vs

def main():
    filename = 'faroeste.txt'
    f = open(filename)
    vs = 0

    for line in f:
        vs += get_vowels(line.strip())

    f.close()
    print(f"Encontrei {vs} vogais na letra da música Faroeste Caboclo")

if __name__ == '__main__':
    main()
