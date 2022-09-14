# Mise en place des fonctions lose() et win()

def lose() :
    print('Vous avez perdu...\n')
    while True :
        choice = input('Voulez-vous recommencer ? (y/n)')

        if choice.upper() == 'Y' :         # Si on choisit de continuer quand on perd, alors 'again' reste True
          return True
          break           

        elif choice.upper() == 'N' :         # Sinon, 'again' devient False
          return False
          break

        else :
            print('Veuillez rentrer soit "y" ou "n"')         # Si l'on se trompe de caractère on redemande
            continue

def win(turns) :
    assert isinstance(turns,int) == True
    print('Vous avez gagné en', turns, 'tours !\n')
    while True :
        choice = input('Voulez-vous recommencer ? (y/n) ')

        if choice.upper() == 'Y' :         # Pareil que lose()
          return True
          break

        elif choice.upper() == 'N' :
          return False
          break

        else :
          print('Veuillez rentrer soit "y" ou "n"')
          continue


authorized = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

specials_a = ['à', 'á', 'â', 'ã', 'ä', 'å']
specials_e = ['è', 'é', 'ê', 'ë']
specials_i = ['ì', 'í', 'î', 'ï']
specials_o = ['ò', 'ó', 'ô', 'õ', 'ö']
specials_u = ['ù', 'ú', 'û', 'ü']
specials_y = ['ý', 'ÿ']
specials_n = ['ñ']

pendus = ['    ____________\n      |        |\n      |        o\n      |       /|\ \n      |        |\n      |       / \ \n      |\n      |\n___ __|___', '    ____________\n      |        |\n      |        o\n      |       /|\ \n      |        |\n      |\n      |\n      |\n___ __|___', '    ____________\n      |        |\n      |        o\n      |        |\n      |        |\n      |\n      |\n      |\n___ __|___', '    ____________\n      |        |\n      |        o\n      |\n      |\n      |\n      |\n      |\n___ __|___', '    ____________\n      |\n      |\n      |\n      |\n      |\n___ __|___', '      |\n      |\n      |\n      |\n      |\n___ __|___', '___ __|___']

# La liste 'pendus' correspond aux dessins ASCII, avec le dessin qui s'affiche à x vies au rang x (exemple : le dessin à 5 vies est pendu[5])

again = True        # Variable qui n'est utilisée que lorsque l'on recommence une partie
while again :
  while True :

      count = 0         # Variable qui compte le nombre de lettres autorisées dans le mot à trouver
      word = input('Proposez un mot secret : ')
      word = list(word)

      for number in range(len(word)) :         # On remplace toutes les lettres avec des accents par leur lettre de base

          if word[number] in specials_a :
              word[number] = 'a'
          elif word[number] in specials_e :
              word[number] = 'e'
          elif word[number] in specials_i :
              word[number] = 'i'
          elif word[number] in specials_o :
              word[number] = 'o'
          elif word[number] in specials_u :
              word[number] = 'u'
          elif word[number] in specials_y :
              word[number] = 'y'
          elif word[number] in specials_n :
              word[number] = 'n'

      word = (''.join(word))
      word = word.upper()

      for letter in word :

          if letter in authorized :         # Si la lettre est autorisée, alors on ajoute "1" à la variable 'count'
              count += 1

          else :          # Si la lettre n'est pas autoris�e, alors on revient au début de la boucle et on réinitialise la variable 'count' en redemandant un autre mot à trouver
              print("Des caract�res ne sont pas autoris�s...")
              break

      if count == len(word) :         # Quand toutes les lettres du mot sont autorisées, alors on peut commencer le pendu et on réinitialise la variable 'count' pour la suite
          count = 0
          break

  life = 7          # Définition d'une variable pour le nombre de vies du joueur
  game_on = True
  turns = 0

  guess = str()                       #}
  for letter in range (len(word)) :   #} Ce bloc correspond à la création de 'guess', qui est le mot à trou que l'on va afficher au joueur
      guess += '_ '                   #} 

  said = []         # Dans cette liste, on ajoute toutes les lettres déjà utilisées

  print('\nLe mot à trouver est le suivant :\n', guess, '\n\nVous avez', life, 'vies.\n')

  while game_on :         # Toute cette boucle correspond à un tour qui ne s'arrête que lorsque l'on perd ou l'on gagne
    turns += 1

    attempt = input('Proposez une lettre : ')
    attempt = attempt.upper()         # Encore une fois, on met tout en majuscule par soucis de simplicité

    if len(attempt) != 1 :          # On s'assure qu'il n'y ai qu'un seul caractère entré
        print("Veuillez ne rentrer qu'une seule lettre !")
        continue

    elif attempt not in authorized :          # On s'assure que c'est un caractère autorisé présent dans la liste 'authorized' (donc forcément une lettre)
        life -= 1
        print('\nVeuillez mettre un caractère autorisé !\n\nVous avez', life, 'vies.\n')

        if life <= 0 :
            assert life <= 0
            print(pendus[life])
            game_on = False
            again = lose()

        elif life < 7 :         # Puisque le pendu ne commence pas à apparaitre lorsque l'on a 7 vies, on vérifie si le joueur en a - avant de la faire apparaitre
            assert life < 7
            print(pendus[life])

        continue

    elif attempt in said :          # On vérifie que la lettre n'ai pas déjà été utilisée
      life -= 1
      print('\nLa lettre a déjà été utilisée !\n', guess, '\n\nVous avez', life, 'vies.\n')

      if life <= 0 :
          assert life <= 0
          print(pendus[life])
          game_on = False
          again = lose()

      elif life < 7 :
        assert life < 7
        print(pendus[life])

      continue

    said.append(attempt)          # On ajoute la lettre entrée dans la liste des lettres déjà utlisées
    guess = list(guess)         # On transforme 'guess' en liste pour pouvoir changer des éléments selon leur rang
    right = False

    for letter in range (len(word)) :         # Dans cette boucle, on vérifie si la lettre proposée est dans le mot
        if attempt == word[letter] :          # Si elle l'est, on remplace le '_' de 'guess' par la lettre
          assert attempt == word[letter]
          count += 1
          guess[letter * 2] = attempt
          right = True

    guess = (''.join(guess))

    if not right :          # Si la lettre n'est pas dans le mot, alors on perd une vie et on affiche l'état du pendu
      life -= 1
      print("\nLa lettre n'est pas dans le mot !\n", guess, '\n\nVous avez', life, 'vies.\n')

    else :          # Si elle l'est, alors on affiche le nombre de fois où elle apparait
      print('\nLa lettre est dans le mot et elle y apparait', count, 'fois !\n', guess, '\n\nVous avez', life, 'vies.\n')


    if life <= 0 :
        assert life <= 0
        print(pendus[life])
        game_on = False
        again = lose()

    elif life < 7 :
      assert life < 7
      print(pendus[life])


    result = list(guess)          # On transforme 'guess' en liste pour la modifier + facilement

    while len(result) > len(word) :         # On supprime tous les espaces de la liste (entre les '_')
        assert len(result) > len(word)  
        result.remove(' ')

    result = (''.join(result))

    if result == word :
      assert result == word  
      game_on = False
      again = win(turns)