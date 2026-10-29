# VSL Scriptwriter

A reusable AI skill for writing video sales letters that sound like a real person and address real buying decisions.

Built for physical products, software, services, courses, coaching, and memberships. It adapts the script to the audience, offer, evidence, and next action, with natural spoken language, believable buyer psychology, and no em dashes.

## What it does

- Writes complete VSL scripts, rewrites existing drafts, and audits weak sales arguments.
- Develops three opening options, then uses one in the full script.
- Explains the product, handles relevant objections, and closes with a clear call to action.
- Separates verified facts from assumptions and flags missing evidence.
- Includes spoken word count and estimated runtime.
- Avoids invented testimonials, results, prices, guarantees, and scarcity.

This is a text-based skill. It does not generate or render videos. No API key, paid service, or package installation is required to use the skill files. You need an AI assistant that can read skill instructions; optional product research depends on that assistant's tools.

## Install in Codex

With Git installed, clone this repository into your personal skills directory:

```bash
git clone https://github.com/ai-saas-wizard/vsl-scriptwriter.git "${CODEX_HOME:-$HOME/.codex}/skills/vsl-scriptwriter"
```

If that directory already exists, inspect your existing copy before replacing it. The clone command intentionally will not overwrite it.

Alternatively, [download the ZIP](https://github.com/ai-saas-wizard/vsl-scriptwriter/archive/refs/heads/main.zip), extract it, and copy the folder as `vsl-scriptwriter` into your Codex skills directory. Keep `SKILL.md`, `agents/`, and `references/` together.

Start a new Codex task after installation. Invoke it explicitly with `$vsl-scriptwriter`, or ask for a VSL script and let the assistant select the skill when appropriate.

## Quick start

```text
Use $vsl-scriptwriter to write a 4-minute VSL for my product.

Product: [what you sell]
Audience: [who buys it and their situation]
Offer and price: [what is included and payment terms]
How it works: [the actual process or product mechanism]
Evidence: [demonstrations, specifications, or verified customer results]
Main objections: [what buyers ask before purchasing]
Traffic: [where the viewer comes from and what they already know]
Next action: [buy, start a trial, book a call, or apply]
Voice and language: [how the speaker should sound]
Guarantees and restrictions: [actual terms, or none]

Use natural spoken language, realistic buyer psychology, and no em dashes.
Do not invent missing facts.
```

You do not need every field to get started. The skill asks for essential missing context and marks unresolved business facts instead of inventing them.

### Rewrite a draft

```text
Use $vsl-scriptwriter to rewrite the script below for a skeptical,
product-aware audience. Keep the offer and confirmed facts unchanged.
Make it conversational, remove em dashes, and strengthen the evidence
and objection handling. Target 3 minutes.

[Paste script and supporting product facts]
```

### Audit a VSL

```text
Use $vsl-scriptwriter to audit this VSL. Identify the biggest problems
with clarity, credibility, buyer psychology, and the next action.
Suggest concrete edits without inventing proof or promising a conversion lift.

[Paste script]
```

For a complete fictional input you can try, see [the example brief](examples/product-brief.md).

## Other assistants

The core instructions are ordinary Markdown. In an assistant that supports `SKILL.md` packages, install this folder using that assistant's documented skill mechanism. Otherwise, supply `SKILL.md` and both reference files as context and ask the assistant to follow them. The `agents/openai.yaml` file contains Codex UI metadata; other tools may ignore it.

Only Codex packaging has been checked here. Output quality and instruction compliance depend on the model and the product information you provide.

## How the writing works

The skill starts with the buying decision, models the audience's actual concerns, and chooses a compact or extended structure. It develops relevance, explanation, evidence, offer details, objections, and a clear next step. A final editing pass checks factual support, spoken flow, runtime, and punctuation.

It does not force every product into a pain-heavy story. Enjoyment, craft, convenience, and fit can be the right reasons to buy.

## Sources and attribution

Inspired by publicly available VSL teaching and the two reference videos:

- [How to Script a Sales Video That Actually Sells](https://www.youtube.com/watch?v=00MhX-4guQo), MoreMozi: direct Hormozi teaching.
- [Alex Hormozi explains how to create the perfect VSL](https://www.youtube.com/watch?v=MEsSN187wUI), Stefan van de Vlasakker: another creator's interpretation.

See [source notes](references/sources-and-frameworks.md) for timestamps, supplementary research, and attribution limits. The exact VSL passage requested from *$100M Leads* was not verified. This repository contains original instructions, not a reproduction of the book or a claim to its exact framework.

This is an independent project, not affiliated with or endorsed by Alex Hormozi, Acquisition.com, or the referenced creators. Full video transcripts and book text are not distributed.

## Files

```text
vsl-scriptwriter/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── buyer-psychology.md
│   └── sources-and-frameworks.md
├── examples/product-brief.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Contributing and license

Improvements and examples are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

Original repository materials are released under the [MIT License](LICENSE). Third-party books, videos, names, and trademarks remain the property of their respective owners; the license does not grant rights to those materials.
