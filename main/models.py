from django.db import models

# ---------- SERVICE MODEL ----------
class Service(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='services/')
    description = models.TextField()

    def __str__(self):
        return self.title


# ---------- GALLERY MODEL ----------
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"Gallery Image {self.id}"


# ---------- TESTIMONIAL MODEL ----------
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name


# ---------- CONTACT MODEL ----------
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
