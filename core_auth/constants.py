
GENERIC_STATUS_LIST = [
    (
        "g_lst_gen_status_pending",
        "g_lst_gen_status_pending",
    ),  # generic status for pending in lifecycle
    (
        "g_lst_gen_status_active",
        "g_lst_gen_status_active",
    ),  # generic status for active in lifecycle
    (
        "g_lst_gen_status_inactive",
        "g_lst_gen_status_inactive",
    ),  # generic status for inactive in lifecycle
    (
        "g_lst_gen_status_archived",
        "g_lst_gen_status_archived",
    ),  # generic status for archived in lifecycle
    (
        "g_lst_gen_status_erased",
        "g_lst_gen_status_erased",
    ),  # generic status for a logically deleted item
]

GENDER_LIST = [
    ("g_lst_gender_mister", "g_lst_gender_mister"),  # Mister
    ("g_lst_gender_madam", "g_lst_gender_madam"),  # Madam
    ("g_lst_gender_miss", "g_lst_gender_miss"),  # Miss
    (
        "g_lst_gender_undef",
        "g_lst_gender_undef",
    ),  # Undefined gender - default value (gender definition not required)
]

# Type de client
C_TYPE = [
    ("g_client_type_Individual", "Individual"),
    ("g_client_type_Individual", "Enterprise"),
]

ACCOUNT_EMAIL_STATUS_LIST = [
    (
        "g_lst_account_email_status_verified",
        "g_lst_account_email_status_verified",
    ),  # status for an email with which the user signed in at least one time
    (
        "g_lst_account_email_status_notverified",
        "g_lst_account_email_status_notverified",
    ),  # DEFAULT VALUE - status for an email that has just been defined but not yet verified nor used for log on
    (
        "g_lst_account_email_status_invalid",
        "g_lst_account_email_status_invalid",
    ),  # status for an email that cannot be reached (presuming not existing)
    (
        "g_lst_account_email_status_inaccurate",
        "g_lst_account_email_status_inaccurate",
    ),  # status for an email that can be reached but does not belong to the user
]

BUSINESS_RELATIONSHIP_NATURE_LIST = [
    (
        "g_lst_bizRel_nature_B2B",
        "g_lst_bizRel_nature_B2B",
    ),  # platform to worker relationship
    (
        "g_lst_bizRel_nature_B2C",
        "g_lst_bizRel_nature_B2C",
    ),  # platform to client relationship
    (
        "g_lst_bizRel_nature_B2B2C",
        "g_lst_bizRel_nature_B2B2C",
    ),  # worker to client relationship (through platform)
    (
        "g_lst_bizRel_nature_B2P",
        "g_lst_bizRel_nature_B2P",
    ),  # platform to partner relationship
    (
        "g_lst_bizRel_nature_B2B2P",
        "g_lst_bizRel_nature_B2B2P",
    ),  # worker to partner relationship (through platform)
    (
        "g_lst_bizRel_nature_OTHER",
        "g_lst_bizRel_nature_OTHER",
    ),  # any other relationship
]


PROPOSAL_NATURE_LIST = [
    ("g_lst_prop_nature_tmpl", "g_lst_prop_nature_tmpl"),  # template proposal
    ("g_lst_prop_nature_demo", "g_lst_prop_nature_demo"),  # demo proposal
    (
        "g_lst_prop_nature_pref",
        "g_lst_prop_nature_pref",
    ),  # preferred (favorite) proposal
    (
        "g_lst_prop_nature_real",
        "g_lst_prop_nature_real",
    ),  # real proposal = proposal for a client
]

WORK_TYPE_LIST = [
    (
        "g_lst_work_type_construct",
        "g_lst_work_type_construct",
    ),  # work type is building construct
    ("g_lst_work_type_other", "g_lst_work_type_other"),  # any other type of work
]


OPPORTUNITY_STATUS_LIST = [
    (
        "g_lst_opp_status_open",
        "g_lst_opp_status_open",
    ),  # status for an open opportunity
    ("g_lst_opp_status_won", "g_lst_opp_status_won"),  # status for a won opportunity
    (
        "g_lst_opp_status_inactive",
        "g_lst_opp_status_inactive",
    ),  # status for an inactive opportunity
    (
        "g_lst_opp_status_archived",
        "g_lst_opp_status_archived",
    ),  # status for an archived opportunity
    (
        "g_lst_opp_status_erased",
        "g_lst_opp_status_erased",
    ),  # status for a logically deleted opportuniy
]

OPPORTUNITY_SUBSTATUS_LIST = [
    (
        "g_lst_opp_substatus_low",
        "g_lst_opp_substatus_low",
    ),  # sub-status for a low priority opportunity ("cold")
    (
        "g_lst_opp_substatus_medium",
        "g_lst_opp_substatus_medium",
    ),  # sub-status for a medium priority opportunity ("warm")
    (
        "g_lst_opp_substatus_high",
        "g_lst_opp_substatus_high",
    ),  # sub-status for a high priority opportunity ("hot")
]

PROPOSAL_STATUS_LIST = [
    (
        "g_lst_prop_status_initiated",
        "g_lst_prop_status_initiated",
    ),  # status for a proposal initiated as part of a client request - not used in MVP
    (
        "g_lst_prop_status_requested",
        "g_lst_prop_status_requested",
    ),  # status for a proposal posted as part of a client request - not used in MVP
    (
        "g_lst_prop_status_ongoing",
        "g_lst_prop_status_ongoing",
    ),  # status for a proposal just created or currently being modified by a worker
    (
        "g_lst_prop_status_sent",
        "g_lst_prop_status_sent",
    ),  # status for a proposal sent to client - for the client, the key will be: g_list_proposal_status_received
    (
        "g_lst_prop_status_revised",
        "g_lst_prop_status_revised",
    ),  # status for a proposal revised by client
    (
        "g_lst_prop_status_signed",
        "g_lst_prop_status_signed",
    ),  # status for a proposal sent by client
    (
        "g_lst_prop_status_refused",
        "g_lst_prop_status_refused",
    ),  # status for a proposal refused by client
    (
        "g_lst_prop_status_archived",
        "g_lst_prop_status_archived",
    ),  # status for a proposal archived (e.g. following cancellation)
    (
        "g_lst_prop_status_erased",
        "g_lst_prop_status_erased",
    ),  # status for a proposal logically deleted
]


CONSTRUCT_WORK_TYPE = [
    (
        "g_lst_constrWork_type_all",
        "g_lst_constrWork_type_all",
    ),  # any type of construct work ("Tout-venant")
    (
        "g_lst_constrWork_type_struct",
        "g_lst_constrWork_type_struct",
    ),  # structural construct work ("Gros oeuvre") - 24% des entreprises unipersonnelles en 2020
    (
        "g_lst_constrWork_type_paint",
        "g_lst_constrWork_type_paint",
    ),  # painting work ("Peinture")                - 12% des entreprises unipersonnelles en 2020
    (
        "g_lst_constrWork_type_elec",
        "g_lst_constrWork_type_elec",
    ),  # wiring work ("Electricité")               - 12% des entreprises unipersonnelles en 2020
    (
        "g_lst_constrWork_type_carp",
        "g_lst_constrWork_type_carp",
    ),  # carpentry work ("Menuiserie") - post-MVP  - 9% des entreprises unipersonnelles en 2020
    (
        "g_lst_constrWork_type_plumb",
        "g_lst_constrWork_type_plumb",
    ),  # plumbing work ("Plomberie")   - post-MVP  - 7% des entreprises unipersonnelles en 2020
    (
        "g_lst_constrWork_type_plast",
        "g_lst_constrWork_type_plast",
    ),  # plastering work ("Plâtrerie") - post-MVP  - 5% des entreprises unipersonnelles en 2020
    (
        "g_lst_constrWork_type_heat",
        "g_lst_constrWork_type_heat",
    ),  # heating work ("Chauffage")    - post-MVP  - 5% des entreprises unipersonnelles en 2020
    (
        "g_lst_constrWork_type_tiling",
        "g_lst_constrWork_type_tiling",
    ),  # tiling work ("Carrelage")     - post-MVP  - 5% des entreprises unipersonnelles en 2020
    (
        "g_lst_constrWork_type_other",
        "g_lst_constrWork_type_other",
    ),  # any other construct work
]


# /!\ List not used in models.py but stands for the reference in code, including for list choice ordering /!\

# In the future, there might be other work unit types (xxxx_WU_TYPE_LIST), for other types of craftwork

CONSTRUCT_WU_TYPE_LIST = [
    (
        "g_lst_wuType_gu",
        "g_lst_wuType_gu",
    ),  # Generic unit ("Unité Générique")          - Symbol FR = "U"
    (
        "g_lst_wuType_as",
        "g_lst_wuType_as",
    ),  # Assembly of items ("Ensemble")            - Symbol FR = "ENS"
    (
        "g_lst_wuType_sm",
        "g_lst_wuType_sm",
    ),  # Surface in square meter ("Mètre carré")   - Symbol FR = "M2"
    (
        "g_lst_wuType_lm",
        "g_lst_wuType_lm",
    ),  # Length in linear meter ("Mètre linéaire") - Symbol FR = "ML"
    (
        "g_lst_wuType_mh",
        "g_lst_wuType_mh",
    ),  # Workload in manhours ("Heure-homme")      - Symbol FR = "H"
    (
        "g_lst_wuType_md",
        "g_lst_wuType_md",
    ),  # Workload in mandays ("Jour-homme")        - Symbol FR = "J"
    (
        "g_lst_wuType_lt",
        "g_lst_wuType_lt",
    ),  # Liquid in litre ("Litre")                 - Symbol FR = "L"
    (
        "g_lst_wuType_kg",
        "g_lst_wuType_kg",
    ),  # Weight in kilogram ("Poids")              - Symbol FR = "KG"
    (
        "g_lst_wuType_cm",
        "g_lst_wuType_cm",
    ),  # Volume in cubic meter ("Mètre cube")      - Symbol FR = "M3"
]

BUSINESS_AGREEMENT_NATURE_CHOICES = [
    ("g_lst_bizAgr_nature_onetime", "g_lst_bizAgr_nature_onetime"),
    ("g_lst_bizAgr_nature_subscription", "g_lst_bizAgr_nature_subscription"),
]

# Enum for Business Agreement Status
BUSINESS_AGREEMENT_STATUS_CHOICES = [
    ("g_lst_bizAgr_status_active", "Active"),
    ("g_lst_bizAgr_status_aborted", "Aborted"),
    ("g_lst_bizAgr_status_terminated", "Terminated"),
]

WORK_EVENT_TYPE_CHOICES = [
    ("wevent_type_lifecycle", "wevent_type_lifecycle"),
    ("wevent_type_date", "wevent_type_date"),
    ("wevent_type_pay", "wevent_type_pay"),
    ("wevent_type_update", "wevent_type_update"),
    ("wevent_type_other", "wevent_type_other"),
    ("wevent_type_alert", "wevent_type_alert"),
    ("wevent_type_image", "wevent_type_image"),
]

WORK_STATUS_CHOICES = [
    ("g_lst_work_status_pending", "g_lst_work_status_pending"),
    ("g_lst_work_status_ongoing", "g_lst_work_status_ongoing"),
    ("g_lst_work_status_terminated", "g_lst_work_status_terminated"),
    ("g_lst_work_status_cancelled", "g_lst_work_status_cancelled"),
]

WORK_TYPE_CHOICES = [
    ("g_lst_work_type_construct", "g_lst_work_type_construct"),
]