# bb-plugin-hmm-themes

Drastically different themes for [bb](https://getbb.app) that keep the same
layout. Each theme is one CSS file that restyles bb's palette, type and key
components, and appears in Settings → Appearance.

## Themes

| Id | Look |
| --- | --- |
| `brutalist` | Paper and ink with one yellow accent, zero radius, hard offset shadows, Space Grotesk and JetBrains Mono |
| `apple` | macOS system type, soft layered shadows, capsule controls, iMessage-blue user bubbles |
| `paper` | Warm paper, Newsreader serif for answers, IBM Plex for UI, one terracotta accent |
| `retro-os` | 90s desktop: grey bevels, navy gradient header, tooltip-yellow user messages, Tahoma |
| `terminal` | Green phosphor on black, monospace everywhere, scanlines, `you@bb $` prompt |
| `liquid-glass` | Frosted glass panels over a soft gradient wallpaper, capsule controls, glossy blue |

## Tech Stack

- Plain CSS through the manifest `bb.themes` entry
- `@get-bb/plugin-sdk` for the (empty) server entry

## Prerequisites

- bb >= 0.42
- Node.js and npm

## Setup

```sh
git clone git@github.com:fadlihdytullah/bb-plugin-hmm-themes.git
cd bb-plugin-hmm-themes
npm install
```

## Environment

No environment variables are required.

## Run

```sh
npx tsc -p .
bb plugin build
bb theme set plugin:hmm-themes:brutalist
```

After editing a theme file:

```sh
bb plugin reload hmm-themes
```

`paper`, `retro-os`, `terminal` and `liquid-glass` are generated. Edit
`scripts/build-themes.py`, not their CSS files, then:

```sh
python3 scripts/build-themes.py && bb plugin reload hmm-themes
```

## Deploy

```sh
bb plugin install git:https://github.com/fadlihdytullah/bb-plugin-hmm-themes
```

From a local checkout:

```sh
bb plugin install path:.
```

## How it works

- Each theme sets bb's two anchors (`--canvas`, `--ink`), the accent and the
  text tiers in `:root, .light` and `.dark`; bb derives the rest of the
  neutral ramp from them.
- Theme-specific tokens (`--brutal-*`, `--apple-*`) hold the border widths, offsets and
  press timing, so component rules never hard-code values.
- `paper`, `retro-os`, `terminal` and `liquid-glass` share one component
  layer driven by `--hmm-*` tokens (colors, radii, press feedback, chips,
  bubble, composer); each file only sets the tokens and adds its own extras.
  `retro-os`, `terminal` and `liquid-glass` look the same in light and dark
  mode.
- Every theme shares one spacing layer driven by `--hmm-leading`,
  `--hmm-space-1..5`, `--hmm-chip-gap` and `--hmm-row-pad`; each theme only
  sets the values.
- Component rules only use stable hooks: `data-*` attributes and test ids
  such as `form[data-promptbox]`, `[data-testid="app-nav-rail"]` and
  `[data-timeline-row-id]`.
- bb paints the send button through its wrapper and forces the button itself
  transparent with a layered `!important`, so the theme styles the wrapper
  (`div:has(> [data-promptbox-submit-action])`).
- Press feedback is a short transform with an ease-out curve, hover effects
  are limited to fine pointers, and motion is removed under
  `prefers-reduced-motion`.

## Adding a theme

1. Add `themes/<id>.css`, copying the shared spacing rules and setting the
   `--hmm-*` tokens.
2. Add an entry to `bb.themes` in `package.json`.
3. Run `bb plugin reload hmm-themes`, then pick it in Settings → Appearance.
