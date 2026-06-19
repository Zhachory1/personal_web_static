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

## Status

Migrating to another service, but this repo remains the source for the static portfolio site.
