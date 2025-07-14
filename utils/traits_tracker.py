class CitationTracker:
    @staticmethod
    def map_citations(persona_text, posts, comments):
        matched_quotes = []

        all_content = posts + comments
        for line in persona_text.splitlines():
            for quote in all_content:
                if quote[:50] in line:  # crude match for start of content
                    matched_quotes.append((line.strip(), quote.strip()))

        return matched_quotes
