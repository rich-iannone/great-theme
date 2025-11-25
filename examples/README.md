# Example Quarto Configuration with Great Theme

This example shows how to configure your quartodoc project to use great-theme.

## Method 1: Using the CLI (Recommended)

After installing great-theme, simply run:

```bash
great-theme init
```

This will automatically:

- Copy the post-render script to `scripts/post-render.py`
- Copy the CSS file to `great-theme.css`
- Update your `_quarto.yml` configuration

## Method 2: Manual Configuration

### 1. Basic \_quarto.yml setup

```yaml
project:
  type: website
  post-render: scripts/post-render.py

format:
  html:
    theme: flatly # Works well with great-theme
    css:
      - great-theme.css
    toc: true
    grid:
      sidebar-width: 270px
      body-width: 950px
      margin-width: 225px
      gutter-width: 1rem

website:
  title: "Your Project Name"
  navbar:
    logo: assets/logo.png # Optional
```

### 2. Copy theme files

```python
from great_theme import GreatTheme

# Initialize theme for current directory
theme = GreatTheme()

# Install theme files
theme.install()
```

## Customization

You can customize the theme by:

1. Editing the copied `great-theme.css` file
2. Modifying the `scripts/post-render.py` script
3. Adding additional CSS files to your `_quarto.yml`
