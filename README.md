# AI Blog Generator — YouTube transcript → blog post

A small tool that turns a YouTube video transcript into a publishable blog
post using an LLM. Built as a portfolio piece to demonstrate clean
LLM-integration patterns: prompt templates, structured output, rate
limiting, and cost guardrails.

---

## 🎯 What it does

1. Accepts a YouTube URL.
2. Fetches the transcript via `youtube-transcript-api` (auto-captions, no API key required).
3. Chunks the transcript (token-aware, sliding window with overlap).
4. Sends each chunk + a prompt template to the LLM and assembles the result into a single Markdown post with headings, intro, body, and conclusion.
5. Saves the post as a `.md` file locally and (optionally) publishes to a static site generator.

---

## 🧰 Tech stack

| Layer | Choice |
|---|---|
| Language | Python 3.11 |
| LLM | OpenAI API (`gpt-4o-mini` default, configurable to Anthropic / local Ollama) |
| Transcript | `youtube-transcript-api` |
| Tokenizer | `tiktoken` |
| Output | Markdown files (Hugo / Jekyll / plain compatible) |

---

## 🚀 Getting started

### 1. Install

```bash
git clone https://github.com/ekowi/ai_blog_gen.git
cd ai_blog_gen
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure

```bash
cp .env.example .env
# Required
OPENAI_API_KEY=sk-...
LLM_MODEL=gpt-4o-mini
# Optional
OUTPUT_DIR=./posts
MAX_TOKENS_PER_CHUNK=3000
```

### 3. Run

```bash
python -m ai_blog_gen "https://www.youtube.com/watch?v=VIDEO_ID"
# → writes ./posts/VIDEO_ID.md
```

Or import the module:

```python
from ai_blog_gen import generate_post

post_md = generate_post("https://www.youtube.com/watch?v=VIDEO_ID")
print(post_md[:500])
```

---

## ⚙️ How it works

```
YouTube URL
   │
   ▼
┌──────────────────────┐
│ fetch_transcript()   │  youtube-transcript-api (auto-captions)
└──────────────────────┘
   │ list[{text, start, duration}]
   ▼
┌──────────────────────┐
│ chunk_with_overlap() │  tiktoken-based, sliding window, 3000 tok chunks
└──────────────────────┘
   │ list[str]
   ▼
┌──────────────────────┐
│ map: summarize chunk │  gpt-4o-mini, prompt template enforces JSON output
└──────────────────────┘
   │ list[str]
   ▼
┌──────────────────────┐
│ reduce: assemble     │  final pass generates intro + conclusion + headings
└──────────────────────┘
   │ Markdown str
   ▼
./posts/VIDEO_ID.md
```

Map-reduce pattern keeps long videos within the LLM context window without
losing coherence at chunk boundaries.

---

## 💸 Cost & limits

- `gpt-4o-mini` costs ~$0.15 per 1M input tokens. A 1-hour video (~10k
  transcript tokens) typically costs < $0.01 to process.
- Rate-limit aware: exponential backoff on 429, single-flight per video URL.
- Auto-captions only — videos without captions raise `TranscriptsDisabled`
  with a clear error message.
- **Not production-grade** — this is a portfolio piece. No auth, no DB, no
  multi-tenant. Treat as a starting point.

---

## 🛣️ Possible improvements

- Swap to Anthropic Claude via the official SDK for higher-quality output.
- Add RAG: index existing blog posts and use them as style references.
- Output to Hugo / Astro directly via their content APIs.
- Stream tokens to the terminal for long videos.

---

## 📝 License

MIT — see `LICENSE`.

---

<sub>Part of my [GitHub profile portfolio](https://github.com/ekowi).</sub>