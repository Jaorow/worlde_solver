class words:
    def __init__(self):
        f = open("words.txt")
        cont = f.read().splitlines()
        f.close()
        self.list = cont
        self.vowles = ["a","e","i","o","u"]
        self.known_letters = []

    def __str__(self):
        count = 0
        if len(self.list) == 1:
            string = f"There is 1 word in the list, that word is \n{self.list[0]}\nGood job!"
        else:
            string = f"\nThere are {len(self.list)} words in the list. The words are :\n"
            for i in self.list:
                count += 1
                if count < 8:
                    footer = ", "
                else:
                    footer = " \n"
                    count = 0
                string += i
                string += footer
        return string[:-2]

    def print_ln(self):
        return self.list
    
    def length(self):
        return len(self.list)

    def nul(self,letters):
        """takes one or manny letters and turns removes them from the list"""
        letters = list(letters)
        check_list = self.list
        for letter in letters:
            new_words = []
            for i in range(len(check_list)):
                if letter not in check_list[i]:
                    new_words.append(check_list[i])
            check_list = new_words
        return self.update(check_list)

    def update(self,new,letter = None):
        """a code that updates the current self.list and keeps the last in a self.last"""
        self.past = self.list
        self.past_known_letters = self.known_letters
        self.known_letters.append(letter)
        self.list = new
        return self.list
    
    def restore(self):
        try:
            if self.past != None:
                self.list = self.past
                self.past = None

                self.known_letters = self.past_known_letters

                return "list restored"
            else:
                return "Error. No backup found, please seak assistance..."
        except AttributeError:
            return "Error. No backup found, please seak assistance..."
    
    def pos(self,pos,letter):
        """known pos and letter. pass in pos then letter"""
        pos = int(pos)
        pos = pos - 1
        check_list,new_list = self.list,[]
        for word in check_list:
            if word[pos] == letter:
                new_list.append(word)
        self.update(new_list,letter)

    def let(self,pos,letter):
        """known letter but not position, pass in pos then letter."""
        pos = int(pos)
        pos = pos - 1
        check_list,new_list = self.list,[]
        for word in check_list:
            if letter in word and word[pos] != letter:
                new_list.append(word)
        self.update(new_list)

    def menu(self):
        """show things to do on the deep menu (never edditng lists just showing diffrent varaitations)"""
        print("\nWelcome to the deep menu\n\n(Press B to go back)\nPress 1 to rank with vowles\nPress 2 to see some good trys, these are letters that appear lots in the big list\n")

        inp = input("-----> ").upper()
        while inp not in "B12":
            print("\nError wrong answer, Try again.")
            inp = input("-----> ").upper()

        #dont address b, if missed will just quit deep menu
        # add more functions in below and add them above in the menu above. 

        if inp == "1":
            self.rank()
        elif inp == "2":
            self.goodtry()

    def rank(self):
        self.ranked = []
        for word in self.list:
            score = 0
            for vowle in self.vowles:
                if vowle in word:
                    score += 1
            # for other score/ai components write here and eddit score
            # current reward is one per vowel
            app = (score,word)
            self.ranked.append(app)
        self.ranked.sort()
        print(f"Good choices are...")
        for i in self.ranked[-5:]:
            print(i[1],"     ",end ="")

    def goodtry(self):
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        alpha_ranked = {}
        for letter in alpha:
            if letter in self.known_letters:
                continue
            else:
                score = 0
                index = []
                for word in self.list:
                    for i in range(len(word)):
                        if word[i] == letter:
                            index.append(i)
                            score+=1
                if score == 0:
                    continue
                else:
                    alpha_ranked[letter] = score,index
        print(alpha_ranked)


w = words()
w.nul("qwertyipghmalc")
w.pos(1,"b")
w.goodtry()
print(w)
