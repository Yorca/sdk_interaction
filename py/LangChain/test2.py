# import os
#
# dir = 'res/detection/expectations'
# for filename in os.listdir(dir):
#     if not filename.endswith('.log'):
#         continue
#     path = os.path.join(dir, filename)
#
#     print(path)
#     spliter = '--------------------------------------------------------------------------------------\n'
#     with open(path, 'r') as file:
#         data = file.read()
#     list = data.split(spliter)
#     new_text = ""
#     for item in list:
#         if "Trace:\ncall 'setUserProperty' of class" in item or "Trace:\ncall 'addNetworkExtrasBundle' of class" in item:
#             print(item)
#             continue
#         new_text += item + spliter
#     with open(path, 'w') as file:
#         file.write(new_text)
# from difflib import get_close_matches
# matches = get_close_matches(str(['tru']), [str(['True']), str(['false'])])
# print(f"matches = {matches}")

import demjson3

data = """
[
    {
        "timestamp": 1733717249404,
        "context": "clicked 'Skip' in a page offering push notifications with a discount.",
    },
    {
        "timestamp": 1733717251514,
        "context": "clicked 'France' in a preferences confirmation page for shipping destination.",
    },
    {
        "timestamp": 1733717252689,
        "context": "clicked 'Français' in a preferences confirmation page for language selection.",
    },
    {
        "timestamp": 1733717254464,
        "context": "clicked 'Recherchez votre pays/région' in a page listing countries for shipping.",
    },
    {
        "timestamp": 1733717256292,
        "context": "clicked 'United States' in a page listing countries for shipping.",
    },
    {
        "timestamp": 1733717257536,
        "context": "clicked 'Azerbaijan' in a page listing countries for shipping.",
    },
    {
        "timestamp": 1733717261228,
        "context": "clicked 'Français' in a preferences confirmation page for language selection.",
    },
    {
        "timestamp": 1733717263053,
        "context": "clicked 'Français' in a language selection page.",
    },
    {
        "timestamp": 1733717266985,
        "context": "clicked 'READY TO GO!' in a preferences confirmation page to finalize choices.",
    },
    {
        "timestamp": 1733717267781,
        "is_privacy_api": true,
        "description": "call 'setConsent' of class 'com.google.firebase.analytics.FirebaseAnalytics' with arguments '[object Object]', return undefined",
        "context": "Consent state needs to be defined for analytics storage and advertisement storage.",
        "expectations": "Sets the applicable end user consent state for this app on this device. User has granted consent for all types of data collection."
    },
    {
        "timestamp": 1733717294600,
        "context": "clicked 'Rechercher' in a page for searching items.",
    },
    {
        "timestamp": 1733717304629,
        "context": "clicked 'ACCUEIL' in a navigation page.",
    },
    {
        "timestamp": 1733717305596,
        "context": "clicked 'ACCUEIL' in a navigation page.",
    },
    {
        "timestamp": 1733717306530,
        "context": "clicked 'Offre Folie: Jusqu'à -70%! Shop Maintenant!' in a promotional page.",
    },
    {
        "timestamp": 1733717317209,
        "context": "clicked 'LIVRAISON GRATUITE DÈS 39,00 €' in a cart page.",
    },
    {
        "timestamp": 1733717323133,
        "context": "clicked 'Se connecter avec Facebook' in a login page.",
    },
    {
        "timestamp": 1733717324244,
        "context": "clicked 'Se connecter avec Facebook' in a login page.",
    },
    {
        "timestamp": 1733717325374,
        "context": "clicked 'CONNECTEZ-VOUS AVEC EMAIL OU TÉLÉPHONE' in a login page.",
    },
    {
        "timestamp": 1733717326149,
        "context": "clicked 'Adresse e-mail' in a login page.",
    },
    {
        "timestamp": 1733717334493,
        "context": "clicked 'BARRETTE EN VELOURS AVEC NŒUD' in a cart page.",
    },
    {
        "timestamp": 1733717343152,
        "context": "clicked 'LIVRAISON GRATUITE DÈS 39,00 €' in a cart page.",
    },
    {
        "timestamp": 1733717366603,
        "context": "clicked 'AJOUTER AU PANIER' in a product page.",
    },
    {
        "timestamp": 1733717376655,
        "context": "clicked 'Se connecter avec Facebook' in a login page.",
    },
    {
        "timestamp": 1733717378835,
        "context": "clicked 'ou en 3 versements sans intérêts de 9,00 €.11' in a product page.",
    },
    {
        "timestamp": 1733717383184,
        "context": "clicked 'AUCUN ARTICLE TROUVÉ :(' in a cart page.",
    },
    {
        "timestamp": 1733717384409,
        "context": "clicked 'LIVRAISON GRATUITE DÈS 39,00 €' in a cart page.",
    },
    {
        "timestamp": 1733717406868,
        "context": "clicked 'Offre Folie: Jusqu'à -70%! Shop Maintenant!' in a promotional page.",
    },
    {
        "timestamp": 1733717408291,
        "context": "clicked 'POUR VOUS' in a page for personalized recommendations.",
    },
    {
        "timestamp": 1733717410469,
        "context": "clicked 'POUR VOUS' in a page for personalized recommendations.",
    },
    {
        "timestamp": 1733717411531,
        "context": "clicked 'Meilleures Ventes' in a page for popular items.",
    },
    {
        "timestamp": 1733717418891,
        "context": "clicked 'CARDIGAN MAILLE UNI À NOUER DEVANT' in a product page.",
    },
    {
        "timestamp": 1733717420491,
        "context": "clicked 'SHOP' in a navigation page.",
    },
    {
        "timestamp": 1733717423819,
        "context": "clicked 'LIVRAISON GRATUITE DÈS 39,00 €' in a page for deals.",
    },
    {
        "timestamp": 1733717425836,
        "context": "clicked 'MIGNONNE' in a page for filtering options.",
    },
    {
        "timestamp": 1733717445241,
        "context": "clicked 'LIVRAISON GRATUITE DÈS 39,00 €' in a product completion page.",
    },
    {
        "timestamp": 1733717448036,
        "context": "clicked 'Offre Folie: Jusqu'à -70%! Shop Maintenant!' in a product completion page.",
    },
    {
        "timestamp": 1733717462105,
        "context": "clicked 'TRIER' in a sorting options page.",
    },
    {
        "timestamp": 1733717465536,
        "context": "clicked 'FILTRER' in a filtering options page.",
    },
    {
        "timestamp": 1733717484962,
        "context": "clicked 'MINIMALIST' in a page for filtering options.",
    },
    {
        "timestamp": 1733717486266,
        "context": "clicked 'KPOP' in a page for filtering options.",
    },
    {
        "timestamp": 1733717488804,
        "context": "clicked 'BAS' in a page for filtering options.",
    },
    {
        "timestamp": 1733717490139,
        "context": "clicked 'ENSEMBLES' in a page for filtering options.",
    },
    {
        "timestamp": 1733717491244,
        "context": "clicked 'MOI' in a navigation page.",
    },
    {
        "timestamp": 1733717492746,
        "context": "clicked 'LIVRAISON GRATUITE DÈS 39,00 €' in a cart page.",
    },
    {
        "timestamp": 1733717497637,
        "context": "clicked 'ici' in a page about shipping and delivery.",
    },
    {
        "timestamp": 1733717498352,
        "context": "clicked 'Se connecter avec Google' in a login page.",
    },
    {
        "timestamp": 1733717498983,
        "context": "clicked 'Se connecter avec Facebook' in a login page.",
    },
    {
        "timestamp": 1733717515543,
        "context": "clicked 'SE CONNECTER / S'INSCRIRE' in a wishlist prompt.",
    },
    {
        "timestamp": 1733717525162,
        "context": "clicked 'ACHETER' in a cart page.",
    },
    {
        "timestamp": 1733717526997,
        "context": "clicked 'LISTE D'ENVIES' in a navigation page.",
    },
    {
        "timestamp": 1733717532691,
        "context": "clicked 'LIVRAISON GRATUITE DÈS 39,00 €' in a product completion page.",
    },
    {
        "timestamp": 1733717537391,
        "context": "clicked 'Offre Folie: Jusqu'à -70%! Shop Maintenant!' in a product completion page.",
    },
    {
        "timestamp": 1733717537995,
        "context": "clicked 'UP TO 70% OFF >> ' in a promotional page.",
    },
    {
        "timestamp": 1733717543221,
        "context": "clicked 'TRIER' in a sorting options page.",
    },
    {
        "timestamp": 1733717544057,
        "context": "clicked 'Meilleures ventes' in a sorting options page.",
    }
]
"""

newdata = demjson3.decode(data)

print(newdata)