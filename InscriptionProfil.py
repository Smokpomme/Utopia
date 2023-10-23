import json

# Modèle de données pour les utilisateurs
users = []


# Fonction pour créer un compte utilisateur
def create_user(username, email, password, size, gender, style_preferences):
  user = {
      "username": username,
      "email": email,
      "password": password,
      "size": size,
      "gender": gender,
      "style_preferences": style_preferences
  }
  users.append(user)
  save_users_to_file()


# Fonction pour enregistrer les utilisateurs dans un fichier JSON
def save_users_to_file():
  with open('users.json', 'w') as file:
    json.dump(users, file)


# Fonction pour charger les utilisateurs depuis un fichier JSON
def load_users_from_file():
  try:
    with open('users.json', 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []


# Charger les utilisateurs existants lors du démarrage de l'application
users = load_users_from_file()


# Menu principal de l'application
def main_menu():
  while True:
    print("Bienvenue dans l'application de vêtements!")
    print("1. Créer un compte utilisateur")
    print("2. Se connecter")
    print("3. Quitter")
    choice = input("Choisissez une option : ")

    if choice == '1':
      create_account()
    elif choice == '2':
      login()
    elif choice == '3':
      break
    else:
      print("Option invalide. Veuillez choisir une option valide.")


# Fonction pour créer un compte utilisateur
def create_account():
  username = input("Nom d'utilisateur : ")
  email = input("Adresse e-mail : ")
  password = input("Mot de passe : ")
  size = input("Taille : ")
  gender = input("Sexe : ")
  style_preferences = input(
      "Préférences de style (séparées par des virgules) : ").split(',')

  create_user(username, email, password, size, gender, style_preferences)
  print("Compte utilisateur créé avec succès!")


# Fonction pour se connecter
def login():
  email = input("Adresse e-mail : ")
  password = input("Mot de passe : ")

  user = find_user_by_email(email)
  if user and user["password"] == password:
    print(f"Connecté en tant que {user['username']}")
  else:
    print(
        "Échec de la connexion. Veuillez vérifier votre adresse e-mail et votre mot de passe."
    )


# Fonction pour trouver un utilisateur par adresse e-mail
def find_user_by_email(email):
  for user in users:
    if user['email'] == email:
      return user
  return None


if __name__ == '__main__':
  main_menu()
