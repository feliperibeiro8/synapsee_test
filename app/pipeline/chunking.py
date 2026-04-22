import re

def is_sentence_end(word):
    return re.search(r'[.!?]["\')]*$', word) is not None


def chunk_text(text, chunk_size=120, overlap=30, min_words=50, max_extension=50):
    words = text.split()
    chunks = []
    start = 0
    n = len(words)

    while start < n:
        base_end = start + chunk_size
        limit = min(start + chunk_size + max_extension, n)

        end = base_end

        if base_end >= n:
            end = n
        else:
            # Try found a dot going forward
            found_forward = None
            i = base_end

            while i < limit:
                if is_sentence_end(words[i]):
                    found_forward = i
                    break
                i += 1

            if found_forward is not None:
                end = found_forward + 1
            else:
                # If didn't find come back to the last dot
                found_backward = None
                i = base_end - 1

                while i > start:
                    if is_sentence_end(words[i]):
                        found_backward = i
                        break
                    i -= 1

                if found_backward is not None:
                    end = found_backward + 1
                else:
                    # If didn't find any dot at the text, cut at the limit
                    end = base_end

        chunk_words = words[start:end]

        # Avoid chunks without context
        if len(chunk_words) < min_words:
            if chunks:
                chunks[-1] += " " + " ".join(chunk_words)
            else:
                chunks.append(" ".join(chunk_words))
            break

        chunk = " ".join(chunk_words).strip()
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks