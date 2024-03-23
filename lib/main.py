import sqlite3

connection = sqlite3.connect('scoreboard.db')
cursor = connection.cursor()

def create_database():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS participants (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            chickenwings INTEGER DEFAULT 0,
            hamburgers INTEGER DEFAULT 0,
            hotdogs INTEGER DEFAULT 0
        );
    ''')
    connection.commit()

def save(participants):

    for participant in participants:
        cursor.execute('''
            INSERT INTO participants (name, chickenwings, hamburgers, hotdogs)
            VALUES (?, ?, ?, ?)
        ''', (participant['name'], participant.get('chickenwings', 0),
              participant.get('hamburgers', 0), participant.get('hotdogs', 0)))

    connection.commit()


participants = [
    {'name': 'Habanero Hillary', 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': 'Big Bob', 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]

save(participants)

connection.close()

class Scoreboard:
    @staticmethod
    def calculate_score(participant):
        chickenwings_score = participant.get('chickenwings', 0) * 5
        hamburgers_score = participant.get('hamburgers', 0) * 3
        hotdogs_score = participant.get('hotdogs', 0) * 2
        total_score = chickenwings_score + hamburgers_score + hotdogs_score
        return total_score

    @staticmethod
    def sort_participants(participants):
        sorted_participants = sorted(participants, key=lambda p: (-Scoreboard.calculate_score(p), p['name']))
        return [{'name': p['name'], 'score': Scoreboard.calculate_score(p)} for p in sorted_participants]

    def select_winner(participants):
        sorted_participants = Scoreboard.sort_participants(participants)
        if sorted_participants:
            return sorted_participants[0]  # Return the first participant (winner) from the sorted list
        else:
            return None


sorted_participants = Scoreboard.sort_participants(participants)
print(sorted_participants)
winner = Scoreboard.select_winner(participants)
print("Winner:", winner)
