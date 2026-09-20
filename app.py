import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    senha = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%&*")
    ]
    for _ in range(tamanho - 4):
        senha.append(random.choice(caracteres))
    random.shuffle(senha)
    return "".join(senha)

def main():
    print("🔐 GERADOR DE SENHAS - Luanda\n")
    try:
        t = input("Tamanho [12]: ") or "12"
        tamanho = int(t)
    except:
        tamanho = 12
    print("\n✅ 5 Senhas Geradas:")
    print("-" * 35)
    for i in range(5):
        print(f"{i+1}. {gerar_senha(tamanho)}")
    print("-" * 35)

if __name__ == "__main__":
    main()
