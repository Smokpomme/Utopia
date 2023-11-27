import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
import json

# Acceuil
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application principale")
        self.geometry("500x500")
      
        self.menu_label = tk.Label(self, text="Choisissez une fonctionnalité:")
        self.menu_label.pack(pady=10)
      
        self.login_button = tk.Button(self, text="Se Connecter / S'enregistrer", command=self.open_login_register)
        self.login_button.pack()

        self.catalogue_button = tk.Button(self, text="Catalogue de Vêtements", command=self.open_catalogue_app)
        self.catalogue_button.pack()

        self.wishlist_button = tk.Button(self, text="Liste de Souhaits", command=self.open_wishlist_app)
        self.wishlist_button.pack()

        self.wardrobe_button = tk.Button(self, text="Garde-Robe", command=self.open_wardrobe_app)
        self.wardrobe_button.pack()
      
        self.produits_button = tk.Button(self, text="Système de Notation et Avis sur les Produits", command=self.open_produits_app)
        self.produits_button.pack()

        self.article_sharing_button = tk.Button(self, text="Partage d'Articles", command=self.open_article_sharing_app)
        self.article_sharing_button.pack()

        self.cart_button = tk.Button(self, text="Panier d'Achats", command=self.open_cart_app)
        self.cart_button.pack()
      
        self.quit_button = tk.Button(self, text="Quitter", command=self.destroy)
        self.quit_button.pack(pady=20)

    def open_produits_app(self):
        produits_app = ProduitsApp(self)

    def open_catalogue_app(self):
        catalogue_app = ClothingCatalog(self)

    def open_article_sharing_app(self):
        article_sharing_app = ArticleSharingApp(self)

    def open_wardrobe_app(self):
        wardrobe_app = WardrobeApp(self)

    def open_clothing_app(self):
        clothing_app = ClothingApp(self)

    def open_wishlist_app(self):
        wishlist_app = WishlistApp(self)

    def open_cart_app(self):
        cart_app = CartApp(self)

    def open_login_register(self):
      login_register = enregistreLog(self)

# Fonction s'enregistrer et se login
class enregistreLog(tk.Toplevel):
    def __init__(self, master):
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


      # Fonction pour créer un compte utilisateur avec une interface Tkinter
      def create_account():
          def save_user():
              username = username_entry.get()
              email = email_entry.get()
              password = password_entry.get()
              size = size_entry.get()
              gender = gender_entry.get()
              style_preferences = style_entry.get().split(',')

              create_user(username, email, password, size, gender, style_preferences)
              messagebox.showinfo("Succès", "Compte utilisateur créé avec succès!")
              top.destroy()

          top = tk.Toplevel()
          top.title("Créer un compte utilisateur")

          username_label = tk.Label(top, text="Nom d'utilisateur:")
          username_label.pack()
          username_entry = tk.Entry(top)
          username_entry.pack()

          email_label = tk.Label(top, text="Adresse e-mail:")
          email_label.pack()
          email_entry = tk.Entry(top)
          email_entry.pack()

          password_label = tk.Label(top, text="Mot de passe:")
          password_label.pack()
          password_entry = tk.Entry(top, show="*")
          password_entry.pack()

          size_label = tk.Label(top, text="Taille (Ex : 180 si 1m80):")
          size_label.pack()
          size_entry = tk.Entry(top)
          size_entry.pack()

          gender_label = tk.Label(top, text="Sexe:")
          gender_label.pack()
          # Créer un Combobox pour le champ "Sexe"
          gender_combobox = ttk.Combobox(top, values=["Homme", "Femme"])
          gender_combobox.pack()

          style_label = tk.Label(top, text="Préférences de style:")
          style_label.pack()
          # Créer un Combobox pour les préférences de style avec les options spécifiées
          style_combobox = ttk.Combobox(top, values=["Streetwear", "Décontracté", "Classique", "Chic", "Vintage"])
          style_combobox.pack()


          create_button = tk.Button(top, text="Créer un compte", command=save_user)
          create_button.pack()


      # Fonction pour se connecter avec une interface Tkinter
      def login():
          def check_login():
              email = email_entry.get()
              password = password_entry.get()

              user = find_user_by_email(email)
              if user and user["password"] == password:
                  messagebox.showinfo("Succès", f"Connecté en tant que {user['username']}")
              else:
                  messagebox.showerror("Échec de la connexion", "Veuillez vérifier votre adresse e-mail et votre mot de passe.")
              top.destroy()

          top = tk.Toplevel()
          top.title("Se connecter")

          email_label = tk.Label(top, text="Adresse e-mail:")
          email_label.pack()
          email_entry = tk.Entry(top)
          email_entry.pack()

          password_label = tk.Label(top, text="Mot de passe:")
          password_label.pack()
          password_entry = tk.Entry(top, show="*")
          password_entry.pack()

          login_button = tk.Button(top, text="Se connecter", command=check_login)
          login_button.pack()


      # Fonction pour trouver un utilisateur par adresse e-mail
      def find_user_by_email(email):
          for user in users:
              if user['email'] == email:
                  return user
          return None


      if __name__ == '__main__':
          root = tk.Tk()
          root.title("Application de vêtements")

          create_account_button = tk.Button(root, text="Créer un compte utilisateur", command=create_account)
          create_account_button.pack()

          login_button = tk.Button(root, text="Se connecter", command=login)
          login_button.pack()

          quit_button = tk.Button(root, text="Quitter", command=root.destroy)
          quit_button.pack()

          root.mainloop()

#Fonction notation et comentaire
class ProduitsApp(tk.Toplevel):
    def __init__(self, master):
        class Produit:
          def __init__(self, nom):
              self.nom = nom
              self.avis = []

          def ajouter_avis(self, note, commentaire):
              self.avis.append((note, commentaire))

          def moyenne_notes(self):
              if not self.avis:
                  return "Pas d'avis"
              moyenne = sum([note for note, _ in self.avis]) / len(self.avis)
              return f"Moyenne des notes : {moyenne:.2f}"

        class Application(tk.Tk):
          def __init__(self):
              super().__init__()

              self.title("Système de Notation et Avis sur les Produits")

              self.produits = []

              self.frame = tk.Frame(self)
              self.frame.pack(padx=20, pady=20)

              self.label = tk.Label(self.frame, text="Nom du produit:")
              self.label.pack()

              self.nom_produit_var = tk.StringVar()
              self.nom_produit_entry = tk.Entry(self.frame, textvariable=self.nom_produit_var)
              self.nom_produit_entry.pack()

              self.ajouter_produit_button = tk.Button(self.frame, text="Ajouter Produit", command=self.ajouter_produit)
              self.ajouter_produit_button.pack()

              self.note_label = tk.Label(self.frame, text="Note (1-5):")
              self.note_label.pack()

              self.note_var = tk.IntVar()
              self.note_entry = tk.Entry(self.frame, textvariable=self.note_var)
              self.note_entry.pack()

              self.commentaire_label = tk.Label(self.frame, text="Commentaire:")
              self.commentaire_label.pack()

              self.commentaire_var = tk.StringVar()
              self.commentaire_entry = tk.Entry(self.frame, textvariable=self.commentaire_var)
              self.commentaire_entry.pack()

              self.ajouter_avis_button = tk.Button(self.frame, text="Ajouter Avis", command=self.ajouter_avis)
              self.ajouter_avis_button.pack()

              self.liste_var = tk.StringVar()
              self.liste_var.set("Liste des Produits:\n")
              self.liste_produits_label = tk.Label(self.frame, textvariable=self.liste_var)
              self.liste_produits_label.pack()

          def ajouter_produit(self):
              nom_produit = self.nom_produit_var.get()
              if nom_produit:
                  produit = Produit(nom_produit)
                  self.produits.append(produit)
                  self.nom_produit_var.set("")
                  self.maj_affichage()

          def ajouter_avis(self):
              note = self.note_var.get()
              commentaire = self.commentaire_var.get()
              if note >= 1 and note <= 5:
                  produit_selectionne = self.produits[-1]  # Dernier produit ajouté
                  produit_selectionne.ajouter_avis(note, commentaire)
                  self.note_var.set(1)  # Réinitialiser la note à 1
                  self.commentaire_var.set("")
                  self.maj_affichage()
              else:
                  messagebox.showerror("Erreur", "La note doit être entre 1 et 5.")

          def maj_affichage(self):
              liste_text = "Liste des Produits:\n"
              for produit in self.produits:
                  liste_text += f"{produit.nom} - {produit.moyenne_notes()}\nAvis:\n"
                  for note, commentaire in produit.avis:
                      liste_text += f"Note : {note}, Commentaire : {commentaire}\n"
                  liste_text += "\n"

              self.liste_var.set(liste_text)

        if __name__ == "__main__":
          app = Application()
          app.mainloop()

#Fonction catalogue de vetements
class ClothingCatalog(tk.Toplevel):
    def __init__(self, master):
        class ClothingCatalog:
          def __init__(self, root):
              self.root = root
              self.root.title("Catalogue de Vêtements")

              # Créer un frame pour afficher les vêtements
              self.frame = tk.Frame(root)
              self.frame.pack()

              # Créer une liste de vêtements (cette liste devrait être remplie avec vos données)
              self.clothes = [
                  {"name": "ZIP", "category": "Hoodie/ZIP", "size": "S", "color": "Gris", "description": "Grey Zip."},
                  {"name": "ZIP", "category": "Hoodie/ZIP", "size": "M", "color": "Gris", "description": "Grey Zip."},
                  {"name": "ZIP", "category": "Hoodie/ZIP", "size": "L", "color": "Gris", "description": "Grey Zip."},
                  {"name": "ZIP", "category": "Hoodie/ZIP", "size": "XL", "color": "Gris", "description": "Grey Zip."},
                  {"name": "Jacket", "category": "Vestes", "size": "S", "color": "Noir", "description": "Windbreaker Jacket."},
                  {"name": "Jacket", "category": "Vestes", "size": "M", "color": "Noir", "description": "Windbreaker Jacket."},
                  {"name": "Jacket", "category": "Vestes", "size": "L", "color": "Noir", "description": "Windbreaker Jacket."},
                  {"name": "Jacket", "category": "Vestes", "size": "XL", "color": "Noir", "description": "Windbreaker Jacket."},
                  # Ajoutez plus d'articles ici
              ]

              # Créer un bouton de tri par catégorie
              self.sort_button = tk.Button(self.frame, text="Trier par catégorie", command=self.sort_by_category)
              self.sort_button.pack()

              # Créer une zone de texte pour la recherche
              self.search_label = tk.Label(self.frame, text="Rechercher un article :")
              self.search_label.pack()

              self.search_entry = tk.Entry(self.frame)
              self.search_entry.pack()

              self.search_button = tk.Button(self.frame, text="Rechercher", command=self.search)
              self.search_button.pack()

              # Créer une zone d'affichage pour les vêtements
              self.display_area = tk.Text(self.frame, width=50, height=20)
              self.display_area.pack()

              # Afficher tous les vêtements au lancement de l'application
              self.display_all()

          def display_all(self):
              self.display_area.delete("1.0", tk.END)  # Effacer le texte existant
              for clothing in self.clothes:
                  self.display_area.insert(tk.END, f"{clothing['name']} - {clothing['category']}\n")
                  self.display_area.insert(tk.END, f"Taille: {clothing['size']} / Couleur: {clothing['color']}\n")
                  self.display_area.insert(tk.END, f"{clothing['description']}\n\n")

          def sort_by_category(self):
              self.clothes.sort(key=lambda x: x['category'])
              self.display_all()

          def search(self):
              query = self.search_entry.get().lower()
              results = []
              for clothing in self.clothes:
                  if query in clothing['name'].lower() or query in clothing['category'].lower() or \
                     query in clothing['size'].lower() or query in clothing['color'].lower():
                      results.append(clothing)
              self.display_area.delete("1.0", tk.END)  # Effacer le texte existant
              for clothing in results:
                  self.display_area.insert(tk.END, f"{clothing['name']} - {clothing['category']}\n")
                  self.display_area.insert(tk.END, f"Taille: {clothing['size']} / Couleur: {clothing['color']}\n")
                  self.display_area.insert(tk.END, f"{clothing['description']}\n\n")

        if __name__ == "__main__":
          root = tk.Tk()
          app = ClothingCatalog(root)
          root.mainloop()

#Fonction partage d'articles
class ArticleSharingApp(tk.Toplevel):
    def __init__(self, master):
        class Utilisateur:
          def __init__(self, nom_utilisateur):
              self.nom_utilisateur = nom_utilisateur
              self.articles_partages = []

          def partager_article(self, article, commentaire=None):
              article_partage = ArticlePartage(self, article, commentaire)
              self.articles_partages.append(article_partage)
              return article_partage

        class Article:
          def __init__(self, titre, contenu):
              self.titre = titre
              self.contenu = contenu

        class ArticlePartage:
          def __init__(self, auteur, article, commentaire=None):
              self.auteur = auteur
              self.article = article
              self.commentaire = commentaire

        class Application(tk.Tk):
          def __init__(self):
              super().__init__()

              self.title("Article Sharing App")

              self.text_widget = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=40, height=10)
              self.text_widget.pack(pady=10)

              self.create_widgets()

          def create_widgets(self):
              self.label = tk.Label(self, text="Nom d'utilisateur:")
              self.label.pack()

              self.username_entry = tk.Entry(self)
              self.username_entry.pack()

              self.share_button = tk.Button(self, text="Partager Article", command=self.share_article)
              self.share_button.pack()

          def share_article(self):
              username = self.username_entry.get()

              # Creating users and articles
              utilisateur = Utilisateur(username)
              article = Article("Titre de l'article", self.text_widget.get("1.0", tk.END))

              # Sharing the article
              article_partage = utilisateur.partager_article(article)

              # Displaying the shared article details
              result_text = f"{utilisateur.nom_utilisateur} a partagé :\n"
              result_text += f"Titre : {article_partage.article.titre}\n"
              result_text += f"Contenu : {article_partage.article.contenu}\n"
              if article_partage.commentaire:
                  result_text += f"Commentaire : {article_partage.commentaire}"

              self.display_result(result_text)

          def display_result(self, result_text):
              result_window = tk.Toplevel(self)
              result_window.title("Partage d'article")

              result_label = tk.Label(result_window, text=result_text)
              result_label.pack()

        if __name__ == "__main__":
          app = Application()
          app.mainloop()

#Fonction garde robe
class WardrobeApp(tk.Toplevel):
    def __init__(self, master):
        class GardeRobe:
          def __init__(self):
              # Initialise les structures de données pour la garde-robe et l'historique des achats
              self.garde_robe = {}
              self.historique_achats = []


          def ajouter_article(self, nom_article, categorie, couleur, saison, style):
              # Ajoute un nouvel article à la garde-robe
              article = {
                  "catégorie": categorie,
                  "couleur": couleur,
                  "saison": saison,
                  "style": style
              }
              self.garde_robe[nom_article] = article

              # Enregistre l'achat dans l'historique
              self.historique_achats.append(f"Achat : {nom_article} ({categorie}, {couleur}, {saison}, {style}) ajouté à la garde-robe.")
              # Affiche un message de réussite à l'utilisateur
              messagebox.showinfo("Information", "Article ajouté avec succès!")

          def modifier_article(self, nom_article, nouvelle_categorie, nouvelle_couleur, nouvelle_saison, nouveau_style):
              # Modifie un article existant dans la garde-robe
              if nom_article in self.garde_robe:
                  article = self.garde_robe[nom_article]
                  article["catégorie"] = nouvelle_categorie
                  article["couleur"] = nouvelle_couleur
                  article["saison"] = nouvelle_saison
                  article["style"] = nouveau_style
                  # Enregistre la modification dans l'historique
                  self.historique_achats.append(f"Modification : {nom_article} ({nouvelle_categorie}, {nouvelle_couleur}, {nouvelle_saison}, {nouveau_style}).")
                   # Affiche un message de réussite à l'utilisateur
                  messagebox.showinfo("Information", "Article modifié avec succès!")
              else:
                  # Affiche une erreur si l'article n'est pas trouvé dans la garde-robe
                  messagebox.showerror("Erreur", f"{nom_article} n'est pas présent dans la garde-robe.")

          def supprimer_article(self, nom_article):
              # Supprime un article de la garde-robe
              if nom_article in self.garde_robe:
                  del self.garde_robe[nom_article]
                  # Enregistre la suppression dans l'historique
                  self.historique_achats.append(f"Suppression : {nom_article} retiré de la garde-robe.")
                  # Enregistre la suppression dans l'historique
                  messagebox.showinfo("Information", "Article supprimé avec succès!")
              else:
                  # Affiche une erreur si l'article n'est pas trouvé dans la garde-robe
                  messagebox.showerror("Erreur", f"{nom_article} n'est pas présent dans la garde-robe.")

          def sauvegarder_garde_robe(self):
              # Sauvegarde la garde-robe dans un fichier JSON
              with open("garde_robe.json", "w") as fichier:
                  json.dump(self.garde_robe, fichier)

              # Affiche un message de réussite à l'utilisateur
              messagebox.showinfo("Information", "Garde-robe sauvegardée avec succès!")

          def charger_garde_robe(self):
              # Charge la garde-robe depuis un fichier JSON s'il existe, sinon affiche un message
              try:
                  with open("garde_robe.json", "r") as fichier:
                      self.garde_robe = json.load(fichier)
              except FileNotFoundError:
                  messagebox.showinfo("Information", "Fichier de garde-robe introuvable. La garde-robe est vide.")

        class Application(tk.Tk):
          def __init__(self):
              super().__init__()

              self.title("Garde-Robe Manager")
              self.geometry("600x400")

              # Crée une instance de la classe GardeRobe
              self.garde_robe = GardeRobe()
              # Charge la garde-robe existante depuis un fichier JSON
              self.garde_robe.charger_garde_robe()

              # Initialise l'interface graphique
              self.create_widgets()

          def create_widgets(self):
              # Crée les éléments de l'interface graphique

              menu_frame = tk.Frame(self)
              menu_frame.pack(pady=10)

              options_label = tk.Label(menu_frame, text="Options:")
              options_label.grid(row=0, column=0, padx=10)

              add_button = tk.Button(menu_frame, text="Ajouter un article", command=self.ajouter_article_window)
              add_button.grid(row=0, column=1, padx=10)

              modify_button = tk.Button(menu_frame, text="Modifier un article", command=self.modifier_article_window)
              modify_button.grid(row=0, column=2, padx=10)

              delete_button = tk.Button(menu_frame, text="Supprimer un article", command=self.supprimer_article_window)
              delete_button.grid(row=0, column=3, padx=10)

              save_button = tk.Button(menu_frame, text="Sauvegarder la garde-robe", command=self.sauvegarder_garde_robe)
              save_button.grid(row=0, column=4, padx=10)

              refresh_button = tk.Button(menu_frame, text="Actualiser l'affichage", command=self.refresh_display)
              refresh_button.grid(row=0, column=5, padx=10)

              display_frame = tk.Frame(self)
              display_frame.pack(pady=10)

              display_label = tk.Label(display_frame, text="Affichage:")
              display_label.grid(row=0, column=0, padx=10)

              self.display_text = tk.Text(display_frame, height=10, width=50)
              self.display_text.grid(row=1, column=0, padx=10)

              self.refresh_display()

          def ajouter_article_window(self):
              # Crée une fenêtre pour ajouter un article avec des champs de saisie

              window = tk.Toplevel(self)
              window.title("Ajouter un article")

              nom_label = tk.Label(window, text="Nom de l'article:")
              nom_label.grid(row=0, column=0, padx=10, pady=5)
              nom_entry = tk.Entry(window)
              nom_entry.grid(row=0, column=1, padx=10, pady=5)

              categorie_label = tk.Label(window, text="Catégorie:")
              categorie_label.grid(row=1, column=0, padx=10, pady=5)
              categorie_entry = tk.Entry(window)
              categorie_entry.grid(row=1, column=1, padx=10, pady=5)

              couleur_label = tk.Label(window, text="Couleur:")
              couleur_label.grid(row=2, column=0, padx=10, pady=5)
              couleur_entry = tk.Entry(window)
              couleur_entry.grid(row=2, column=1, padx=10, pady=5)

              saison_label = tk.Label(window, text="Saison:")
              saison_label.grid(row=3, column=0, padx=10, pady=5)
              saison_entry = tk.Entry(window)
              saison_entry.grid(row=3, column=1, padx=10, pady=5)

              style_label = tk.Label(window, text="Style:")
              style_label.grid(row=4, column=0, padx=10, pady=5)
              style_entry = tk.Entry(window)
              style_entry.grid(row=4, column=1, padx=10, pady=5)

              add_button = tk.Button(window, text="Ajouter", command=lambda: self.ajouter_article(nom_entry.get(), categorie_entry.get(), couleur_entry.get(), saison_entry.get(), style_entry.get(), window))
              add_button.grid(row=5, column=0, columnspan=2, pady=10)

          def ajouter_article(self, nom_article, categorie, couleur, saison, style, window):
              # Appelle la méthode ajouter_article de la classe GardeRobe avec les données saisies
              self.garde_robe.ajouter_article(nom_article, categorie, couleur, saison, style)

              # Actualise l'affichage de la garde-robe dans la fenêtre principale
              self.refresh_display()

              # Ferme la fenêtre d'ajout d'article
              window.destroy()

          def modifier_article_window(self):
              # Crée une fenêtre pour modifier un article avec des champs de saisie préremplis

              window = tk.Toplevel(self)
              window.title("Modifier un article")

              nom_label = tk.Label(window, text="Nom de l'article:")
              nom_label.grid(row=0, column=0, padx=10, pady=5)
              nom_entry = tk.Entry(window)
              nom_entry.grid(row=0, column=1, padx=10, pady=5)

              categorie_label = tk.Label(window, text="Nouvelle catégorie:")
              categorie_label.grid(row=1, column=0, padx=10, pady=5)
              categorie_entry = tk.Entry(window)
              categorie_entry.grid(row=1, column=1, padx=10, pady=5)

              couleur_label = tk.Label(window, text="Nouvelle couleur:")
              couleur_label.grid(row=2, column=0, padx=10, pady=5)
              couleur_entry = tk.Entry(window)
              couleur_entry.grid(row=2, column=1, padx=10, pady=5)

              saison_label = tk.Label(window, text="Nouvelle saison:")
              saison_label.grid(row=3, column=0, padx=10, pady=5)
              saison_entry = tk.Entry(window)
              saison_entry.grid(row=3, column=1, padx=10, pady=5)

              style_label = tk.Label(window, text="Nouveau style:")
              style_label.grid(row=4, column=0, padx=10, pady=5)
              style_entry = tk.Entry(window)
              style_entry.grid(row=4, column=1, padx=10, pady=5)

              modify_button = tk.Button(window, text="Modifier", command=lambda: self.modifier_article(nom_entry.get(), categorie_entry.get(), couleur_entry.get(), saison_entry.get(), style_entry.get(), window))
              modify_button.grid(row=5, column=0, columnspan=2, pady=10)

          def modifier_article(self, nom_article, nouvelle_categorie, nouvelle_couleur, nouvelle_saison, nouveau_style, window):
              # Appelle la méthode modifier_article de la classe GardeRobe avec les données saisies
              self.garde_robe.modifier_article(nom_article, nouvelle_categorie, nouvelle_couleur, nouvelle_saison, nouveau_style)

              # Actualise l'affichage de la garde-robe dans la fenêtre principale
              self.refresh_display()

              # Ferme la fenêtre de modification d'article
              window.destroy()

          def supprimer_article_window(self):
              # Crée une fenêtre pour supprimer un article avec un champ de saisie
              window = tk.Toplevel(self)

              window.title("Supprimer un article")

              nom_label = tk.Label(window, text="Nom de l'article à supprimer:")
              nom_label.grid(row=0, column=0, padx=10, pady=5)
              nom_entry = tk.Entry(window)
              nom_entry.grid(row=0, column=1, padx=10, pady=5)

              delete_button = tk.Button(window, text="Supprimer", command=lambda: self.supprimer_article(nom_entry.get(), window))
              delete_button.grid(row=1, column=0, columnspan=2, pady=10)

          def supprimer_article(self, nom_article, window):
              # Appelle la méthode supprimer_article de la classe GardeRobe avec les données saisies
              self.garde_robe.supprimer_article(nom_article)
              # Actualise l'affichage de la garde-robe dans la fenêtre principale
              self.refresh_display()
              # Actualise l'affichage de la garde-robe dans la fenêtre principale
              window.destroy()

          def sauvegarder_garde_robe(self):
              # Appelle la méthode sauvegarder_garde_robe de la classe GardeRobe
              self.garde_robe.sauvegarder_garde_robe()

          def refresh_display(self):
              # Actualise l'affichage de la garde-robe dans la fenêtre principale
              self.display_text.delete(1.0, tk.END)
              self.display_text.insert(tk.END, "Garde-robe de l'utilisateur :\n")
              for article, details in self.garde_robe.garde_robe.items():
                  self.display_text.insert(tk.END, f"{article} ({details['catégorie']}, {details['couleur']}, {details['saison']}, {details['style']})\n")

        if __name__ == "__main__":

          # Crée une instance de la classe Application et lance la boucle principale de l'interface graphique
          app = Application()
          app.mainloop()

#Fonction Liste des souhait
class WishlistApp(tk.Toplevel):
    def __init__(self, master):
        class Vetements:
          def __init__(self, nom, prix):
              self.nom = nom
              self.prix = prix

        class ListeDeSouhaitsApp:
          def __init__(self, root):
              self.root = root
              self.root.title("Liste de Souhaits de Vêtements")

              self.liste_souhaits = []

              self.frame = tk.Frame(root)
              self.frame.pack(padx=20, pady=20)

              self.label = tk.Label(self.frame, text="Nom du vêtement:")
              self.label.pack()

              self.nom_var = tk.StringVar()
              self.nom_entry = tk.Entry(self.frame, textvariable=self.nom_var)
              self.nom_entry.pack()

              self.label2 = tk.Label(self.frame, text="Prix du vêtement (en euros):")
              self.label2.pack()

              self.prix_var = tk.DoubleVar()
              self.prix_entry = tk.Entry(self.frame, textvariable=self.prix_var)
              self.prix_entry.pack()

              self.ajouter_bouton = tk.Button(self.frame, text="Ajouter à la liste de souhaits", command=self.ajouter_vetement)
              self.ajouter_bouton.pack()

              self.liste_var = tk.StringVar()
              self.liste_var.set("Liste de souhaits:\n")

              self.liste_label = tk.Label(self.frame, textvariable=self.liste_var)
              self.liste_label.pack()

              self.retirer_label = tk.Label(self.frame, text="Nom du vêtement à retirer:")
              self.retirer_label.pack()

              self.retirer_var = tk.StringVar()
              self.retirer_entry = tk.Entry(self.frame, textvariable=self.retirer_var)
              self.retirer_entry.pack()

              self.retirer_bouton = tk.Button(self.frame, text="Retirer de la liste", command=self.retirer_vetement)
              self.retirer_bouton.pack()

          def ajouter_vetement(self):
              nom = self.nom_var.get()
              prix = self.prix_var.get()

              vetement = Vetements(nom, prix)
              self.liste_souhaits.append(vetement)

              self.nom_var.set("")
              self.prix_var.set(0.0)

              self.maj_affichage()

          def retirer_vetement(self):
              nom = self.retirer_var.get()

              for vetement in self.liste_souhaits:
                  if vetement.nom == nom:
                      self.liste_souhaits.remove(vetement)
                      self.maj_affichage()
                      return

              self.maj_affichage()

          def maj_affichage(self):
              liste_text = "Liste de souhaits:\n"
              for vetement in self.liste_souhaits:
                  liste_text += f"{vetement.nom} - Prix : {vetement.prix} €\n"

              self.liste_var.set(liste_text)

        if __name__ == "__main__":
          root = tk.Tk()
          app = ListeDeSouhaitsApp(root)
          root.mainloop()

#Fonctions Panier d'achat
class CartApp(tk.Toplevel):
    def __init__(self, master):
        class Article:
          def __init__(self, nom, prix):
              self.nom = nom
              self.prix = prix

        class Panier:
          def __init__(self):
              self.articles = []

          def ajouter_article(self, article):
              self.articles.append(article)

          def vider_panier(self):
              self.articles = []

          def calculer_total(self):
              total = 0
              for article in self.articles:
                  total += article.prix
              return total

        class PanierApp(tk.Tk):
          def __init__(self):
              super().__init__()

              self.title("Panier App")

              self.panier = Panier()

              self.text_widget = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=40, height=10)
              self.text_widget.pack(pady=10)

              self.create_widgets()

          def create_widgets(self):
              self.add_button = tk.Button(self, text="Ajouter un article", command=self.ajouter_article_window)
              self.add_button.pack()

              self.clear_button = tk.Button(self, text="Vider le panier", command=self.vider_panier)
              self.clear_button.pack()

              self.display_button = tk.Button(self, text="Afficher le panier", command=self.afficher_panier)
              self.display_button.pack()

              self.checkout_button = tk.Button(self, text="Passer à la caisse", command=self.passer_a_la_caisse)
              self.checkout_button.pack()

              self.quit_button = tk.Button(self, text="Quitter", command=self.destroy)
              self.quit_button.pack()

          def ajouter_article_window(self):
              top = tk.Toplevel(self)
              top.title("Ajouter un article")

              # Créer des champs de saisie
              nom_article_label = tk.Label(top, text="Nom de l'article:")
              nom_article_label.pack()
              nom_article_entry = tk.Entry(top)
              nom_article_entry.pack()

              prix_article_label = tk.Label(top, text="Prix de l'article:")
              prix_article_label.pack()
              prix_article_entry = tk.Entry(top)
              prix_article_entry.pack()

              # Create a button to add the article
              add_button = tk.Button(top, text="Ajouter l'article", command=lambda: self.ajouter_article(
                  nom_article_entry.get(), float(prix_article_entry.get())))
              add_button.pack()

          def ajouter_article(self, nom, prix):
              article = Article(nom, prix)
              self.panier.ajouter_article(article)
              self.text_widget.delete(1.0, tk.END)
              self.text_widget.insert(tk.END, f"{nom} a été ajouté au panier.\n")

          def vider_panier(self):
              self.panier.vider_panier()
              self.text_widget.delete(1.0, tk.END)
              self.text_widget.insert(tk.END, "Le panier a été vidé.\n")

          def afficher_panier(self):
              result = "Contenu du panier :\n"
              for article in self.panier.articles:
                  result += f"{article.nom}: ${article.prix}\n"
              result += f"Total du panier : ${self.panier.calculer_total()}\n"
              self.text_widget.delete(1.0, tk.END)
              self.text_widget.insert(tk.END, result)

          def passer_a_la_caisse(self):
              top = tk.Toplevel(self)
              top.title("Options de paiement")

              payment_label = tk.Label(top, text="Options de paiement:")
              payment_label.pack()

              credit_card_button = tk.Button(top, text="1. Carte de crédit", command=self.paiement_carte_credit)
              credit_card_button.pack()

              paypal_button = tk.Button(top, text="2. PayPal", command=self.paiement_paypal)
              paypal_button.pack()

          def paiement_carte_credit(self):
              self.text_widget.delete(1.0, tk.END)
              self.text_widget.insert(tk.END, "Paiement par carte de crédit en cours...\n")
              #Implement logique pour le payement par carte de credit

          def paiement_paypal(self):
              self.text_widget.delete(1.0, tk.END)
              self.text_widget.insert(tk.END, "Paiement par PayPal en cours...\n")
              #Implement logique pour le payement PayPal

        if __name__ == "__main__":
          app = PanierApp()
          app.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
