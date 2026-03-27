# core/executor.py

from skill import time_skill, web_skill, system_skill

# 🔌 Skill registry (like Alexa skills)
SKILLS = {
    "time": time_skill.run,
    "youtube": web_skill.open_youtube,
    "google": web_skill.search_google,
    "vscode": system_skill.open_vscode,
    "shutdown": system_skill.shutdown,
}


def execute(intent, text):
    """
    Main executor function
    """
    print(f"[EXECUTOR] Intent: {intent}")

    # ✅ 1. Direct intent match
    if intent in SKILLS:
        try:
            return SKILLS[intent](text)
        except TypeError:
            # if skill doesn't take text argument
            return SKILLS[intent]()

    # ✅ 2. Fallback (basic NLP)
    return fallback(text)


# 🔁 Fallback system (VERY IMPORTANT)
def fallback(text):
    """
    Handles unknown commands
    Later: replace with LLM
    """
    text = text.lower()

    if "search" in text:
        return web_skill.search_google(text)

    if "open" in text:
        return system_skill.open_app(text)

    return "Sorry, I didn't understand that."