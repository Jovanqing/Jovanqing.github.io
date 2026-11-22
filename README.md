# yongqingjiang.com

Source of Yongqing Jiang's academic homepage, https://yongqingjiang.com, built with Jekyll and served by GitHub Pages.
Based on [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) by Yi Ren (MIT License, see `LICENSE`).

## Where things live
- Page content: `_pages/about.md`
- Site settings and author profile: `_config.yml`
- Layout, styles, scripts: `_layouts/`, `_includes/`, `_sass/` (`_sass/_modern.scss` holds the custom theme)

## Preview locally
1. Install Ruby and Bundler, then run `bundle install`.
2. Run `bash run_server.sh` (or `bundle exec jekyll serve --livereload`) and open http://127.0.0.1:4000.

## Citations badge
The workflow `.github/workflows/google_scholar_crawler.yaml` runs every 3 days (or manually). It calls SerpApi via
`google_scholar_crawler/main.py`, writes `gs_data_shieldsio.json`, and force-pushes it to the `google-scholar-stats`
branch. The sidebar badge reads that file through jsDelivr and shields.io.

## Acknowledgements
- AcadHomepage is influenced by [mmistakes/minimal-mistakes](https://github.com/mmistakes/minimal-mistakes) and
  [academicpages/academicpages.github.io](https://github.com/academicpages/academicpages.github.io), both MIT License.
- Includes Font Awesome (SIL OFL 1.1 and MIT License).
