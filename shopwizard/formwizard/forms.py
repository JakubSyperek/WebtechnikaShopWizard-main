from django import forms
from django.core.exceptions import ValidationError

def file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')

def get_available_templates():
    return {"t1": "test template1", "t2": "test template2"}

# Krok 1
class ShopForm1(forms.Form):
    nazwa_sklepu = forms.CharField(label="Nazwa sklepu", max_length=100)
    # Używamy [0-9] zamiast \d, bo w py3 \d matchuje liczby w innych skryptach, np. ੩
    nip = forms.RegexField(label="NIP firmy", regex=r"^[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}$")
    logo = forms.ImageField(label="Logo", validators=[file_size])
    imie = forms.CharField(label="Imię", max_length=30, required=False)
    nazwisko = forms.CharField(label="Nazwisko", max_length=60, required=False)
    nazwa_firmy = forms.CharField(label="Nazwa firmy", max_length=100, required=False)
    adres_email = forms.EmailField(label="Adres email")
    numer_telefonu = forms.CharField(label="Numer telefonu", max_length=12)

# Krok 2
class ShopForm2(forms.Form):
    szablon = forms.ChoiceField(label="Wybierz szablon", choices=get_available_templates)

# Kroki 3-5 (placeholder)
class ShopForm3(forms.Form):
    funkcjonalnosci = forms.CharField(label="Funkcjonalności")


class ShopForm4(forms.Form):
    platnosci = forms.CharField(label="Płatności")


class ShopForm5(forms.Form):
    przewoznicy = forms.CharField(label="Przewoźnicy")
