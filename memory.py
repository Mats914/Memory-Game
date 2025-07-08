import random
import time

def generate_sequence(level):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return random.sample(chars, level)

def play_game():
    print("Välkommen till Memory-spelet!")
    level = int(input("Välj svårighetsgrad (antal tecken, t.ex. 3, 5, 7): "))

    original = generate_sequence(level)
    print("\nMemorera denna sekvens:")
    print(' '.join(original))
    time.sleep(3)  # Visa i 3 sekunder

    print("\n" * 50)  # Rensa skärmen visuellt

    shuffled = original[:]
    random.shuffle(shuffled)
    print("Här är de blandade tecknen:")
    print(' '.join(shuffled))

    guess = input("Skriv in den ursprungliga sekvensen (utan mellanslag): ").upper()
    while list(guess) != original:
        print("Fel. Försök igen.")
        guess = input("Skriv in den ursprungliga sekvensen igen: ").upper()

    print("Rätt! Du klarade det! 🎉")

if __name__ == "__main__":
    play_game()
