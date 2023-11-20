import json
import tkinter as tk
from tkinter import messagebox

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
