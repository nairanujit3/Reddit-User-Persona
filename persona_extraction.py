import os
from urllib.parse import urlparse
from utils.scraper import RedditScraper
from utils.llm_person_builder import PersonaBuilder
from utils.traits_tracker import CitationTracker

def extract_username(url):
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")
    return parts[-1] if "user" in parts else None

def main():
    profile_url = input("Enter Reddit profile URL: ").strip()
    username = extract_username(profile_url)

    if not username:
        print("Invalid Reddit profile URL.")
        return

    scraper = RedditScraper(username)
    posts, comments = scraper.fetch_user_activity(limit=25)

    if not posts and not comments:
        print("No data found for this user.")
        return

    builder = PersonaBuilder()
    persona = builder.build_persona(username, posts, comments)

    output_dir = "personas"
    os.makedirs(output_dir, exist_ok=True)

    persona_path = os.path.join(output_dir, f"{username}_persona.txt")
    with open(persona_path, "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"✅ Persona written to: {persona_path}")

    # print matched citations
    citation_matches = CitationTracker.map_citations(persona, posts, comments)
    if citation_matches:
        print("\n🔍 Example Citations:")
        for cited, source in citation_matches[:3]:
            print(f"→ {cited}\n   ↳ Source: {source[:80]}...\n")

if __name__ == "__main__":
    main()
