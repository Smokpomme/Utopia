import tkinter as tk

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