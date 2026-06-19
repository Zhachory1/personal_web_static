# personal_web_static

Static files for my personal website.

## Structure

- `src/` — source HTML/CSS/JS/assets
- `public/` — compiled static site output
- `bundle.py` — copies assets from `src/` to `public/`, minifies JS, and optionally injects Google Analytics when `GTAGID` is set

The root `package.json` is the only Node entrypoint. Older nested `src/package*` files were removed to avoid ambiguity.

## Commands

```bash
npm install
npm run build
npm run serve
npm test
```

- `npm run build` rebuilds `public/` from `src/`.
- `npm run serve` serves `public/` at <http://localhost:8000>.
- `npm test` runs static QA for local links/images, viewport metadata, social metadata, and mobile navigation markup.

## Migration / deploy workflow

This repo remains the source of truth for the static portfolio until the migration is complete.

1. Edit files in `src/`.
2. Run `npm test`.
3. Run `npm run build` to regenerate `public/` for local preview/deploy packaging.
4. Serve with `npm run serve` and verify the homepage/resume links.
5. When a new host replaces this repo, archive it by freezing `src/`, documenting the target host here, and disabling any old deploy hooks.

Generated binaries such as the PyInstaller `bundle` executable are intentionally not tracked.
