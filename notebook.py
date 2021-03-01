import datetime


# Store the next available id for all new notes
last_id = 0


class Note:
    '''
    Represent a note in the notebook. Match against a
    string in searches and store tags for each note.
    '''
    def __init__(self, memo, tags=''):
        '''
        Initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        # Make a unique note id
        self.id = ''.join(str(datetime.datetime.now().timestamp()).split('.'))
    
    def match(self, filter_param):
        '''
        Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags.
        '''
        return filter_param in self.memo or filter_param in self.tags



class Notebook:
    '''Represent a collection of notes that can be tagged,
    modified, and searched.'''

    def __init__(self):
        '''
        Initialize a notebook with an empty list.
        '''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''
        Create a new note and add it to the list.
        '''
        self.notes.append(Note(memo, tags))

    def modify(self, note_id, memo, tags):
        '''
        Find the note with the given id and change its
        memo to the given value.
        '''
        # Check if id is the same and if it is, change the note
        # I made it work with tags and memos simultaniously
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                note.tags = tags
                break

    def search(self, filter_param):
        '''
        Find all notes that match the given filter
        string.
        '''
        # Uses a note.match to match notes
        return [note for note in self.notes if note.match(filter_param)]