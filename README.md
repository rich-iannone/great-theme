# Great Theme for Quarto-Based Documentation Sites

This is comprehensive theming package that provides enhanced styling and functionality for Python documentation sites built with Quarto and `quartodoc`.

## Features

- enhanced typography: monospace fonts for code elements and improved readability
- smart classification: automatic function/method/class labeling with color-coded badges
- modern styling: clean, professional appearance with gradient effects
- mobile responsive: optimized for all device sizes
- easy installation: simple CLI tool for quick setup
- zero configuration: works out of the box with sensible defaults

## Quick Start

### Installation

#### From PyPI (when published)

```bash
pip install great-theme
```

#### From GitHub

Install the latest version directly from the GitHub repository:

```bash
pip install git+https://github.com/rich-iannone/great-theme.git
```

Or install a specific branch, tag, or commit:

```bash
# Install from a specific branch
pip install git+https://github.com/rich-iannone/great-theme.git@main

# Install from a specific tag
pip install git+https://github.com/rich-iannone/great-theme.git@v0.1.0

# Install from a specific commit
pip install git+https://github.com/rich-iannone/great-theme.git@abc1234
```

For development or editable installation:

```bash
# Clone the repository
git clone https://github.com/rich-iannone/great-theme.git
cd great-theme

# Install in editable mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

### Apply to Your Project

Navigate to your project root directory and run:

```bash
great-theme install
```

The installer will:

1. Automatically detect existing documentation directories (`docs/`, `site/`, etc.)
2. Look for existing `_quarto.yml` files to determine the correct location
3. Prompt you to choose a location if no docs directory is found
4. Install all necessary files to the detected or chosen directory

That's it! The theme will automatically enhance your documentation site.

## What Gets Enhanced

Great Theme automatically improves your quartodoc site through:

### Visual Enhancements

- **function signatures** styled with monospace fonts
- **type annotations** with improved formatting
- **parameter descriptions** with better spacing
- **code blocks** with enhanced syntax highlighting

### Smart Labeling

- **classes** get green labels and styling
- **methods** get blue labels (e.g., `Class.method()`)
- **functions** get orange labels (e.g., `function()`)

### Responsive Design

- mobile-friendly navigation
- optimized sidebar behavior
- touch-friendly interface elements

### Interactive Elements

- animated gradient headers for Examples sections
- hover effects on navigation elements
- smooth transitions and animations

## Usage

### CLI Commands

```bash
# Install theme (auto-detects docs directory)
great-theme install

# Install to specific docs directory
great-theme install --docs-dir docs

# Install to specific project
great-theme install --project-path /path/to/project

# Install with specific docs directory in a project
great-theme install --project-path /path/to/project --docs-dir documentation

# Force overwrite existing files
great-theme install --force

# Remove theme from project
great-theme uninstall

# Uninstall from specific docs directory
great-theme uninstall --docs-dir docs
```

### Python API

```python
from great_theme import GreatTheme

# Initialize for current directory (auto-detects docs dir)
theme = GreatTheme()

# Install theme files and configuration
theme.install()

# Initialize with specific project root
theme = GreatTheme(project_path="/path/to/project")
theme.install()

# Initialize with specific docs directory
theme = GreatTheme(project_path="/path/to/project", docs_dir="docs")
theme.install()

# Remove theme
theme.uninstall()
```

## What Gets Installed

When you run `great-theme install`, the following files are added to your documentation directory:

```
your-project/
├── docs/                # Or your chosen docs directory
│   ├── _quarto.yml      # Updated with theme configuration
│   ├── great-theme.css  # Main theme stylesheet
│   └── scripts/
│       └── post-render.py   # HTML post-processing script
```

If you have an existing `_quarto.yml` or documentation directory, great-theme will detect and use it.

## Configuration

The theme works with your existing `_quarto.yml` configuration. After installation, your config will include:

```yaml
project:
  type: website
  post-render: scripts/post-render.py

format:
  html:
    theme: flatly # Recommended base theme
    css:
      - great-theme.css
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
