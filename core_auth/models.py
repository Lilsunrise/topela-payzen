from django.contrib.auth.models import AbstractUser
from django.db import models


from .constants import *

# Create your models here.

class TopelaBaseModel(models.Model):
    posted = models.DateTimeField(auto_now_add=True)  # Date de création de l'objet
    updated = models.DateTimeField(auto_now=True)  # Date de modification de l'objet

    class Meta:
        abstract = True


class Address(TopelaBaseModel):
    """
    **Adresse**
    Adresse Postale France et Dom-Tom selon la norme Afnor **NF Z 10-011**
    """

    complement = models.CharField(
        max_length=76, blank=True, null=True
    )  ### --- ### --- : EVOLUTION
    street = models.CharField(max_length=38)  ### --- ### --- : EVOLUTION
    mailbox_compl = models.CharField(
        max_length=38, blank=True, null=True
    )  ### --- ### --- : EVOLUTION
    zipcode = models.CharField(max_length=38)  ### --- ### --- : EVOLUTION
    town = models.CharField(max_length=38)  ### --- ### --- : EVOLUTION
    long = models.DecimalField(
        max_digits=9, decimal_places=7, blank=True, null=True
    )  ### --- ### --- : EVOLUTION
    lat = models.DecimalField(
        max_digits=9, decimal_places=7, blank=True, null=True
    )  ### --- ### --- : EVOLUTION

    def __str__(self):
        return f"{self.street}, {self.zipcode} {self.town}"

    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adresses"


class Account(AbstractUser, TopelaBaseModel):
    """
    **Compte d'authentification**
    Ce modèle hérite de la classe Django AbstractUser, qui comporte les éléments
    d'authentification de base comme le nom d'utilisateur, mot de passe SHA256, email,
    status, groupe, etc...)
    """

    username = models.CharField(
        max_length=30,
        unique=True,
        help_text="Required. 150 characters or fewer",
        # validators=[UsernameValidator()],
        error_messages="A user with that username already exists.",
    )
    email = models.CharField(max_length=100,null=True, blank=True)
    # avatar = models.FileField(upload_to=account_avatar_path, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)  # Téléphone portable | added blank on jan 28 2024 by kaiss
    gender = models.CharField(
        max_length=32, 
        choices=GENDER_LIST, 
        default="g_lst_gender_undef"
    )
    landline = models.CharField(max_length=15, blank=True, null=True)  # Téléphone fixe
    failed_login_attempts = models.IntegerField(default=0)
    last_failed_login_timestamp = models.DateTimeField(null=True, blank=True)
    phone_verified = models.BooleanField(
        default=False
    )  # Si le numéro de téléphone est vérifié par OTP
    email_verified_status = models.CharField(
        max_length=40,
        choices=ACCOUNT_EMAIL_STATUS_LIST,
        default="g_lst_account_email_status_notverified",
    )  # Si l'email est vérifié par envoi d'email
    otp_retries = models.IntegerField(
        default=0
    )  # Combien de fois le login OTP a été réessayé

    status = models.CharField(
        max_length=32, 
        choices=GENERIC_STATUS_LIST, 
        default="g_lst_gen_status_active"
    )  # Status cycle générique
    failed_login_attempts = models.PositiveSmallIntegerField(default=0)
    blocked_until = models.DateTimeField(null=True, blank=True)
    notif_email = models.BooleanField(default=False)
    notif_phone = models.BooleanField(default=False)
    notif_push_app = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False) # added on jan 28 2024 by kaiss
    disable_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

class Party(TopelaBaseModel):
    """
    **Tiers**
    Une entité utilisant l'application Topela.
    Ce modèle est une superclasse des quartes tiers de Topela:
    Client, Professionnel, Partenaire et Administrateur.
    """

    accounts = models.ManyToManyField(Account)
    name = models.CharField(max_length=64, blank=False)  # Dénomination

    address = models.ForeignKey(
        "Address",
        related_name="%(class)s_party_address",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )  # Adresse postale
    status = models.CharField(
        max_length=32,
        choices=GENERIC_STATUS_LIST, 
        default="g_lst_gen_status_active"
    )  # Status cycle générique

    class Meta:
        abstract = True

    @property
    def get_account(self) -> Account:
        return self.accounts.all()[0]

class Client(Party):
    """
    **Client**
    Ce modèle est pour un client particulier ou professionnel qui cherche des affaires
    ou des devis sur Topela.
    """

    # Informations supplémentaire sur le client
    ctype = models.CharField(
        max_length=24, choices=C_TYPE
    )  # Type de client (Particulier ou professionnel)

    def __str__(self):
        return self.get_account.username

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

class Pro(Party):
    """
    **Professionnel**
    Ce modèle est pour un prestataire professionnel qui cherche des affaires ou des clients
    sur Topela.
    """

    subscribed = models.BooleanField(default=False)  ### --- ### --- : EVOLUTION
    company_name = models.CharField(max_length=64)
    company_reference = models.CharField(
        max_length=64, blank=True, null=True
    )  # company_reference in France is "SIRET"
    company_compl_reference = models.CharField(
        max_length=64, blank=True, null=True
    )  # company_compl_reference in France is used to store "Numéro RM" (Numéro d'inscription au Registre des Métiers)
    company_activity_code = models.CharField(max_length=64, blank=True, null=True)
    company_share_capital = models.IntegerField(blank=True, null=True)
    company_legal_status = models.CharField(max_length=32, null=True, blank=True)
    company_tax_number = models.CharField(max_length=64, null=True, blank=True)
    company_phone = models.CharField(max_length=32, null=True, blank=True)
    company_email = models.CharField(max_length=64, null=True, blank=True)
    specialty = models.CharField(
        max_length=32, null=True, blank=True
    )  # updated in model evols sept 2023
    description = models.CharField(max_length=256, null=True, blank=True)
    # logo = models.FileField(upload_to=pro_logo_path, null=True, blank=True)  # Logo | added null and blank on jan 28 2024 by kaiss
    platform_code = models.CharField(max_length=6, unique=True)
    # add gallery model
    # type : certificate,work
    # insurance
    insurance_name = models.CharField(max_length=64, null=True, blank=True)
    insurance_warranty = models.CharField(max_length=128, null=True, blank=True)
    insurance_policy_number = models.CharField(max_length=64, null=True, blank=True)
    insurance_geo_coverage = models.CharField(max_length=128, null=True, blank=True)
    insurance_address = models.CharField(max_length=256, null=True, blank=True)
    # profile of worker
    website_url = models.CharField(max_length=256, null=True, blank=True)
    iban = models.CharField(max_length=27, null=True, blank=True) # Updated by Kaiss on Apr 9th 2024 (Model Evolutions Sprint 35)
    swift = models.CharField(max_length=11, null=True, blank=True) # Added by Kaiss on Apr 9th 2024 (Model Evolutions Sprint 35)
    additional_conditions = models.CharField(max_length=256, null=True, blank=True)
    accepted_payment_modes = models.CharField(max_length=256, null=True, blank=True)
    # add it in proposal
    favorite_color = models.CharField(max_length=10, default="#49AFDA")
    proposal_validity_duration = models.IntegerField(default=30)
    payment_max_delay = models.IntegerField(default=30)
    sales_conditions = models.TextField(null=True, blank=True)
    profile_visible = models.BooleanField(
        default=False
    )  # added in model evols sept 2023
    profile_verified = models.BooleanField(
        default=False
    )  # added in model evols sept 2023

    def __str__(self):
        return self.get_account.username

    class Meta:
        verbose_name = "Artisan"
        verbose_name_plural = "Artisans"


class Intermediary(Party):
    # Informations supplémentaire sur l'intermédiaire
    def __str__(self):
        return self.get_account.username

    class Meta:
        verbose_name = "Intermédiaire"
        verbose_name_plural = "Intermédiaires"

class BusinessRelationship(TopelaBaseModel):
    """
    **Relation d'Affaire**
    Une relation d'affaire qui relie 2 tiers selon la nature de l'affaire (B2C, B2B, etc...)
    """

    intermediary = models.ForeignKey(
        "Intermediary", on_delete=models.CASCADE
    )  # Consommateur du service dans la relation d'affaire
    provider = models.ForeignKey(
        "Pro", on_delete=models.CASCADE
    )  # Fournisseur du service dans la relation d'affaire
    consumer = models.ForeignKey(
        "Client", on_delete=models.CASCADE, null=True, blank=True
    )  # Consommateur du service dans la relation d'affaire
    nature = models.CharField(
        max_length=32, choices=BUSINESS_RELATIONSHIP_NATURE_LIST
    )  # Nature de Relation d'Affaire
    status = models.CharField(
        max_length=32, choices=GENERIC_STATUS_LIST, default="g_lst_gen_status_active"
    )  # Statut générique

    def __str__(self):
        if self.provider and self.consumer:
            return f"{self.intermediary} <> {self.provider} <> {self.consumer}"
        elif self.provider and not self.consumer:
            return f"{self.intermediary} <> {self.provider}"
        else:
            return f"{self.intermediary} <> {self.consumer}"

    class Meta:
        unique_together = ["intermediary", "provider", "consumer"]
        verbose_name = "Relation d'Affaire"
        verbose_name_plural = "Relations d'Affaire"

class BusinessAgreement(TopelaBaseModel):
    business_relationship = models.ForeignKey(
        "BusinessRelationship",
        on_delete=models.CASCADE,
        verbose_name="Relation d'Affaire",
    )

    nature = models.CharField(
        max_length=255,
        choices=BUSINESS_AGREEMENT_NATURE_CHOICES,
        default="g_lst_bizAgr_nature_onetime",
        verbose_name="Nature de l'affaire",
        db_index=True,
    )

    status = models.CharField(
        max_length=255,
        choices=BUSINESS_AGREEMENT_STATUS_CHOICES,
        default="g_lst_bizAgr_status_active",
        verbose_name="Statut de l'affaire",
        db_index=True,
    )

    # si indiqué plutard
    # billing_schedule = models.ForeignKey('BillingSchedule', on_delete=models.CASCADE, verbose_name="Clé étrangère, identifiant de l'échéancier")

    def __str__(self):
        return f"Business Agreement {self.id}"

    class Meta:
        verbose_name = "Affaire"
        verbose_name_plural = "Affaires"


    
class Offer(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    pricing = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50, default="monthly")
    recurrent_payment_date = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.title
    
class Work(TopelaBaseModel):
    business_agreement = models.ForeignKey(BusinessAgreement, on_delete=models.CASCADE)
    proposal = models.CharField(max_length=10)
    status = models.CharField(max_length=50, choices=WORK_STATUS_CHOICES, db_index=True)
    worktype = models.CharField(max_length=50, choices=WORK_TYPE_CHOICES, db_index=True)

    work_start_date = models.DateField()
    work_end_date = models.DateField()

    practical_info = models.CharField(max_length=512, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    client_reserves = models.TextField(null=True, blank=True)

    cancellation_date = models.DateField(null=True, blank=True)
    cancellation_account = models.ForeignKey(
        "Account",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cancellation_account",
    )
    cancellation_reason = models.CharField(max_length=512, null=True, blank=True)

    abortion_request_date = models.DateField(null=True, blank=True)
    abortion_request_account = models.ForeignKey(
        "Account",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="abortion_request_account",
    )
    abortion_reason = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        abstract = True

class SaaSWork(Work):
    title = models.CharField(max_length=256, db_index=True)
    offer = models.ForeignKey("Offer", on_delete=models.CASCADE, related_name='saas_works')
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Abonnement"
        verbose_name_plural = "Abonnements"