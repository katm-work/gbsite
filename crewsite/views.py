from django.shortcuts import render
from datetime import datetime, timedelta
import asyncio

# from crewsite.functions import scrape

def home(request):
    # scraper = asyncio.run(scrape())
    # print(scraper)
    # print(len(scraper))
    return render(request, 'home.html', {'products': ''})

def about(request):
    about_officers = {'Officers': ['Danchou - Polo', 'Police Officer - Qrow', 'Pensioner - Noah']}
    
    about_rules = {
        'Crew Rules': {"Raids":
                       [
                        "Your raid, you decide whether to share or not. We tend to wait for members to get minimum honour (especially in raids that drop blue chests). But in the end, it is up to you.",
                        "Don’t pub other ppl’s raids, unless they say it’s fine.",
                        "During GW, there is a ban on sharing raids other than to crew. (GW raids to be extra clear.) (If you prefer to solo, that’s fine too.)",
                        "Don't bid against the host's share chest. If you are looking for something specific, ask whether you can have it first."
                        ],
                        "General":
                        [
                            "Be nice. Joking and everything is fine, but be considerate of the rest.",
                            "Inform us when you can’t be active as much (especially during GW).",
                            "If something/somebody is bothering you, speak up (either directly in chat or to me/Aymes)."
                            ],
                        "Line/Discord Chat":
                        [
                            "If you want to add something as a note, please contact me or Aymes, so we can examine/add it.",
                            "If you have useful links that can be added, comment it on the respective note and I can add them."
                            ],
                        "Guild War Requirements":
                        [
                            "Minimum honors is 30mil by the end of GW. (No daily honors minimum)",
                            "If you don't hit minimum honors, it counts as missing GW.",
                            "Miss 3 GW during the year and you are likely to be kicked out."
                            ],


                         }
    }
    return render(request, 'about.html', {'about_officers': about_officers,
                                          'about_rules': about_rules})

def forum(request):
    return render(request, 'forum.html', {'products': ''})

def resources(request):
    return render(request, 'resources.html', {'products': ''})