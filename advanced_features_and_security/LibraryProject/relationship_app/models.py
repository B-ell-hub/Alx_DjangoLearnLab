class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    publication_year = models.PositiveIntegerField()
    library = models.ForeignKey("Library", on_delete=models.CASCADE, related_name="books")

    # -----------------------
    # Custom permissions
    # -----------------------
    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]

    def __str__(self):
        return self.title
