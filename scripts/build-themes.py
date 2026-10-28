import os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'themes')

BASE='''::selection {
  background: var(--hmm-selection-bg);
  color: var(--hmm-selection-fg);
}

:is(a, button, [role="button"], [role="tab"], [role="menuitem"], [role="option"], input, select):focus-visible {
  outline: var(--hmm-focus);
  outline-offset: 2px;
}

[data-testid="app-nav-rail"] {
  background: var(--hmm-rail-bg);
  border-right: var(--hmm-divider);
}

[data-nav-rail-item] button {
  border-radius: var(--hmm-radius-sm);
}

[data-testid="app-nav-rail"] button[aria-current="page"] {
  background: var(--hmm-rail-active-bg);
  color: var(--hmm-rail-active-fg);
  box-shadow: var(--hmm-rail-active-shadow);
}

[data-sidebar="sidebar"] {
  background: var(--hmm-sidebar-bg);
}

[data-testid="nav-rail-header"] > button[aria-keyshortcuts="Shift+Meta+O"] {
  background: var(--hmm-new-bg);
  color: var(--hmm-new-fg);
  border-radius: var(--hmm-radius-sm);
  box-shadow: var(--hmm-new-shadow);
  font-weight: 600;
  transition: transform var(--hmm-press-duration) var(--hmm-ease);
}

[data-testid="nav-rail-header"] > button[aria-keyshortcuts="Shift+Meta+O"] svg {
  color: var(--hmm-icon-accent);
}

[data-testid="nav-rail-header"] > button[aria-keyshortcuts="Shift+Meta+O"]:active {
  transform: var(--hmm-press);
  box-shadow: var(--hmm-new-shadow-pressed);
}

[data-sidebar="sidebar"] span.select-none.uppercase {
  font-family: var(--hmm-label-font);
  font-style: var(--hmm-label-style);
  font-size: var(--hmm-label-size);
  text-transform: var(--hmm-label-transform);
  letter-spacing: var(--hmm-label-spacing);
  color: var(--muted-foreground);
  margin-block: var(--hmm-space-2);
}

[data-collection-id] > div {
  color: var(--ink);
  font-size: 13px;
  font-weight: 600;
  padding-block: calc(var(--hmm-row-pad) + 1px);
}

[data-collection-id] > div svg {
  color: var(--hmm-icon-accent);
}

[data-project-id] > div:first-child,
a[data-sidebar-thread-id] {
  font-size: 13px;
  border-radius: var(--hmm-radius-sm);
  padding-block: var(--hmm-row-pad);
}

[data-project-id] > div:first-child {
  color: var(--ink);
}

[data-project-id] > [class*="border-l"] {
  border-left-color: var(--hmm-guide);
  margin-block: var(--hmm-space-1);
}

a[data-sidebar-thread-id][aria-current="page"] {
  background: var(--hmm-active-bg);
  color: var(--hmm-active-fg);
  box-shadow: var(--hmm-active-shadow);
  font-weight: 600;
}

a[data-sidebar-thread-id][aria-current="page"] * {
  color: inherit;
}

section[aria-label="Sidebar activity"] {
  border-top: var(--hmm-divider);
  background: var(--hmm-sidebar-bg);
}

section[aria-label="Sidebar activity"] .overflow-y-auto {
  background: var(--hmm-card-bg);
  border: var(--hmm-card-border);
  border-radius: var(--hmm-radius-md);
  box-shadow: var(--hmm-card-shadow);
}

a[data-activity-thread-id] {
  border-radius: var(--hmm-radius-sm);
  padding-block: var(--hmm-space-2);
}

a[data-activity-thread-id][data-active="true"] {
  background: var(--hmm-activity-active-bg);
  color: var(--hmm-activity-active-fg);
}

a[data-activity-thread-id][data-active="true"] .text-muted-foreground {
  color: inherit;
}

[data-testid="sidebar-footer-row"] {
  border-top: var(--hmm-divider);
}

[data-sidebar="menu-button"] {
  border-radius: var(--hmm-radius-sm);
}

header:has(> [data-testid="app-page-header-content-row"]) {
  background: var(--hmm-header-bg);
  color: var(--hmm-header-fg);
  border-bottom: var(--hmm-divider);
  backdrop-filter: var(--hmm-header-filter);
  -webkit-backdrop-filter: var(--hmm-header-filter);
}

form[data-promptbox] {
  background: var(--hmm-composer-bg);
  border: var(--hmm-composer-border);
  border-radius: var(--hmm-radius-lg);
  box-shadow: var(--hmm-composer-shadow);
  backdrop-filter: var(--hmm-panel-filter);
  -webkit-backdrop-filter: var(--hmm-panel-filter);
  transition: box-shadow 200ms var(--hmm-ease);
}

form[data-promptbox]:focus-within {
  box-shadow: var(--hmm-composer-shadow-focus);
}

div:has(> [data-promptbox-submit-action]) {
  background: var(--hmm-send-bg);
  color: var(--hmm-send-fg);
  border-radius: var(--hmm-send-radius);
  box-shadow: var(--hmm-send-shadow);
  transition: transform var(--hmm-press-duration) var(--hmm-ease), background-color var(--hmm-press-duration) var(--hmm-ease);
}

div:has(> [data-promptbox-submit-action]) button {
  color: inherit;
  border-radius: var(--hmm-send-radius);
}

div:has(> [data-promptbox-submit-action]:not(:disabled)):active {
  transform: var(--hmm-press);
  box-shadow: var(--hmm-send-shadow-pressed);
}

div:has(> [data-promptbox-submit-action]:disabled) {
  background: var(--hmm-send-disabled-bg);
  color: var(--subtle-foreground);
  box-shadow: var(--hmm-send-disabled-shadow);
  opacity: 1;
}

[data-promptbox-submit-action]:disabled {
  opacity: 1;
}

[data-follow-up-composer-footer] {
  margin-top: var(--hmm-space-3);
}

[data-timeline-row-id] {
  padding-block: var(--hmm-space-2);
}

[data-timeline-row-id*=":user"] .bg-surface-recessed {
  background: var(--hmm-bubble-bg);
  color: var(--hmm-bubble-fg);
  border: var(--hmm-bubble-border);
  border-radius: var(--hmm-bubble-radius);
  box-shadow: var(--hmm-bubble-shadow);
  font-family: var(--hmm-bubble-font);
  font-size: var(--hmm-prose-size);
  padding: var(--hmm-space-3) var(--hmm-space-4);
  line-height: 1.6;
}

[data-timeline-row-id*=":user"] .bg-surface-recessed * {
  color: inherit;
}

[data-timeline-row-id*=":user"] .bg-surface-recessed [data-markdown-preview] {
  font-family: inherit;
  font-size: inherit;
  text-shadow: none;
}

[data-timeline-row-id*=":user"] .bg-surface-recessed .prompt-mention-pill {
  background: var(--hmm-bubble-pill-bg);
  color: var(--hmm-bubble-pill-fg);
  border-color: var(--hmm-bubble-pill-border);
  border-radius: var(--hmm-radius-sm);
}

[data-timeline-row-id*=":user"] .bg-surface-recessed code {
  background: var(--hmm-bubble-pill-bg);
}

[data-markdown-preview] {
  font-family: var(--hmm-prose-font);
  font-size: var(--hmm-prose-size);
  line-height: var(--hmm-leading);
}

[data-markdown-preview] :is(p, ul, ol, table, pre, blockquote) {
  margin-block: var(--hmm-space-3);
}

[data-markdown-preview] > :first-child {
  margin-top: 0;
}

[data-markdown-preview] > :last-child {
  margin-bottom: 0;
}

[data-markdown-preview] li + li {
  margin-top: var(--hmm-space-2);
}

[data-markdown-preview] :is(th, td) {
  padding: var(--hmm-space-2) var(--hmm-space-3);
}

[data-markdown-preview] code {
  font-family: var(--font-mono);
  font-size: 0.875em;
  border-radius: var(--hmm-radius-xs);
}

[data-markdown-preview] pre {
  border-radius: var(--hmm-radius-md);
}

[data-bb-plugin="hmm-suggest"] .flex-wrap {
  gap: var(--hmm-chip-gap);
  margin-block: var(--hmm-space-4);
}

[data-bb-plugin="hmm-suggest"] button {
  background: var(--hmm-chip-bg);
  color: var(--hmm-chip-fg);
  border: var(--hmm-chip-border);
  border-radius: var(--hmm-chip-radius);
  box-shadow: var(--hmm-chip-shadow);
  font-family: var(--hmm-chip-font);
  font-weight: 500;
  padding: var(--hmm-space-2) var(--hmm-space-4);
  transition: transform var(--hmm-press-duration) var(--hmm-ease), background-color var(--hmm-press-duration) var(--hmm-ease);
}

[data-bb-plugin="hmm-suggest"] button:active:not(:disabled) {
  transform: var(--hmm-press);
  box-shadow: var(--hmm-chip-shadow-pressed);
}

@media (hover: hover) and (pointer: fine) {
  [data-bb-plugin="hmm-suggest"] button:hover:not(:disabled) {
    background: var(--hmm-chip-hover-bg);
    color: var(--hmm-chip-hover-fg);
  }
}

@media (prefers-reduced-motion: reduce) {
  form[data-promptbox],
  div:has(> [data-promptbox-submit-action]),
  [data-testid="nav-rail-header"] > button[aria-keyshortcuts="Shift+Meta+O"],
  [data-bb-plugin="hmm-suggest"] button {
    transition: none;
  }
}
'''

SPACE='''  --hmm-space-1: 4px;
  --hmm-space-2: 8px;
  --hmm-space-3: 12px;
  --hmm-space-4: 16px;
  --hmm-space-5: 24px;
'''

themes={}

themes['paper']=('''@import url("https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400..700;1,6..72,400..700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap");

:root,
.light {
  --font-sans: "IBM Plex Sans", ui-sans-serif, system-ui, sans-serif;
  --font-serif: "Newsreader", Georgia, serif;
  --font-mono: "IBM Plex Mono", ui-monospace, Menlo, monospace;
  --font-terminal: "IBM Plex Mono", monospace;

  --canvas: #f6f1e7;
  --ink: #2b2620;
  --primary: #a3412a;
  --primary-foreground: #fbf8f2;

  --paper-raised: #fbf8f2;
  --paper-sidebar: #efe8da;
  --paper-hairline: color-mix(in oklch, var(--ink) 13%, transparent);

  --card: var(--paper-raised);
  --popover: var(--paper-raised);
  --sidebar: var(--paper-sidebar);
  --sidebar-foreground: var(--ink);
  --sidebar-accent: color-mix(in oklch, var(--ink) 7%, var(--paper-sidebar));
  --sidebar-accent-foreground: var(--ink);
  --sidebar-border: var(--paper-hairline);
  --sidebar-ring: var(--primary);
  --border: color-mix(in oklch, var(--ink) 14%, var(--canvas));
  --border-seam: color-mix(in oklch, var(--ink) 11%, var(--canvas));
  --border-seam-vertical: var(--border-seam);
  --input: color-mix(in oklch, var(--ink) 22%, var(--canvas));
  --surface-scrim: color-mix(in oklab, var(--canvas) 88%, transparent);

  --muted-foreground: color-mix(in oklch, var(--ink) 70%, var(--canvas));
  --subtle-foreground: color-mix(in oklch, var(--ink) 58%, var(--canvas));
  --readback-foreground: color-mix(in oklch, var(--ink) 64%, var(--canvas));

  --destructive: #b3261e;
  --destructive-foreground: #fbf8f2;
  --destructive-text: #a3231c;
  --warning: #9a4a00;
  --warning-text: #9a4a00;
  --attention: #c06a00;
  --success: #3f6b2e;
  --diff-added: #3f6b2e;
  --diff-removed: #a3231c;
  --pr-merged: #6b3fa0;
  --file-accent: #a3412a;

  --radius: 8px;
  --shadow-lift: 0 6px 18px -6px #2b262024, 0 1px 2px 0 #2b262014;

  --hmm-leading: 1.7;
''' + SPACE + '''  --hmm-chip-gap: 10px;
  --hmm-row-pad: 4px;
  --hmm-radius-xs: 4px;
  --hmm-radius-sm: 6px;
  --hmm-radius-md: 8px;
  --hmm-radius-lg: 12px;
  --hmm-ease: cubic-bezier(0.23, 1, 0.32, 1);
  --hmm-press-duration: 160ms;
  --hmm-press: scale(0.97);
  --hmm-divider: 1px solid var(--paper-hairline);
  --hmm-focus: 2px solid var(--primary);
  --hmm-selection-bg: color-mix(in oklch, var(--primary) 22%, transparent);
  --hmm-selection-fg: inherit;
  --hmm-icon-accent: var(--primary);
  --hmm-rail-bg: var(--paper-sidebar);
  --hmm-rail-active-bg: var(--paper-raised);
  --hmm-rail-active-fg: var(--primary);
  --hmm-rail-active-shadow: 0 0 0 1px var(--paper-hairline);
  --hmm-sidebar-bg: var(--paper-sidebar);
  --hmm-new-bg: var(--paper-raised);
  --hmm-new-fg: var(--ink);
  --hmm-new-shadow: 0 0 0 1px var(--paper-hairline);
  --hmm-new-shadow-pressed: var(--hmm-new-shadow);
  --hmm-label-font: var(--font-serif);
  --hmm-label-style: italic;
  --hmm-label-size: 13px;
  --hmm-label-transform: none;
  --hmm-label-spacing: 0;
  --hmm-guide: var(--paper-hairline);
  --hmm-active-bg: color-mix(in oklch, var(--ink) 10%, var(--paper-sidebar));
  --hmm-active-fg: var(--ink);
  --hmm-active-shadow: inset 2px 0 0 var(--primary);
  --hmm-card-bg: var(--paper-raised);
  --hmm-card-border: 1px solid var(--paper-hairline);
  --hmm-card-shadow: none;
  --hmm-activity-active-bg: color-mix(in oklch, var(--primary) 8%, transparent);
  --hmm-activity-active-fg: var(--ink);
  --hmm-header-bg: var(--surface-scrim);
  --hmm-header-fg: inherit;
  --hmm-header-filter: blur(12px);
  --hmm-panel-filter: none;
  --hmm-composer-bg: var(--paper-raised);
  --hmm-composer-border: 1px solid color-mix(in oklch, var(--ink) 16%, transparent);
  --hmm-composer-shadow: var(--shadow-lift);
  --hmm-composer-shadow-focus: var(--shadow-lift), 0 0 0 3px color-mix(in oklch, var(--primary) 16%, transparent);
  --hmm-send-bg: var(--primary);
  --hmm-send-fg: var(--primary-foreground);
  --hmm-send-radius: 8px;
  --hmm-send-shadow: none;
  --hmm-send-shadow-pressed: none;
  --hmm-send-disabled-bg: color-mix(in oklch, var(--ink) 9%, transparent);
  --hmm-send-disabled-shadow: none;
  --hmm-bubble-bg: #ece3d1;
  --hmm-bubble-fg: var(--ink);
  --hmm-bubble-border: 1px solid var(--paper-hairline);
  --hmm-bubble-radius: 10px;
  --hmm-bubble-shadow: none;
  --hmm-bubble-font: var(--font-sans);
  --hmm-bubble-pill-bg: transparent;
  --hmm-bubble-pill-fg: var(--primary);
  --hmm-bubble-pill-border: var(--primary);
  --hmm-prose-font: var(--font-serif);
  --hmm-prose-size: 15px;
  --hmm-chip-bg: transparent;
  --hmm-chip-fg: var(--ink);
  --hmm-chip-border: 1px solid color-mix(in oklch, var(--ink) 24%, transparent);
  --hmm-chip-radius: 999px;
  --hmm-chip-shadow: none;
  --hmm-chip-shadow-pressed: none;
  --hmm-chip-font: var(--font-sans);
  --hmm-chip-hover-bg: var(--paper-raised);
  --hmm-chip-hover-fg: var(--primary);
}

.dark {
  --canvas: #1e1b17;
  --ink: #e8e0d0;
  --primary: #e08a6d;
  --primary-foreground: #1e1b17;

  --paper-raised: #26221d;
  --paper-sidebar: #191713;

  --destructive: #ff8a7a;
  --destructive-foreground: #1e1b17;
  --destructive-text: #ff9d8f;
  --warning: #f0a35c;
  --warning-text: #f0a35c;
  --attention: #f0a35c;
  --success: #9cc985;
  --diff-added: #9cc985;
  --diff-removed: #ff9d8f;
  --pr-merged: #c3a3ef;
  --file-accent: #e08a6d;

  --hmm-bubble-bg: #2c2721;
}
''', '')

BEVEL_UP='inset -1px -1px #0a0a0a, inset 1px 1px #ffffff, inset -2px -2px #808080, inset 2px 2px #dfdfdf'
BEVEL_DOWN='inset -1px -1px #ffffff, inset 1px 1px #0a0a0a, inset -2px -2px #dfdfdf, inset 2px 2px #808080'

themes['retro-os']=(''':root,
.light,
.dark {
  --font-sans: Tahoma, "Segoe UI", Verdana, "MS Sans Serif", sans-serif;
  --font-mono: "Courier New", Courier, monospace;
  --font-terminal: "Courier New", monospace;

  --canvas: #ffffff;
  --ink: #000000;
  --primary: #000080;
  --primary-foreground: #ffffff;

  --retro-face: #c0c0c0;
  --retro-shadow: #808080;
  --retro-light: #dfdfdf;
  --retro-up: ''' + BEVEL_UP + ''';
  --retro-down: ''' + BEVEL_DOWN + ''';

  --background: var(--canvas);
  --card: var(--retro-face);
  --popover: var(--retro-face);
  --secondary: var(--retro-face);
  --muted: var(--retro-light);
  --sidebar: var(--retro-face);
  --sidebar-foreground: var(--ink);
  --sidebar-accent: #b4b4b4;
  --sidebar-accent-foreground: var(--ink);
  --sidebar-border: var(--retro-shadow);
  --sidebar-ring: var(--ink);
  --border: var(--retro-shadow);
  --border-hairline: var(--retro-shadow);
  --border-seam: var(--retro-shadow);
  --border-seam-vertical: var(--border-seam);
  --input: var(--retro-shadow);
  --surface-scrim: var(--retro-face);
  --surface-recessed: var(--retro-light);
  --surface-selected: var(--primary);

  --muted-foreground: #3d3d3d;
  --subtle-foreground: #595959;
  --readback-foreground: #4a4a4a;

  --destructive: #c00000;
  --destructive-foreground: #ffffff;
  --destructive-text: #a00000;
  --warning: #806000;
  --warning-text: #806000;
  --attention: #c08000;
  --success: #006400;
  --diff-added: #006400;
  --diff-removed: #a00000;
  --pr-merged: #800080;
  --file-accent: #000080;

  --radius: 0px;
  --radius-xs: 0px;
  --radius-sm: 0px;
  --radius-md: 0px;
  --radius-lg: 0px;
  --radius-xl: 0px;
  --radius-2xl: 0px;
  --shadow-lift: none;

  --hmm-leading: 1.6;
''' + SPACE + '''  --hmm-chip-gap: 8px;
  --hmm-row-pad: 3px;
  --hmm-radius-xs: 0px;
  --hmm-radius-sm: 0px;
  --hmm-radius-md: 0px;
  --hmm-radius-lg: 0px;
  --hmm-ease: linear;
  --hmm-press-duration: 0ms;
  --hmm-press: translate(1px, 1px);
  --hmm-divider: 1px solid var(--retro-shadow);
  --hmm-focus: 1px dotted var(--ink);
  --hmm-selection-bg: var(--primary);
  --hmm-selection-fg: #ffffff;
  --hmm-icon-accent: #b8860b;
  --hmm-rail-bg: var(--retro-face);
  --hmm-rail-active-bg: var(--retro-face);
  --hmm-rail-active-fg: var(--primary);
  --hmm-rail-active-shadow: var(--retro-down);
  --hmm-sidebar-bg: var(--retro-face);
  --hmm-new-bg: var(--retro-face);
  --hmm-new-fg: var(--ink);
  --hmm-new-shadow: var(--retro-up);
  --hmm-new-shadow-pressed: var(--retro-down);
  --hmm-label-font: var(--font-sans);
  --hmm-label-style: normal;
  --hmm-label-size: 12px;
  --hmm-label-transform: none;
  --hmm-label-spacing: 0;
  --hmm-guide: var(--retro-shadow);
  --hmm-active-bg: var(--primary);
  --hmm-active-fg: #ffffff;
  --hmm-active-shadow: 0 0 0 1px #ffff00;
  --hmm-card-bg: #ffffff;
  --hmm-card-border: 0;
  --hmm-card-shadow: var(--retro-down);
  --hmm-activity-active-bg: var(--primary);
  --hmm-activity-active-fg: #ffffff;
  --hmm-header-bg: linear-gradient(90deg, #000080, #1084d0);
  --hmm-header-fg: #ffffff;
  --hmm-header-filter: none;
  --hmm-panel-filter: none;
  --hmm-composer-bg: #ffffff;
  --hmm-composer-border: 0;
  --hmm-composer-shadow: var(--retro-down);
  --hmm-composer-shadow-focus: var(--retro-down), 0 0 0 1px var(--ink);
  --hmm-send-bg: var(--retro-face);
  --hmm-send-fg: var(--ink);
  --hmm-send-radius: 0px;
  --hmm-send-shadow: var(--retro-up);
  --hmm-send-shadow-pressed: var(--retro-down);
  --hmm-send-disabled-bg: var(--retro-face);
  --hmm-send-disabled-shadow: var(--retro-up);
  --hmm-bubble-bg: #ffffe1;
  --hmm-bubble-fg: var(--ink);
  --hmm-bubble-border: 1px solid var(--ink);
  --hmm-bubble-radius: 0px;
  --hmm-bubble-shadow: none;
  --hmm-bubble-font: var(--font-sans);
  --hmm-bubble-pill-bg: var(--retro-face);
  --hmm-bubble-pill-fg: var(--primary);
  --hmm-bubble-pill-border: var(--retro-shadow);
  --hmm-prose-font: var(--font-sans);
  --hmm-prose-size: 15px;
  --hmm-chip-bg: var(--retro-face);
  --hmm-chip-fg: var(--ink);
  --hmm-chip-border: 0;
  --hmm-chip-radius: 0px;
  --hmm-chip-shadow: var(--retro-up);
  --hmm-chip-shadow-pressed: var(--retro-down);
  --hmm-chip-font: var(--font-sans);
  --hmm-chip-hover-bg: var(--retro-face);
  --hmm-chip-hover-fg: var(--primary);
}
''', '''
header:has(> [data-testid="app-page-header-content-row"]) :is(button, a, span, h1, h2) {
  color: #ffffff;
}

[data-testid="app-nav-rail"] button[aria-current="page"] {
  color: var(--primary);
}

[data-sidebar="content"] {
  background: #ffffff;
  box-shadow: var(--retro-down);
  margin: 4px;
}

[data-sidebar="sidebar"] span.select-none.uppercase {
  color: var(--ink);
  font-weight: 700;
}

[data-markdown-preview] pre {
  background: #ffffff;
  box-shadow: var(--retro-down);
}

[data-markdown-preview] code {
  background: var(--retro-light);
}
''')

themes['terminal']=('''@import url("https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400..800&display=swap");

:root,
.light,
.dark {
  --font-sans: "JetBrains Mono", ui-monospace, Menlo, monospace;
  --font-serif: "JetBrains Mono", ui-monospace, monospace;
  --font-mono: "JetBrains Mono", ui-monospace, Menlo, monospace;
  --font-terminal: "JetBrains Mono", monospace;

  --canvas: #0a0e0a;
  --ink: #4af626;
  --primary: #4af626;
  --primary-foreground: #0a0e0a;

  --term-dim: #3fa34d;
  --term-line: #1e5b28;
  --term-amber: #ffb000;
  --term-bright: #e8ffe0;
  --term-panel: #0d140d;

  --background: var(--canvas);
  --card: var(--term-panel);
  --popover: var(--term-panel);
  --sidebar: var(--canvas);
  --sidebar-foreground: var(--ink);
  --sidebar-accent: #122312;
  --sidebar-accent-foreground: var(--ink);
  --sidebar-border: var(--term-line);
  --sidebar-ring: var(--ink);
  --border: var(--term-line);
  --border-hairline: var(--term-line);
  --border-seam: var(--term-line);
  --border-seam-vertical: var(--border-seam);
  --input: var(--term-line);
  --surface-scrim: var(--canvas);
  --surface-recessed: #122312;
  --surface-raised: #0f1a0f;

  --muted-foreground: var(--term-dim);
  --subtle-foreground: #36893f;
  --readback-foreground: var(--term-dim);

  --destructive: #ff5555;
  --destructive-foreground: #0a0e0a;
  --destructive-text: #ff6e6e;
  --warning: var(--term-amber);
  --warning-text: var(--term-amber);
  --attention: var(--term-amber);
  --success: var(--ink);
  --diff-added: var(--ink);
  --diff-removed: #ff6e6e;
  --pr-merged: #c792ea;
  --file-accent: var(--term-amber);

  --radius: 0px;
  --radius-xs: 0px;
  --radius-sm: 0px;
  --radius-md: 0px;
  --radius-lg: 0px;
  --radius-xl: 0px;
  --radius-2xl: 0px;
  --shadow-lift: none;

  --hmm-leading: 1.7;
''' + SPACE + '''  --hmm-chip-gap: 12px;
  --hmm-row-pad: 3px;
  --hmm-radius-xs: 0px;
  --hmm-radius-sm: 0px;
  --hmm-radius-md: 0px;
  --hmm-radius-lg: 0px;
  --hmm-ease: steps(2, end);
  --hmm-press-duration: 80ms;
  --hmm-press: none;
  --hmm-divider: 1px solid var(--term-line);
  --hmm-focus: 1px solid var(--term-amber);
  --hmm-selection-bg: var(--ink);
  --hmm-selection-fg: var(--canvas);
  --hmm-icon-accent: var(--ink);
  --hmm-rail-bg: var(--canvas);
  --hmm-rail-active-bg: var(--ink);
  --hmm-rail-active-fg: var(--canvas);
  --hmm-rail-active-shadow: none;
  --hmm-sidebar-bg: var(--canvas);
  --hmm-new-bg: transparent;
  --hmm-new-fg: var(--ink);
  --hmm-new-shadow: inset 0 0 0 1px var(--ink);
  --hmm-new-shadow-pressed: inset 0 0 0 1px var(--term-amber);
  --hmm-label-font: var(--font-mono);
  --hmm-label-style: normal;
  --hmm-label-size: 11px;
  --hmm-label-transform: uppercase;
  --hmm-label-spacing: 0.12em;
  --hmm-guide: var(--term-line);
  --hmm-active-bg: var(--ink);
  --hmm-active-fg: var(--canvas);
  --hmm-active-shadow: none;
  --hmm-card-bg: transparent;
  --hmm-card-border: 1px solid var(--term-line);
  --hmm-card-shadow: none;
  --hmm-activity-active-bg: #122312;
  --hmm-activity-active-fg: var(--ink);
  --hmm-header-bg: var(--canvas);
  --hmm-header-fg: var(--ink);
  --hmm-header-filter: none;
  --hmm-panel-filter: none;
  --hmm-composer-bg: var(--canvas);
  --hmm-composer-border: 1px solid var(--ink);
  --hmm-composer-shadow: none;
  --hmm-composer-shadow-focus: 0 0 0 1px var(--ink), 0 0 18px -6px var(--ink);
  --hmm-send-bg: var(--ink);
  --hmm-send-fg: var(--canvas);
  --hmm-send-radius: 0px;
  --hmm-send-shadow: none;
  --hmm-send-shadow-pressed: none;
  --hmm-send-disabled-bg: transparent;
  --hmm-send-disabled-shadow: inset 0 0 0 1px var(--term-line);
  --hmm-bubble-bg: #122312;
  --hmm-bubble-fg: var(--term-bright);
  --hmm-bubble-border: 0;
  --hmm-bubble-radius: 0px;
  --hmm-bubble-shadow: inset 2px 0 0 var(--term-amber);
  --hmm-bubble-font: var(--font-mono);
  --hmm-bubble-pill-bg: var(--ink);
  --hmm-bubble-pill-fg: var(--canvas);
  --hmm-bubble-pill-border: var(--ink);
  --hmm-prose-font: var(--font-mono);
  --hmm-prose-size: 15px;
  --hmm-chip-bg: transparent;
  --hmm-chip-fg: var(--ink);
  --hmm-chip-border: 1px solid var(--ink);
  --hmm-chip-radius: 0px;
  --hmm-chip-shadow: none;
  --hmm-chip-shadow-pressed: none;
  --hmm-chip-font: var(--font-mono);
  --hmm-chip-hover-bg: var(--ink);
  --hmm-chip-hover-fg: var(--canvas);

  --ansi-0: #0a0e0a;
  --ansi-1: #ff5555;
  --ansi-2: #4af626;
  --ansi-3: #ffb000;
  --ansi-4: #5fb3ff;
  --ansi-5: #c792ea;
  --ansi-6: #5fffd7;
  --ansi-7: #b8f5a8;
  --ansi-8: #3fa34d;
  --ansi-9: #ff6e6e;
  --ansi-10: #7dff5c;
  --ansi-11: #ffc940;
  --ansi-12: #8fcaff;
  --ansi-13: #ddb3ff;
  --ansi-14: #8affe6;
  --ansi-15: #e8ffe0;
}
''', '''
[data-markdown-preview] {
  text-shadow: 0 0 6px color-mix(in oklch, var(--ink) 28%, transparent);
}

[data-timeline-row-id*=":user"] .bg-surface-recessed::before {
  content: "you@bb $ ";
  color: var(--term-amber);
  font-weight: 800;
}

[data-bb-plugin="hmm-suggest"] button::before {
  content: "> ";
  color: var(--term-dim);
}

[data-bb-plugin="hmm-suggest"] button:hover::before {
  color: inherit;
}

[data-markdown-preview] code {
  color: var(--term-amber);
  background: transparent;
  border: 1px solid var(--term-line);
}

[data-markdown-preview] a {
  color: var(--term-amber);
}

[data-app-content-shell]::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(to bottom, transparent 0 2px, rgb(0 0 0 / 0.18) 2px 3px);
  z-index: 50;
}
''')

themes['liquid-glass']=(''':root,
.light,
.dark {
  --font-sans: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Inter", system-ui, sans-serif;
  --font-mono: "SF Mono", ui-monospace, Menlo, monospace;
  --font-terminal: "SF Mono", Menlo, monospace;

  --canvas: #f4f6fb;
  --ink: #0b1220;
  --primary: #0a6cff;
  --primary-foreground: #ffffff;

  --glass-wallpaper: radial-gradient(60% 50% at 30% 40%, #7fa8ff80, transparent 70%), radial-gradient(50% 50% at 85% 85%, #ffc9a680, transparent 70%), linear-gradient(135deg, #c9dbff, #ebd9f5 50%, #ffe3cc);
  --glass-fill: rgb(255 255 255 / 0.42);
  --glass-fill-strong: rgb(255 255 255 / 0.7);
  --glass-edge: rgb(255 255 255 / 0.75);
  --glass-blur: blur(24px) saturate(180%);
  --glass-shadow: 0 10px 30px -8px rgb(30 42 90 / 0.18), inset 0 1px 0 rgb(255 255 255 / 0.8);
  --glass-link: #0a55cc;
  --bb-sidebar-rail-padding: 16px;
  --bb-sidebar-control-size: 32px;

  --background: transparent;
  --card: var(--glass-fill-strong);
  --popover: rgb(250 251 255 / 0.92);
  --glass-overlay: rgb(250 251 255 / 0.9);
  --sidebar: transparent;
  --sidebar-foreground: var(--ink);
  --sidebar-accent: rgb(255 255 255 / 0.55);
  --sidebar-accent-foreground: var(--ink);
  --sidebar-border: var(--glass-edge);
  --sidebar-ring: var(--primary);
  --border: rgb(11 18 32 / 0.1);
  --border-seam: transparent;
  --border-seam-vertical: transparent;
  --input: rgb(11 18 32 / 0.16);
  --surface-scrim: transparent;

  --muted-foreground: #3c4558;
  --subtle-foreground: #556075;
  --readback-foreground: #4a5468;

  --destructive: #e5212f;
  --destructive-foreground: #ffffff;
  --destructive-text: #c2101d;
  --warning: #b83a00;
  --warning-text: #b83a00;
  --attention: #ff9500;
  --success: #1e9e4a;
  --diff-added: #187c3a;
  --diff-removed: #c2101d;
  --pr-merged: #8944ab;
  --file-accent: #0a55cc;

  --radius: 12px;
  --shadow-lift: var(--glass-shadow);

  --hmm-leading: 1.6;
''' + SPACE + '''  --hmm-chip-gap: 8px;
  --hmm-row-pad: 5px;
  --hmm-radius-xs: 6px;
  --hmm-radius-sm: 999px;
  --hmm-radius-md: 18px;
  --hmm-radius-lg: 26px;
  --hmm-ease: cubic-bezier(0.23, 1, 0.32, 1);
  --hmm-press-duration: 180ms;
  --hmm-press: scale(0.96);
  --hmm-divider: 1px solid transparent;
  --hmm-focus: 3px solid rgb(10 108 255 / 0.45);
  --hmm-selection-bg: rgb(10 108 255 / 0.25);
  --hmm-selection-fg: inherit;
  --hmm-icon-accent: var(--primary);
  --hmm-rail-bg: var(--glass-fill);
  --hmm-rail-active-bg: var(--glass-fill-strong);
  --hmm-rail-active-fg: var(--primary);
  --hmm-rail-active-shadow: 0 2px 6px rgb(30 42 90 / 0.1), inset 0 0 0 1px #ffffff;
  --hmm-sidebar-bg: transparent;
  --hmm-new-bg: var(--glass-fill-strong);
  --hmm-new-fg: var(--ink);
  --hmm-new-shadow: 0 2px 8px rgb(30 42 90 / 0.08), inset 0 0 0 1px #ffffff;
  --hmm-new-shadow-pressed: var(--hmm-new-shadow);
  --hmm-label-font: var(--font-sans);
  --hmm-label-style: normal;
  --hmm-label-size: 11px;
  --hmm-label-transform: none;
  --hmm-label-spacing: 0;
  --hmm-guide: transparent;
  --hmm-active-bg: linear-gradient(135deg, #2f86ff, #0a5ce0);
  --hmm-active-fg: #ffffff;
  --hmm-active-shadow: 0 4px 12px rgb(10 108 255 / 0.3);
  --hmm-card-bg: var(--glass-fill-strong);
  --hmm-card-border: 1px solid #ffffff;
  --hmm-card-shadow: 0 2px 10px rgb(30 42 90 / 0.08);
  --hmm-activity-active-bg: rgb(10 108 255 / 0.1);
  --hmm-activity-active-fg: var(--ink);
  --hmm-header-bg: transparent;
  --hmm-header-fg: inherit;
  --hmm-header-filter: none;
  --hmm-panel-filter: var(--glass-blur);
  --hmm-composer-bg: var(--glass-fill-strong);
  --hmm-composer-border: 1px solid #ffffff;
  --hmm-composer-shadow: 0 12px 32px -8px rgb(30 42 90 / 0.22), inset 0 1px 0 #ffffff;
  --hmm-composer-shadow-focus: var(--hmm-composer-shadow), 0 0 0 4px rgb(10 108 255 / 0.18);
  --hmm-send-bg: linear-gradient(135deg, #2f86ff, #0a5ce0);
  --hmm-send-fg: #ffffff;
  --hmm-send-radius: 999px;
  --hmm-send-shadow: 0 4px 10px rgb(10 108 255 / 0.35);
  --hmm-send-shadow-pressed: 0 2px 4px rgb(10 108 255 / 0.3);
  --hmm-send-disabled-bg: rgb(11 18 32 / 0.08);
  --hmm-send-disabled-shadow: none;
  --hmm-bubble-bg: linear-gradient(135deg, #2f86ff, #0a5ce0);
  --hmm-bubble-fg: #ffffff;
  --hmm-bubble-border: 1px solid rgb(255 255 255 / 0.4);
  --hmm-bubble-radius: 22px;
  --hmm-bubble-shadow: 0 6px 16px rgb(10 108 255 / 0.25), inset 0 1px 0 rgb(255 255 255 / 0.4);
  --hmm-bubble-font: var(--font-sans);
  --hmm-bubble-pill-bg: rgb(255 255 255 / 0.22);
  --hmm-bubble-pill-fg: #ffffff;
  --hmm-bubble-pill-border: transparent;
  --hmm-prose-font: var(--font-sans);
  --hmm-prose-size: 15px;
  --hmm-chip-bg: var(--glass-fill-strong);
  --hmm-chip-fg: var(--glass-link);
  --hmm-chip-border: 1px solid #ffffff;
  --hmm-chip-radius: 999px;
  --hmm-chip-shadow: 0 2px 8px rgb(30 42 90 / 0.08);
  --hmm-chip-shadow-pressed: none;
  --hmm-chip-font: var(--font-sans);
  --hmm-chip-hover-bg: #ffffff;
  --hmm-chip-hover-fg: var(--glass-link);
}
''', '''
:is([role="dialog"], [role="alertdialog"], [role="menu"], [role="listbox"], [data-radix-popper-content-wrapper] > *, [data-slot="dialog-content"], [data-slot="popover-content"]) {
  background-color: var(--glass-overlay);
  backdrop-filter: blur(30px) saturate(180%);
  -webkit-backdrop-filter: blur(30px) saturate(180%);
}

[data-testid="app-layout-root"] {
  background: var(--glass-wallpaper);
  background-attachment: fixed;
}

[data-testid="app-nav-rail"] {
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
}

[data-sidebar="panel"],
main[data-sidebar="inset"] {
  background: transparent;
  border: 0;
}

[data-sidebar="sidebar"] {
  background: var(--glass-fill);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  clip-path: inset(10px round 22px);
  padding-bottom: 10px;
}

[data-testid="app-nav-rail"] button {
  border-radius: 12px;
}

[data-sidebar="sidebar"] [data-testid="app-nav-rail"] {
  background: transparent;
  border-right: 0;
  backdrop-filter: none;
  -webkit-backdrop-filter: none;
}

section[aria-label="Sidebar activity"],
[data-testid="sidebar-footer-row"] {
  background: transparent;
}

[data-framed] [data-sidebar="sidebar"] {
  clip-path: inset(0 var(--bb-window-frame-lip, 8px) 0 var(--bb-window-frame-lip, 8px) round 22px);
  padding-bottom: 0;
}

[data-framed] main[data-sidebar="inset"] {
  border-color: transparent;
}

[data-framed] :is([data-testid="nav-rail-sidebar-body"], [data-sidebar="collapsible-body"]) {
  background: transparent;
  border-color: transparent;
  border-radius: 0;
  clip-path: none;
}

[data-framed] [data-app-content-shell] {
  clip-path: inset(0 round 22px);
  padding-bottom: 0;
}

[data-testid="sidebar-footer-row"] > div {
  background: transparent;
}

[data-sidebar="sidebar"] [data-sidebar="footer"] {
  padding-right: calc(10px + 8px);
}

[data-app-content-shell] {
  background: rgb(255 255 255 / 0.5);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  clip-path: inset(10px 10px 10px 0 round 22px);
  padding-bottom: 10px;
}

[data-sidebar="sidebar"] span.select-none.uppercase {
  font-weight: 600;
}
''')

for name,(head,extra) in themes.items():
    css=head.strip('\n')+'\n\n'+BASE+extra
    open(os.path.join(OUT,name+'.css'),'w').write(css)
    print(name, len(css))
