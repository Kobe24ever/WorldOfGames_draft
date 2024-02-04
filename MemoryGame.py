import random
import time


def play_memory_game(difficulty):
    generate_sequence = []
    for i in range(0, difficulty):
        generate_sequence.append(random.randint(1, 101))

    # Print the generated sequence
    print(generate_sequence, end='', flush=True)
    time.sleep(0.7)

    # Clear the printed sequence by printing spaces and carriage return
    print('\r' + ' ' * len(str(generate_sequence)), end='', flush=True)
    time.sleep(0.7)

    get_list_from_user = []
    for i in range(0, difficulty):
        get_list_from_user.append(int(input("\nPlease add a number you think was on this list: ")))

    print(f"\nThe generated list: {generate_sequence}")
    print(f"User guess: {get_list_from_user}")

    def is_list_equal(generate_sequence, get_list_from_user):
        return sorted(generate_sequence) == sorted(get_list_from_user)

    # Check if the lists are the same
    if is_list_equal(generate_sequence, get_list_from_user):
        print("You won!!!")
        return {'success': True, 'difficulty': difficulty}
    else:
        print("You Lost :(")
        return {'success': False, 'difficulty': difficulty}

