
def main():
    print_header()
    run_event_loop()




def print_header():
    print('-------------------------------------------')
    print('              JOURNAL APP')
    print('-------------------------------------------')
    print()

def run_event_loop():

    print('What do you want to do with your journal?')
    cmd = None
    journal_data = []

    while cmd != 'x':
        cmd = input('[l]ist entries, [a]dd an entry, e[x]it: ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd != 'x':
            print("Sorry, I'm not sure what '{}' means.".format(cmd))

    print("Goodbye!")

def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for entry in entries:
        print(entry)

def add_entries(data):
    text = input('Add your entry: ')
    data = data.append(text)

main()


