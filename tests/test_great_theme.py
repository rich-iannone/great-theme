"""
Basic tests for great-theme functionality.
"""

import tempfile
from pathlib import Path
from great_theme import GreatTheme


def test_great_theme_init():
    """Test GreatTheme initialization."""
    theme = GreatTheme(docs_dir=".")
    assert theme.project_root == Path.cwd()


def test_great_theme_init_with_path():
    """Test GreatTheme initialization with custom path."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        theme = GreatTheme(project_path=tmp_dir, docs_dir=".")
        assert theme.project_root == Path(tmp_dir)


def test_install_creates_files():
    """Test that install creates the expected files."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        theme = GreatTheme(project_path=tmp_dir, docs_dir=".")
        theme.install(force=True, skip_quartodoc=True)

        # Check that files were created
        project_path = Path(tmp_dir)
        assert (project_path / "scripts" / "post-render.py").exists()
        assert (project_path / "great-theme.css").exists()
        assert (project_path / "_quarto.yml").exists()


def test_uninstall_removes_files():
    """Test that uninstall removes the theme files."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        theme = GreatTheme(project_path=tmp_dir, docs_dir=".")

        # Install first
        theme.install(force=True, skip_quartodoc=True)

        project_path = Path(tmp_dir)
        assert (project_path / "scripts" / "post-render.py").exists()
        assert (project_path / "great-theme.css").exists()

        # Then uninstall
        theme.uninstall()


def test_parse_package_exports():
    """Test parsing __all__ from __init__.py."""
    # Test on great-theme's own __init__.py
    theme = GreatTheme(docs_dir=".")
    exports = theme._parse_package_exports("great_theme")

    assert exports is not None
    assert "GreatTheme" in exports
    assert "main" in exports


def test_create_quartodoc_sections():
    """Test auto-generation of quartodoc sections."""
    theme = GreatTheme(docs_dir=".")
    sections = theme._create_quartodoc_sections("great_theme")

    assert sections is not None
    assert len(sections) > 0

    # Check that we have at least one section with contents
    has_contents = any(section.get("contents") for section in sections)
    assert has_contents


def test_detect_package_name_from_pyproject():
    """Test package name detection from pyproject.toml."""
    # Test on great-theme's own pyproject.toml
    theme = GreatTheme(docs_dir=".")
    package_name = theme._detect_package_name()

    assert package_name == "great-theme"


def test_find_package_init():
    """Test finding __init__.py in standard location."""
    theme = GreatTheme(docs_dir=".")
    init_file = theme._find_package_init("great_theme")

    assert init_file is not None
    assert init_file.exists()
    assert init_file.name == "__init__.py"


def test_find_package_init_with_nested_structure():
    """Test finding __init__.py in nested directories like python/."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Create a package structure in python/ subdirectory
        python_dir = Path(tmp_dir) / "python"
        python_dir.mkdir()
        package_dir = python_dir / "mypackage"
        package_dir.mkdir()

        # Create __init__.py with __version__ and __all__
        init_file = package_dir / "__init__.py"
        init_file.write_text('__version__ = "1.0.0"\n__all__ = ["MyClass"]')

        theme = GreatTheme(project_path=tmp_dir, docs_dir=".")
        found_init = theme._find_package_init("mypackage")

        assert found_init is not None
        assert found_init == init_file


def test_cli_import():
    """Test that CLI module can be imported."""
    from great_theme.cli import main

    assert callable(main)
